*** Settings ***
Resource        ../Resources/EmployeeAPIKeywords.robot

*** Test Cases ***
Verify Get All Users
    Init API Session
    ${response}=    Get All Users
    Should Be Equal As Integers    ${response.status_code}    200
    Log    ${response.json()}

Verify Get User By ID
    Init API Session
    ${response}=    Get User By ID
    Should Be Equal As Integers    ${response.status_code}    200
    Log    ${response.json()}
Verify Create User
    Init API Session
    ${data}=    Create Dictionary    name=John Doe    username=johndoe    email=john@example.com
    ${response}=    Create User    ${data}
    Should Be Equal As Integers    ${response.status_code}    201
    Log    ${response.json()}
Verify Update User
    Init API Session
    ${data}=    Create Dictionary    name=Jane Doe    username=janedoe    email=jane@example.com
    ${response}=    Update User    ${data}    1
    Should Be Equal As Integers    ${response.status_code}    200
    Log    ${response.json()}
Verify Delete User
    Init API Session
    ${response}=    Delete User    1
    Should Be Equal As Integers    ${response.status_code}    200
    Log    ${response.json()}