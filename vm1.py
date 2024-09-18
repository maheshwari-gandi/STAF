import os
import subprocess

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.core.driver import Driver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_experimental_option("prefs",{"protocol_handler.excluded_schemes":{"https":False}})


#
# chrome_options = Options()
# chrome_options.add_argument('--allow-insecure-localhost')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--ignore-ssl-errors')
# chrome_options.add_argument('--disable-notifications')
# chrome_options.add_argument('--acceptInsecureCerts')
#
# path_to_cookies = '~/.config/google-chrome/Default/Cookies'
# user_data_dir='~/.config/google-chrome'
# chrome_options.add_argument('-cookies-load-from='+path_to_cookies)
# chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
# # Optional: Specify a profile within the user data directory
# chrome_options.add_argument('--profile-directory=Default')
# caps = webdriver.DesiredCapabilities.CHROME.copy()
# caps['acceptInsecureCerts'] = True
# driver = webdriver.Chrome(desired_capabilities=caps)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(),options=chrome_options))
driver.get("https://10.91.237.221/Citrix/storeWeb/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='details-button']").click()
driver.find_element(By.XPATH,"//a[@id='proceed-link']").click()
time.sleep(10)
print(driver.title)
driver.find_element(By.XPATH,"//h1[normalize-space()='Welcome to Citrix Workspace app']").is_displayed()
time.sleep(10)
driver.find_element(By.XPATH,"//a[normalize-space()='Detect Citrix Workspace app']").click()
time.sleep(5)
pyautogui.press("tab")
time.sleep(5)
pyautogui.press("enter")
driver.find_element(By.XPATH,"//a[@id='protocolhandler-detect-alreadyInstalledLink']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("administrator@mypoc.local")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Test@123")
time.sleep(3)
driver.find_element(By.XPATH,"//a[@id='loginBtn']").click()
time.sleep(3)
ele=driver.find_element(By.XPATH,"//p[normalize-space()='Win2k19']").click()
time.sleep(3)
print(ele.text)
driver.find_element(By.XPATH,"//div[@class='theme-highlight-color appDetails-actions-text'][normalize-space()='Open']").click()
time.sleep(3)
# driver.get("chrome://downloads/")
# time.sleep(3)
download_dir = "/home/sysadmin/Downloads"
files = [f for f in os.listdir(download_dir) if f.endswith('.ica')]
paths = [os.path.join(download_dir, basename) for basename in files]
latest_file = max(paths, key=os.path.getctime)
# print(latest_file)
subprocess.call(('open', latest_file))
time.sleep(10)