import os
import sys
import json
import time
import threading
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



def getPath():
    path=os.path.dirname(os.path.realpath(sys.argv[0]))
    return path

def getDriver():
    # sysdir=os.path.dirname(os.path.realpath(sys.argv[0]))
    driver=getPath()+"/chromedriver.exe"
    return driver

def abs_url(orgUrl,path):
    URI=orgUrl
    if str(path).startswith("/"):
        return URI+path
    return orgUrl+path
    pass

def getUserDir():
    path=getPath()+"/data/userdata/"
    return path

def getChromeOptions():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--user-data-dir='+getUserDir())
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--enable-javascript')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-popup-blocking')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    return chrome_options

def initDriver():
    driver =None
    try:
        driver = webdriver.Chrome(chrome_options=getChromeOptions(),executable_path=getDriver())
        driver.set_page_load_timeout(5000) 
        driver.get("chrome://version/")
        return driver
    except Exception as e:
        if 'already in use' in str(e):
            print(str(e))
        print(e)
    return driver

def sysCmd(commander):
    print(commander)
    pass

def getActions(driver):
    return ActionChains(driver)

def clickId(driver,id):
    try:
        driver.implicitly_wait(5)
        web_id=driver.find_element_by_id(id)
        if web_id:
            actions=getActions(driver)
            actions.click(web_id)
            actions.perform()
    except Exception as e:
        print(e)
    pass


def test():
    print(getDriver())
    try:
        driver=initDriver()
        driver.get("https://www.made-in-china.com/")
    except Exception as e:
        print(e)
    pass


if __name__ == "__main__":
    try:
        test()
        time.sleep(1780)
    except Exception as e:
        print(e)
    pass