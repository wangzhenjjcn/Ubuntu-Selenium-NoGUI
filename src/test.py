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
import unittest
import app
import page



class MadeInChinaSearch(unittest.TestCase):

    def setUp(self):
        self.driver=driver = webdriver.Chrome(chrome_options=app.getChromeOptions(),executable_path=app.getDriver())
        self.driver.get("https://www.made-in-china.com/")


    def test_search_made_in_china(self):
        mainPage=page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "suzhou"
        mainPage.click_search_button()
        search_result_page=page.SearchResultsPage(self.driver)
        assert search_result_page.is_resaults_found()



    def test_search2_made_in_china(self):
        mainPage=page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "suz5646546hou"
        mainPage.click_search_button()
        search_result_page=page.SearchResultsPage(self.driver)
        assert search_result_page.is_resaults_found()


    def tearDown(self):
        self.driver.close()



if __name__ =="__main__":
    unittest.main()