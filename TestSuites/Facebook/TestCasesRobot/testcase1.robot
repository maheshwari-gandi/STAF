*** Settings ***
Library   BuiltIn
Library   AppiumLibrary

Resource    ${EXECDIR}/TestSuites/Facebook/TestCasesRobot/Resources/create_account.robot

Suite Setup  Open Application	${REMOTE_URL}	platformName=Android	platformVersion=10	deviceName=samsung	appPackage=com.facebook.katana 	appActivity=com.facebook.katana.activity.FbMainTabActivity
Suite Teardown  Close All Applications
*** Variables ***

${REMOTE_URL}  http://127.0.0.1:4723/wd/hub

*** Test Cases ***

TC001
        [Documentation]         create account with valid username and password
        create_account.Create contact          TC001

TC002   [Documentation]         search for an account
        create_account.Search account          TC002



