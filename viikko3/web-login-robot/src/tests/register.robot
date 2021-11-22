*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jaakko
    Set Password  jaakko123
    Set Password Confirmation  jaakko123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  j
    Set Password  jaakko123
    Set Password Confirmation  jaakko123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  jaakko
    Set Password  jaakko1
    Set Password Confirmation  jaakko1
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  jaakko
    Set Password  jaakko123
    Set Password Confirmation  jaakko456
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation not matching

Login After Successful Registration
    Set Username  jaakko
    Set Password  jaakko123
    Set Password Confirmation  jaakko123
    Submit Credentials
    Go To Login Page
    Set Username  jaakko
    Set Password  jaakko123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  j
    Set Password  jaakko1
    Set Password Confirmation  jaakko1
    Submit Credentials
    Go To Login Page
    Set Username  j
    Set Password  jaakko1
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
