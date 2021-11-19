*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testi  testi123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  testi123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  testi123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  testi  test1
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testi  testitesti
    Output Should Contain  Password should not contain ony letters 

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command