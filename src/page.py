from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "word"

class SearchButtonElement(BasePageElement):
    locator = "word"
    


class BasePage(object):
    def __init__(self,driver):
        self.driver=driver



class MainPage(BasePage):

    search_text_element=SearchButtonElement()

    def is_title_matches(self):
        return "Made-in-China.com" in self.driver.title

    def click_search_button(self):
        element=self.driver.find_element(*MainPageLocators().Search_Button)
        element.click()

class SearchResultsPage(BasePage):
    def is_resaults_found(self):
        return "No matches were found" not in self.driver.page_source