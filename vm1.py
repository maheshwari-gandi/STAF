import os
import subprocess
import signal
import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pathlib import Path
import psutil
import subprocess
import re

def setup(citrix_url,username,password,virtual_machine,status):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))#,options=chrome_options))
    driver.get(citrix_url)
    driver.maximize_window()
    time.sleep(8)
    driver.find_element(By.XPATH,"//button[@id='details-button']").click()
    driver.find_element(By.XPATH,"//a[@id='proceed-link']").click()
    time.sleep(5)
    print(driver.title)
    driver.find_element(By.XPATH,"//h1[normalize-space()='Welcome to Citrix Workspace app']").is_displayed()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[normalize-space()='Detect Citrix Workspace app']").click()
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(5)
    pyautogui.press("enter")
    driver.find_element(By.XPATH,"//a[@id='protocolhandler-detect-alreadyInstalledLink']").click()
    time.sleep(60)
    driver.find_element(By.XPATH,"//input[@id='username']").send_keys(username)
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[@id='loginBtn']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,f"//p[normalize-space()='{virtual_machine}']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//div[@class='theme-highlight-color appDetails-actions-text'][normalize-space()='Open']").click()
    time.sleep(3)
    home_directory = Path.home()
    print(home_directory)
    download_dir = f"{home_directory}/Downloads"
    files = [f for f in os.listdir(download_dir) if f.endswith('.ica')]
    print(files)
    paths = [os.path.join(download_dir, basename) for basename in files]
    print(paths)
    latest_file = max(paths, key=os.path.getctime)
    print(latest_file)
    process = subprocess.Popen(['open', latest_file])
    # process=subprocess.call(('open', latest_file))
    time.sleep(10)
    print(process.pid)
    # subprocess.run(['pkill','-f','pycharm'],check=True)
    # time.sleep(10)
    status=False
    return status

citrix_url = "https://10.91.237.221/Citrix/storeWeb/"
username = "administrator@mypoc.local"
password = "Test@123"
virtual_machine = "Win2k19"
status=True
for i in range(1,4):
    if True:
        setup(citrix_url,username,password,virtual_machine,status)
        print(f"Connected to VM {virtual_machine}")
        break
    else:
        print(f"trying {i} time to connect to VM")
else:
    print(f"Error while connecting VM {virtual_machine}")

