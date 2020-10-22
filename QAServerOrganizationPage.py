from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class QAOrganizationKeys():

    def __init__(self,driver):
        self.driver = driver

        #CSS -> Image, for Adam's organization
        self.a_org = (By.CSS_SELECTOR, "div#app0 img")
        #CSS -> Image for Joe's organization
        self.j_org = (By.CSS_SELECTOR, "div#app1 img")
        #CSS -> Image for Kevin's Organization
        self.k_org = (By.CSS_SELECTOR, "div#app2 img")
        #CSS -> Image for Michael's Organization
        self.m_org = (By.CSS_SELECTOR, "div#app3 img")
        #CSS -> for Logout Button
        self.logg = (By.CSS_SELECTOR, "div[id='container'] [class = 'btn-header']")
        #CSS -> Flag Button
        self.flag = (By.CSS_SELECTOR, "div[id='container'] [class = 'dropdown no-padding margin-right-0 text-right']")
        #CSS Selector -> loader
        self.loader = (By.CSS_SELECTOR, "div[id='loader']")
        #CSS Selector -> Drop Down Menu
       # self.dropdown_profile = (By.CSS_SELECTOR, "div[id='content_wrapper'] [class='dropdown menu-merge nav-profile']")
        self.dropdown_profile = (By.CSS_SELECTOR, "[class='dropdown menu-merge nav-profile']")
        self.pop_up = (By.CSS_SELECTOR, "[class='onesignal-popover-container onesignal-reset slide-down']")
        self.pop_up_exit = (By.CSS_SELECTOR, "[class='align-right secondary popover-button']")

