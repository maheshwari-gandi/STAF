*** Settings ***
Library   AppiumLibrary
Library   ${EXECDIR}/TestSuites/Facebook/Libraries/get_input_from_excel.py


*** Variables ***
${username}
${password}


*** Keywords ***
Create contact
        Log To Console  ${EXECDIR}
        [Arguments]     ${test_case_num}
        sleep   15
        Click Element   //android.view.View[@content-desc="Mobile number or email address"]
        ${username}     ${password}      get_input_from_excel.read_excel_data         ${test_case_num}
        sleep   3
        Input Text      xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText         ${username}
        Click Element   //android.view.View[@content-desc="Password"]
        Input Text      xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText      ${password}
        Click Element   xpath=//android.view.View[@content-desc="Log In"]
        sleep   10


Search account

        [Arguments]     ${test_case_num}
        Click Element   //android.view.ViewGroup[@content-desc="Deny"]
        Click Element   //android.widget.Button[@content-desc="Search"]
        ${search_name}  get.input_from_excel.read_excel_data   ${test_case_name}
        Input Text      /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText     ${search_name}
