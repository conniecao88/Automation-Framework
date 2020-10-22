from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class ZipInventoryCredit():
    def __init__(self, driver):
        self.driver = driver
        self.loader = (By.CSS_SELECTOR, "div[id='loader']")
        self.credit_left = (By.CSS_SELECTOR, "#Menu_Inventory_creditMemo")
        self.add_credit = (By.CSS_SELECTOR, "button[class='btn rounded_blue_btn ng-binding ng-scope']")
        self.add_credit_screen = (By.CSS_SELECTOR, "div[class='modal-dialog  modal-top-margin  ng-scope']")
        self.supplier_drop = (By.CSS_SELECTOR, "div[id^='s2id_autogen']")
        self.suppliers = (By.CSS_SELECTOR, "ul[class='select2-results']")
        self.supplier_children = (By.TAG_NAME, "li")
        self.supplier_select = (By.CSS_SELECTOR, "ul[class='select2-results'] li:nth-of-type(2)")
        self.date_click = (By.CSS_SELECTOR, "div[class='input-group input-group-l-span col-md-12']")
        self.current_date = (By.CSS_SELECTOR, "button[class='btn cutomiseBtn btn-info currentdate']")
        self.calendar_information = (By.CSS_SELECTOR, "input[class^='form-control cursor-auto bg-white']")
        self.ok_button = (By.CSS_SELECTOR, "button[class='btn rounded_green_btn padding-left-20 pull-right padding-right-20']")
        self.manual_message = (By.CSS_SELECTOR, "div[id='ui_notifIt']")
        self.close_button = (By.CSS_SELECTOR, "button[class='btn-sm btn rounded_red_btn padding-left-15 padding-right-15 margin-left-7 ng-binding']")
        self.save_button = (By.CSS_SELECTOR, "button[class='btn btn-sm rounded_green_btn margin-left-7  ng-binding ng-scope']")
        self.finalize_button = (By.CSS_SELECTOR, "button[class='btn btn-sm rounded_blue_btn  ng-binding ng-scope']")
        self.credit_note = (By.CSS_SELECTOR, "input[class^='form-control font-13']")
        self.order_note = (By.CSS_SELECTOR, "div[class='row margin-bottom-10'] div[class='col-md-7'] input[class^='form-control']")
        self.invoice_number = (By.CSS_SELECTOR, "div[class='col-md-4 no-padding'] div[class='col-md-8'] div[class='row margin-bottom-10'] input[class^='form-control']")
        self.authorization_number = (By.CSS_SELECTOR, "div[class='col-md-4 no-padding'] div[class='col-md-8'] div[class='row'] input[class^='form-control']")
        self.item_drop = (By.CSS_SELECTOR, ".select2-choice")
        self.item_drop_list = (By.CSS_SELECTOR, ".select2-results")
        self.item_drop_child = (By.CSS_SELECTOR,"ul[class='select2-results'] li:nth-of-type(2)")
        self.item_drop_childs = (By.TAG_NAME, "li")

        self.received_quantity = (By.CSS_SELECTOR, "input[class^='received_qty form-control']")
        self.total_credit_amount = (By.CSS_SELECTOR, "span[class='margin-left-10 ng-binding']")
        self.credit_amount = (By.CSS_SELECTOR, "input[class^='form-control font-13 text-right']")

        self.item_trashcan = (By.CSS_SELECTOR, "div[class='text-center']")
        self.click_created_memo = (By.XPATH, "//table[@class='table table-hover table-striped table-bordered table-fixed no-margin']//tr[1]//td[7]//img[1]")
        self.delete_memo_trashcan = (By.XPATH,"//table[@class='table table-hover table-striped table-bordered table-fixed no-margin']//tr[1]//td[7]//img[2]")

        self.visible_text_page = (By.TAG_NAME, "body")



    def list_suppliers(self):
        list_sup = self.driver.find_element(*self.suppliers)
        return list_sup.find_elements(*self.supplier_children)

    def suppliers_box(self):
        return self.driver.find_element(*self.supplier_drop).text

    def date_box(self):
        return self.driver.find_element(*self.calendar_information).get_attribute("value")

    def man_message(self):
        return self.driver.find_element(*self.manual_message).text

    def type_credit(self,note):
        self.driver.find_element(*self.credit_note).clear()
        self.driver.find_element(*self.credit_note).send_keys(note)

    def credit_note_box(self):
        return self.driver.find_element(*self.credit_note).get_attribute("value")

    def type_order(self,order):
        self.driver.find_element(*self.order_note).clear()
        self.driver.find_element(*self.order_note).send_keys(order)

    def order_note_box(self):
        return self.driver.find_element(*self.order_note).get_attribute("value")

    def type_invoice(self, invoice):
        self.driver.find_element(*self.invoice_number).clear()
        self.driver.find_element(*self.invoice_number).send_keys(invoice)

    def invoice_box(self):
        return self.driver.find_element(*self.invoice_number).get_attribute("value")

    def type_authorization(self, authorization):
        self.driver.find_element(*self.authorization_number).clear()
        self.driver.find_element(*self.authorization_number).send_keys(authorization)

    def authorization_box(self):
        return self.driver.find_element(*self.authorization_number).get_attribute("value")

    def type_quantity(self,quantity):
        self.driver.find_element(*self.received_quantity).clear()
        self.driver.find_element(*self.received_quantity).send_keys(quantity)

    def type_quantity_enter(self,amount):
        self.driver.find_element(*self.received_quantity).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.received_quantity).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.received_quantity).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.received_quantity).send_keys(amount)
        self.driver.find_element(*self.credit_note).click()

    def received_box(self):
        return self.driver.find_element(*self.received_quantity).get_attribute("value")

    def credit_amount_box(self):
        return self.driver.find_element(*self.credit_amount).get_attribute("value")

    def total_credit_amount_box(self):
        return self.driver.find_element(*self.total_credit_amount).text

    def type_credit_amount(self,credit):
        self.driver.find_element(*self.credit_amount).clear()
        self.driver.find_element(*self.credit_amount).send_keys(credit)

    def type_credit_enter(self, amount):
        self.driver.find_element(*self.credit_amount).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.credit_amount).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.credit_amount).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.credit_amount).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.credit_amount).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.credit_amount).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.credit_amount).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.credit_amount).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.credit_amount).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.credit_amount).send_keys(amount)
        self.driver.find_element(*self.credit_note).click()

    #def click_created(self):
      #  return self.driver.find_element(*self.click_created_memo)

   # def memo_trashcan(self):
      #  return self.driver.find_element(*self.delete_memo_trashcan)




