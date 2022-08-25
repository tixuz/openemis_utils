# Openemis Selenium
## How To Install Requered Libraries

Run
```
pip install -r requirements.txt
```

## How To Run Selenium

1. Please write necessary information into config.py

2. If the "chromedriver" file in this folder is incompatible with your version of Chrome, download the compatible version and change path to it in config.py

3. Run open_core_chrome.py

## How To Get API Bearer token

4. Create key pair
```
ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
# Don't add passphrase
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub
cat jwtRS256.key
cat jwtRS256.key.pub
```

5.
    a) Create new Credentials in OpenEMIS Core;
    b) copy all from jwtRS256.key.pub to Public Key field
    c) Copy Client Id from Credentials and paste it to config.py iss variable value

### Example

```
iss = "1661365366-d6277c12d6e9f67a.app"
```

7. run get_core_assertion.py

8. you can try if the assertion works, using postman or running get_institutions_via_api.py

## Examples of API requests to OpenEMIS Core
```
//curl -i -X GET https://demo.openemis.org/core/restful/User.Users.json
//curl -i -X GET https://demo.openemis.org/core/restful/User.Users.json?_contain=Genders
//curl -i -X GET https://demo.openemis.org/core/restful/User.Users.json?_fields=username,Genders.name&_contain=Genders
//curl -i -X GET https://demo.openemis.org/core/restful/User.Users.json?_order=-first_name,last_name
//curl -i -X GET https://demo.openemis.org/core/restful/User.Users.json?_limit=10&_page=2
```

## API Models and their Addresses

| API Name                                        | API Address                                  | Index | View | Add  | Edit | Delete  | Execute  |
|-------------------------------------------------|----------------------------------------------|-------|------|------|------|---------|----------|
|   Institutions                                  |   Institution.Institutions                   |   1   |   1  |   1  |   1  |   0     |   0      |
|   Users                                         |   User.Users                                 |   1   |   1  |   1  |   1  |   0     |   0      |
|   Classes                                       |   Institution.InstitutionClasses             |   1   |   1  |   0  |   0  |   0     |   0      |
|   Student Admission                             |   Institution.StudentAdmission               |   1   |   1  |   1  |   1  |   0     |   0      |
|   Gender                                        |   Institution.Genders                        |   1   |   1  |   0  |   0  |   0     |   0      |
|   Institution Types                             |   Institution.Types                          |   1   |   1  |   0  |   0  |   0     |   0      |
|   Institution Providers                         |   Institution.Providers                      |   1   |   1  |   0  |   0  |   0     |   0      |
|   Institution Sectors                           |   Institution.Sectors                        |   1   |   1  |   0  |   0  |   0     |   0      |
|   Institution Ownerships                        |   Institution.Ownerships                     |   1   |   1  |   0  |   0  |   0     |   0      |
|   Institution Localities                        |   Institution.Localities                     |   1   |   1  |   0  |   0  |   0     |   0      |
|   Institution AreaAdministratives               |   Institution.AreaAdministratives            |   1   |   1  |   0  |   0  |   0     |   0      |
|   User Nationalities                            |   User.Nationalities                         |   1   |   1  |   0  |   0  |   0     |   0      |
|   Nationality Names                             |   User.NationalityNames                      |   1   |   1  |   0  |   0  |   0     |   0      |
|   Create Student                                |   Institution.Students                       |   1   |   1  |   1  |   1  |   0     |   0      |
|   Identity Types                                |   FieldOption.IdentityTypes                  |   1   |   1  |   0  |   0  |   0     |   0      |
|   Areas                                         |   Area.Areas                                 |   1   |   1  |   1  |   1  |   0     |   0      |
|   Status                                        |   Student.StudentStatuses                    |   1   |   1  |   1  |   1  |   0     |   0      |
|   AcademicPeriod                                |   AcademicPeriod.AcademicPeriods             |   1   |   1  |   1  |   1  |   0     |   0      |
|   Education                                     |   Education.EducationGrades                  |   1   |   1  |   1  |   1  |   0     |   0      |
|   Security User                                 |   Security.Users                             |   1   |   1  |   0  |   0  |   0     |   0      |
|   Security User Groups                          |   Security.UserGroups                        |   1   |   1  |   0  |   0  |   0     |   0      |
|   Security Role Functions                       |   Security.SecurityRoleFunctions             |   1   |   0  |   0  |   0  |   0     |   0      |
|   Staff                                         |   Institution.Staff                          |   1   |   0  |   0  |   0  |   0     |   0      |
|   Institution Student Attendances               |   Institution.StudentAttendances             |   1   |   1  |   0  |   0  |   0     |   0      |
|   Institution Student Absence Period Details    |   Institution.StudentAbsencesPeriodDetails   |   1   |   1  |   1  |   1  |   0     |   0      |
|   Attendance Student Attendance Marked Records  |   Attendance.StudentAttendanceMarkedRecords  |   1   |   1  |   1  |   1  |   0     |   0      |
|   Institution Staff                             |   Institution.Staff                          |   1   |   1  |   1  |   1  |   0     |   0      |
|   UserGender                                    |   User.Genders                               |   1   |   1  |   0  |   0  |   0     |   0      |
|   Subjects                                      |   Institution.InstitutionClassSubjects       |   1   |   1  |   1  |   1  |   0     |   0      |
|   StudentAttendanceTypes                        |   Attendance.StudentAttendanceTypes          |   1   |   1  |   1  |   1  |   0     |   0      |
|   User Authentication                           |   User.Users                                 |   0   |   0  |   0  |   0  |   0     |   1      |
|   Institution Absence Types                     |   Institution.AbsenceTypes                   |   1   |   1  |   1  |   1  |   0     |   0      |
|   Institution Student Absence Reasons           |   Institution.StudentAbsenceReasons          |   1   |   1  |   1  |   1  |   0     |   0      |
|   Institution Staff Attendances                 |   Staff.InstitutionStaffAttendances          |   1   |   1  |   1  |   1  |   0     |   0      |
|   Payslips                                      |   Staff.StaffPayslips                        |   0   |   0  |   1  |   0  |   0     |   0      |
|   Security Group Users                          |   Security.SecurityGroupUsers                |   1   |   1  |   0  |   0  |   0     |   0      |
|   Assessment                                    |   Assessment.Assessments                     |   1   |   1  |   1  |   1  |   0     |   0      |
|   Teacher Subjects                              |   Institution.InstitutionSubjectStaff        |   1   |   1  |   1  |   1  |   0     |   0      |
