from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Transfer_Page():
    def __init__(self,driver):
        self.driver = driver
        self.loader = (By.CSS_SELECTOR, "div[id='loader']")
        self.transfer_button = (By.CSS_SELECTOR, "ul[class='nav nav-pills nav-stacked ng-isolate-scope'] li:nth-of-type(4")
        self.add_transfer_out = (By.CSS_SELECTOR, "button[class='btn rounded_blue_btn white ng-binding ng-scope']")
        self.transfer_popup = (By.CSS_SELECTOR, "form[class='form-horizontal ng-valid ng-valid-date ng-valid-date-disabled ng-dirty ng-valid-parse']")
        self.site_drop = (By.CSS_SELECTOR, "div[id^='s2id_autogen']")
        self.sites = (By.CSS_SELECTOR, "ul[class='select2-results']")
        self.sites_children = (By.TAG_NAME, "li")
        self.site_site_chosen = (By.XPATH, "//ul[contains(@class,'select2-results')]//div[contains(.,'Site 2')]")
        self.add_button = (By.CSS_SELECTOR, "button[class='btn rounded_blue_btn white ng-binding']")
        self.transfer_in_tab = (By.XPATH,"//div[@class='col-md-4 col-md-offset-4']//span[2]")
        self.edit_transfer_in = (By.CSS_SELECTOR, "button[class='btn btn-link hover-pointer no-padding no-margin margin-right-5 ng-scope']")
        self.finalize_button = (By.CSS_SELECTOR,"button[title='finalize']")
        self.decline_button = (By.CSS_SELECTOR, "button[class='{'rounded_gray_btn': (eoTrfMain.status == 'Declined' && eoTrfMain.isPosted), 'rounded_gray_btn btn-sm': eoTrfMain.isPosted, 'rounded_gray_btn': eoTrfMain.status == 'Declined', 'rounded_red_btn':(!eoTrfMain.isPosted && eoTrfMain.status == 'Un-finalized')}']")
        self.close_button = (By.CSS_SELECTOR, "button[class='btn rounded_red_btn white ng-binding']")
        self.select_sites = (By.CSS_SELECTOR, "#app_sites")
        self.select_sites_child = (By.XPATH, "//ul[@class='site-listings no-margin pop-content ng-scope']//li[@class='ng-scope']//a[text()='Costa Mesa']")
        self.select_sites_child2 = (By.XPATH, "//ul[@class='site-listings no-margin pop-content ng-scope']//li[@class='ng-scope']//a[text()='Site 2']")
        self.type_item_add_in = (By.CSS_SELECTOR,"#charSerach")
        #Selecting Item to Transfer after typing it in
        self.select_item = (By.CSS_SELECTOR, "ul[class='typeahead dropdown-menu'] li:nth-of-type(1)")
       # self.add_unit_1 = (By.CSS_SELECTOR, "div[class='col-sm-5 no-padding ng-scope']")
        #Adding Unit (Number) for Transfers
        self.add_unit_1 = (By.CSS_SELECTOR, "input[class^='form-control text-right']")
        #Clicking on the Button Transfer Out
        self.transfer_out = (By.CSS_SELECTOR, "button[title='Transfer Out']")
      #  self.save_button = (By.CSS_SELECTOR, "button[class='btn margin-right-10 white ng-binding ng-scope rounded_green_btn']")
        self.visible_text_page = (By.TAG_NAME, "body")
        #Pop Up Message
        self.manual_message = (By.CSS_SELECTOR, "div[id='ui_notifIt']")

    def visible_texts(self):
        return self.driver.find_element(*self.visible_text_page).text




    def list_sites(self):
        list_sup = self.driver.find_element(*self.sites)
        return list_sup.find_elements(*self.sites_children)

    def site_box(self):
        return self.driver.find_element(*self.site_drop).text

    def switch_sites(self):
        return self.driver.find_element(*self.select_sites)

    def click_switched_site(self):
        return self.driver.find_element(*self.select_sites_child2)

    def type_item(self,item):
        self.driver.find_element(*self.type_item_add_in).clear()
        self.driver.find_element(*self.type_item_add_in).send_keys(item)
       # self.driver.find_element(*self.type_item_add_in).send_keys(Keys.RETURN)

    def select_items(self):
        self.driver.find_element(*self.select_item).click()

    def add_first_unit(self,count):
       # self.driver.find_element(*self.add_unit_1).clear()
        self.driver.find_element(*self.add_unit_1).send_keys(count)

