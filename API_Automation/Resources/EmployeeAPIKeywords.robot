*** Settings ***
Library     RequestsLibrary
Resource    ../PageObjects/Locators.robot

*** Keywords ***
Init API Session
    [Arguments]    ${session_name}=api
    Create Session    ${session_name}    ${BASE_URL}

Get All Users
    [Arguments]    ${session_name}=api
    ${response}=    GET On Session    ${session_name}    ${ENDPOINT_ALL}
    RETURN    ${response}

Get User By ID
    [Arguments]    ${session_name}=api
    ${response}=    GET On Session    ${session_name}    ${ENDPOINT_ID}
    RETURN    ${response}
Create User
    [Arguments]    ${data}    ${session_name}=api
    ${response}=    POST On Session    ${session_name}    ${ENDPOINT_ALL}    json=${data}
    RETURN    ${response}
Update User
    [Arguments]    ${data}    ${user_id}=1    ${session_name}=api
    ${response}=    PUT On Session    ${session_name}    /users/${user_id}    json=${data}
    RETURN    ${response}
Delete User
    [Arguments]    ${user_id}=1    ${session_name}=api
    ${response}=    DELETE On Session    ${session_name}    /users/${user_id}
    RETURN    ${response}
