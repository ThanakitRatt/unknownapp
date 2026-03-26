#!/usr/bin/env python3
"""
Python equivalent of Main.java::viewCourseCatalog().

This script prints the course catalog in a table format similar to the Java CLI.
It is intentionally data-shape tolerant:
- Each course can be a dict (from JSON) or an object with attributes/getters.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable, List

SEPARATOR = "=" * 70
THIN_SEP = "-" * 70


def _read_course_field(course: Any, key: str, default: Any = "") -> Any:
    """Read a course field from dict-like or object-like inputs."""
    if isinstance(course, dict):
        return course.get(key, default)

    # Attribute access
    if hasattr(course, key):
        return getattr(course, key)

    # Java-style getter fallback, e.g. getCode/getTitle
    getter = f"get{key[:1].upper()}{key[1:]}"
    if hasattr(course, getter):
        method = getattr(course, getter)
        if callable(method):
            try:
                return method()
            except TypeError:
                pass

    return default


def _format_course_row(course: Any) -> str:
    code = str(_read_course_field(course, "code", ""))
    title = str(_read_course_field(course, "title", ""))
    credits = _read_course_field(course, "credits", "")
    capacity = _read_course_field(course, "capacity", "")
    enrolled = _read_course_field(course, "enrolledStudents", [])
    time_slot = _read_course_field(course, "timeSlot", "")
    prerequisites = _read_course_field(course, "prerequisites", [])

    # Seats column similar to Java output style: enrolled/capacity
    enrolled_count = len(enrolled) if isinstance(enrolled, list) else 0
    seats = f"{enrolled_count}/{capacity}" if str(capacity) != "" else str(enrolled_count)

    if isinstance(time_slot, dict):
        days = time_slot.get("days", "")
        start = time_slot.get("startTime", "")
        end = time_slot.get("endTime", "")
        time_text = f"{days} {start}-{end}".strip()
    else:
        time_text = str(time_slot) if time_slot is not None else ""

    prereq_text = ", ".join(prerequisites) if isinstance(prerequisites, list) and prerequisites else "None"

    return f"  {code:<10} {title:<40} {str(credits):<8} {seats:<12} {time_text:<18} {prereq_text}"


def print_course_header() -> None:
    print(f"  {'Code':<10} {'Title':<40} {'Credits':<8} {'Seats':<12} {'Time':<18} Prerequisites")
    print(f"  {THIN_SEP}")


def view_course_catalog(courses: Iterable[Any]) -> None:
    """
    Equivalent behavior to Main.java::viewCourseCatalog():
    - print title block
    - handle empty course list
    - print header + each course row
    """
    print()
    print(SEPARATOR)
    print("  COURSE CATALOG")
    print(SEPARATOR)

    # Materialize once for emptiness check and stable iteration
    course_list: List[Any] = list(courses)
    if not course_list:
        print("  No courses available.")
        return

    print_course_header()
    for course in course_list:
        print(_format_course_row(course))


def _load_courses_from_json() -> List[dict]:
    # Path relative to this script: ../data/courses.json
    path = Path(__file__).resolve().parent.parent / "data" / "courses.json"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data if isinstance(data, list) else []


def main() -> None:
    courses = _load_courses_from_json()
    view_course_catalog(courses)


if __name__ == "__main__":
    main()