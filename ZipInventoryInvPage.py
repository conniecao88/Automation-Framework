from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Inv_Page():
    def __init__(self,driver):
        self.driver = driver
        self.loader = (By.CSS_SELECTOR, "div[id='loader']")
        self.add_inventory = (By.CSS_SELECTOR, "[class='btn margin-left-10 rounded_blue_btn white ng-binding ng-scope']")
        self.add_popup = (By.CSS_SELECTOR, "[class='form-horizontal ng-pristine ng-valid ng-valid-date ng-valid-date-disabled']")
        self.select_count_menu = (By.CSS_SELECTOR, "class['select2-choice']")

        self.visible_text_page = (By.TAG_NAME, "body")