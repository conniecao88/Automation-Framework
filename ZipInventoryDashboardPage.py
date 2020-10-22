from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ZipInventoryDashboard():
    def __init__(self,driver):
        self.driver = driver
        #CSS_SELECTOR
        self.loader = (By.CSS_SELECTOR, "div[id='loader']")
        #CSS Selector for Left Menu
        self.menu_left = (By.CSS_SELECTOR, "ul[class='nav nav-pills nav-stacked ng-isolate-scope']")
        #Tag Name for Child Elements
        self.child_elements_of_menu = (By.TAG_NAME, "li")

        self.dash_board = (By.CSS_SELECTOR, "ul[class='nav nav-pills nav-stacked ng-isolate-scope'] li:nth-of-type(1)")

        self.dash_inventory_dollars = (By.CSS_SELECTOR, "div[class='tabbox inventory cursor-pointer'")

        self.dash_weekly_deliveries = (By.CSS_SELECTOR, "div[class='tabbox weekly_deliveries cursor-pointer'")

        self.dash_act_foodcost = (By.CSS_SELECTOR, "div[class='tabbox food_cost cursor-pointer']")

        self.dash_variance = (By.CSS_SELECTOR, "div[class='tabbox variance cursor-pointer'")

        self.visible_text_page = (By.TAG_NAME, "body")


    def visible_texts(self):
        return self.driver.find_element(*self.visible_text_page).text








    #Results

    #def click_dashboard(self):
       # drop_menu = self.driver.find_element(*self.menu_left)
       # dashboard = drop_menu.find_elements(*self.child_elements_of_menu)
        #return dashboard[0]






