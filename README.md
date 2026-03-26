# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
![Use Case Diagram](UseCaseDiagram.jpg)

### Flowchart of the main workflow
```mermaid
---
config:
      theme: redux
---
flowchart TD
    A(["Start"])
    A --> B{"Login as?"}
    
    B --Student--> C{"Student Menu"}
        C --View Course Catalog--> G["Show Course Catalog"]
        G --> X

        C --Register for a Course--> H["Input Course Code"]
        H --> I["Enrollment Result"]
        I --> X

        C --Drop a Course--> J["Input Course Code"]
        J --> K["Dropping Result"]
        K --> X

        C --View My Schedule--> L["Show My Schedule"]
        L --> X

        C --Billing Summary--> M["Show Billing Summary"]
        M --> X

        C --Edit My Profile--> N["Input New Profile Details"]
        N --> X

        C --Logout and Save--> F["Logout and Save"]
        F --> B

        X{"Done?"}
        X --True--> B
        X --False--> C
    
    B --Admin--> D["Admin Menu"]
        D --View Course Catalog--> O["Show Course Catalog"]
        O --> Y

        D --View Class Roster--> P["Show Class Roster"]
        P --> Y

        D --View All Students--> Q["Show All Students"]
        Q --> Y

        D --Add New Student--> R["Input Student Details"]
        R --> S["Adding Result"]
        S --> Y

        D --Edit Student Profile--> T["Input New Profile Details"]
        T --> Y

        D --Add New Course--> U["Input Course Details"]
        U --> Y

        D --Edit Course--> V["Input New Course Details"]
        V --> Y

        D --View Student Schedule--> W["Show Student Schedule"]
        W --> Y

        D --Billing Summary--> Z["Input Student ID"]
        Z --> AA["Show Billing Summary"]
        AA --> Y

        D --Logout and Save--> BB["Logout and Save"]
        BB --> B

        Y{"Done?"}
        Y --True--> B
        Y --False--> D

    B --Exit--> E(["Stop"])
```
### Prompts
In viewCatalog.py, create equivalent viewCourseCatalog() program in python based on the Main.java and EnrollmentSystem.java
