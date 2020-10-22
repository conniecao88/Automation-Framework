from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HACCP_Ongoing_Checklist():
    def __init__(self,driver):
        self.driver = driver

        #Loader
        self.loader = (By.CSS_SELECTOR, "div[class='loader-container']")

        # Click on Dashboard
        self.dashboard = (By.CSS_SELECTOR, "#Menu_Hw_Haccp_Dashboard")

        # Click on Ongoing Checklist
        self.ongoing_checklist = (By.CSS_SELECTOR, "#Menu_Hw_Haccp_Checklist")

        # Ongoing Checklists List
        self.total_checklists = (By.CSS_SELECTOR, "div[class='col-12 fn-select-append']")

        # Each Individual Checklist on the Ongoing Checklist
        self.list_checklists = (By.CSS_SELECTOR,"zchk-setup-panel[class='accordian-panel-wrapper'] div[class='d-inline-block align-middle mr-2 text-left text-truncate']")



    def return_checklist_names(self):
        total_checklists = self.driver.find_element(*self.total_checklists)
        return total_checklists.find_elements(*self.list_checklists)


