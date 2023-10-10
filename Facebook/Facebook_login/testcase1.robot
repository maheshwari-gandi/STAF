*** Settings ***
Library   BuiltIn
Library   AppiumLibrary


Suite Setup  Open Application	${REMOTE_URL}	platformName=Android	platformVersion=10	deviceName=samsung	appPackage=com.facebook.katana 	appActivity=com.facebook.katana.activity.FbMainTabActivity
Suite Teardown  Close All Applications

*** Variables ***

${REMOTE_URL}  http://127.0.0.1:4723/wd/hub
${username}     7989693368
${password}     Mahi@3130
${search_name}  Narayana Gandi

*** Test Cases ***


TC001
    Create contact

TC002
    Search account



*** Keywords ***
Create contact
        sleep   15
        Click Element   //android.view.View[@content-desc="Mobile number or email address"]
        sleep   3
        Input Text      xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText         ${username}
        Click Element   //android.view.View[@content-desc="Password"]
        Input Text      xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText      ${password}
        Click Element   xpath=//android.view.View[@content-desc="Log In"]
        sleep   10


Search account
        Click Element   //android.view.ViewGroup[@content-desc="Deny"]
        Click Element   //android.widget.Button[@content-desc="Search"]
        Input Text      /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText     ${search_name}




