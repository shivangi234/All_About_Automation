*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/AddToCartKeywords.robot
*** Variables ***
${Browser}      headlesschrome
${firstname}    Shivangi
${lastname}     Sahu
${postalcode}   411067

*** Test Cases ***
Shopping Cart Update
        Open SauceLab Browser    ${Browser}
        ${username}    ${password}=    Get Credentials From Page
        Enter Username    ${username}
        Enter Password    ${password}
        Click Login

        Verify Successful Login
        Sleep    3s
        Click BagPack
        Click FleeceJacket
        Go To Cart
        Verify Page Contents
        Click CheckOut
        Enter Firstname     ${firstname}
        Enter Lastname      ${lastname}
        Enter PostalCode    ${postalcode}
        Enter Continue
        Verify Price With Tax
        Click Finish
        Verify Order Success Message
        Close SauceLab Browser