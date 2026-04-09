*** Settings ***
Library     SeleniumLibrary
Library     String
Resource    ../PageObjects/Locators.robot

*** Keywords ***
Open SauceLab Browser
    [Arguments]    ${Browser}

    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver

    # Add arguments
    Call Method    ${options}    add_argument    --incognito
    Call Method    ${options}    add_argument    --start-maximized

    # Disable password manager
    ${prefs}=    Create Dictionary
    ...    credentials_enable_service=False
    ...    profile.password_manager_enabled=False

    Call Method    ${options}    add_experimental_option    prefs    ${prefs}

    Open Browser    ${URL}    ${Browser}    options=${options}
    Maximize Browser Window

Get Credentials From Page
    ${user_text}=    Get Text    xpath://div[@id='login_credentials']
    ${pass_text}=    Get Text    xpath://div[@class='login_password']

    ${user_lines}=    Split To Lines    ${user_text}
    ${pass_lines}=    Split To Lines    ${pass_text}

    ${username}=    Set Variable    ${user_lines}[1]
    ${password}=    Set Variable    ${pass_lines}[1]

    RETURN    ${username}    ${password}



Enter Username
        [Arguments]     ${username}
        Wait Until Element Is Visible    ${TXT_USER_NAME}   5s
        Input Text    ${TXT_USER_NAME}    ${username}
Enter Password
        [Arguments]     ${password}
        Input Text    ${TXT_PASSWORD}    ${password}
Click Login
        Wait Until Element Is Visible    ${LOGIN_BTN}    5s
        Click Element    ${LOGIN_BTN}
Verify Successful Login
        Page Should Contain    Sauce Labs Backpack
Click BagPack
        Wait Until Element Is Visible    ${CLICK_BOLT_T_SHIRT}     5s
        Click Button    ${CLICK_BOLT_T_SHIRT}
Click FleeceJacket
        Wait Until Element Is Visible    ${CLICK_FLEECE_JACKET}      10s
        Click Button    ${CLICK_FLEECE_JACKET}
Go To Cart
        Wait Until Element Is Visible       ${CLICK_CART_ICON}        5s
        Click Element    ${CLICK_CART_ICON}
Verify Page Contents
        Page Should Contain     Sauce Labs Bolt T-Shirt
        Page Should Contain     Sauce Labs Fleece Jacket

Click CheckOut
        Wait Until Element Is Visible    ${CLICK_CHEKOUT}       10s
        Click Element    ${CLICK_CHEKOUT}
Enter Firstname
        [Arguments]     ${firstname}
        Wait Until Element Is Visible    ${ENTER_FIRSTNAME}   10s
        Input Text    ${ENTER_FIRSTNAME}    ${firstname}
Enter Lastname
        [Arguments]     ${lastname}
        Wait Until Element Is Visible    ${ENTER_LASTNAME}   5s
        Input Text    ${ENTER_LASTNAME}    ${lastname}
Enter PostalCode
        [Arguments]     ${postalcode}
        Wait Until Element Is Visible    ${ENTER_POSTAL_CODE}   5s
        Input Text    ${ENTER_POSTAL_CODE}    ${postalcode}
Enter Continue
        Wait Until Element Is Visible       ${CONTINUE}     3s
        Click Element    ${CONTINUE}

Verify Price With Tax
    Wait Until Element Is Visible    ${PRICE_BOLT}      10s
    Wait Until Element Is Visible    ${PRICE_JACKET}    10s
    ${bolt_price}=    Get Text    ${PRICE_BOLT}

    ${jacket_price}=  Get Text    ${PRICE_JACKET}

    ${item_total}=    Get Text    ${ITEM_TOTAL}
    ${total}=         Get Text    ${TOTAL_WITH_TAX}

    # Remove text and keep numbers
    ${bolt}=    Evaluate    float('${bolt_price}'.replace('$',''))
    ${jacket}=  Evaluate    float('${jacket_price}'.replace('$',''))

    ${sum}=     Evaluate    ${bolt} + ${jacket}

    ${total_value}=    Evaluate    float('${total}'.split('$')[1])

    Should Be True    ${total_value} > ${sum}

Click Finish
        Wait Until Element Is Visible    ${FINISH}      5s
        Click Element    ${FINISH}
Verify Order Success Message
        Wait Until Element Is Visible    ${SUCCESS_MESSAGE}    5s
        Element Text Should Be    ${SUCCESS_MESSAGE}    Thank you for your order!

Close SauceLab Browser
        Close All Browsers