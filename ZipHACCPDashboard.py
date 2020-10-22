from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from BasePages.Base import BaseClassWaits

class HACCP_Dashboard():
    def __init__(self, driver):
        self.driver = driver

        self.use_base = BaseClassWaits(self.driver)

        self.loader = (By.CSS_SELECTOR, "div[class='loader-container']")

        #Click on Dashboard
        self.dashboard = (By.CSS_SELECTOR,"#Menu_Hw_Haccp_Dashboard")

        #What is visible on the Page
        self.visible_text_page = (By.TAG_NAME, "body")

        #What is visible on the Dashboard Page
        self.test_text = (By.CSS_SELECTOR, "div[class='hw-box-content']")

        #What is visible on the Dashboard Page
        self.test_text2 = (By.CSS_SELECTOR,"div[class^='dashboard-header-wrap-title']")


        #Click on Ongoing Checklist
        self.ongoing_checklist = (By.CSS_SELECTOR, "#Menu_Hw_Haccp_Checklist")

        #Completed Checklist Value
        self.completed_checklist_values = (By.CSS_SELECTOR, "span[class='font-weight-bold mr-2 font-16']")
       # self.completed_checklist_values = (By.CSS_SELECTOR,"span[class='font-weight-bold mr-2 font-18']")

        #When there are no Dashboard Tasks for Previous Week
        self.dashboard_comp_no_percent = (By.XPATH, "//div[@class='hw-content']//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[2]//div[@class='no_data_display']//span")

        #Dashboard Completed Percentage for Previous week
        self.dashboard_comp_previous_percent = (By.XPATH,"//div[@class='hw-content']//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[2]//*[name() ='svg']//*[name() = 'text']//*[name()='tspan']")

        #Dashboard Completed Percentage for Current Week
        self.dashboard_comp_percent = (By.XPATH, "//div[@class='hw-content']//div[1]//div[1]//div[1]//div[2]//div[1]//div[2]//div[2]//*[name() ='svg']//*[name() = 'text']//*[name()='tspan']")


        #Dashboard Escalated Value
        self.dashboard_escalated_value = (By.XPATH, "//div[@class='row']//div[1]//*[@class='dashboard-header-wrap']//*[@class='right-icon']")

        #Dashboard Escalated Percentage for Previous Week
        self.dashboard_escalated_previous_percent = (By.XPATH, "//div[@class='hw-content']//div[1]//div[2]//div[1]//div[2]//div[1]//div[1]//div[2]//*[name() ='svg']//*[name() = 'text']//*[name()='tspan']")

        #Dashboard Escalated Percentage for Current Week
        self.dashboard_escalated_percent = (By.XPATH, "//div[@class='hw-content']//div[1]//div[2]//div[1]//div[2]//div[1]//div[2]//div[2]//*[name() ='svg']//*[name() = 'text']//*[name()='tspan']")


        self.comments = (By.XPATH, "//span[contains(@title, 'Comments')]")

        #Grab all the temperature tasks
        self.temp_tasks = (By.CSS_SELECTOR, "div[class='input-group']")
       # self.temp_tasks = (By.XPATH, "//span[contains(@title, 'C')]")
        #self.temp_tasks = (By.XPATH, "//span[text() = '° C']")

        #Grab all the esc tasks
        self.esc_tasks = (By.XPATH, "//span[contains(@title,'Escalated Task')]")

        #Dashboard Exceptions
        #self.dashboard_exceptions_tasks = (By.XPATH, "//div[@class='row']//div[2]//*[@class='dashboard-header-wrap']//*[@class='right-icon']")
        self.dashboard_exceptions_tasks = (By.XPATH, "//div[@class='hw-content']//div[2]//div[2]//div[@class='dashboard-header-wrap']//div[@class='right-icon']//span")


        #Dashboard Exception Percentage for Previous Week
        self.dashboard_exception_previous_percent = (By.XPATH,"//div[@class='hw-content']//div[1]//div[3]//div[1]//div[2]//div[1]//div[1]//div[2]//*[name() ='svg']//*[name() = 'text']//*[name()='tspan']")

        #Dashboard Exception Percentage for Current Week
        self.dashboard_exception_percent = (By.XPATH, "//div[@class='hw-content']//div[1]//div[3]//div[1]//div[2]//div[1]//div[2]//div[2]//*[name() ='svg']//*[name() = 'text']//*[name()='tspan']")

        #Dashboard when there are no temperature tasks for Current Week
       # self.dashboard_exception_no_data = (By.XPATH,"//div[@class='no_data_display']//span")
        self.dashboard_exception_no_data = (By.XPATH, "//div[@class='hw-content']//div[1]//div[3]//div[1]//div[2]//div[1]//div[2]//div[2]//div[@class='no_data_display']//span")

        #Dashboard when there are no temperature tasks for Previous Week
        self.dashboard_exception_no_data_1 = (By.XPATH, "//div[@class='hw-content']//div[1]//div[3]//div[1]//div[2]//div[1]//div[1]//div[2]//div[@class='no_data_display']//span")

        #Return when there are no Escalated tasks for Current Week
       # self.dashboard_exception_no_esc_data = (By.XPATH, "//div[@class='hw-content']//div[1]//div[2]//div[1]//div[2]//div[1]//div[2]//div[2]//div[@class='no_data_display']//span")

        # Return when there are no Escalated tasks for Previous week
        self.dashboard_exception_no_esc_data_1 = (By.XPATH, "//div[@class='hw-content']//div[1]//div[2]//div[1]//div[2]//div[1]//div[1]//div[2]//div[@class='no_data_display']//span")

        #Escalated Task Icon on Ongoing Checklist
        self.escalated_icon = (By.XPATH, "//span[contains(@title,'Escalated Task')]")

        #Completed on Historical Checklist
        self.completed_icon = (By.XPATH, "//span[contains(@title, 'Completed')]")

        #Ongoing Checklists List
       # self.total_checklists = (By.CSS_SELECTOR, "div[class='col-12 fn-select-append']")

        #Expand the Ongoing Checklist
       # self.list_checklists = (By.CSS_SELECTOR,".accordian-panel-wrapper")

        # Historical Checklists List
        self.total_checklists = (By.CSS_SELECTOR, "div[class='hw-box-content']")

        #Expand the Historical Checklists
        self.list_checklists = (By.CSS_SELECTOR, "i[class='fn-global-expand fn-panel_icon']")

        #Return Weekly Checklist
        self.list_checklists_weekly = (By.CSS_SELECTOR, "div[class='weekly']")


        #Today's Checklist
        self.today_checklist = (By.CSS_SELECTOR, "span[class='d-inline-block align-middle']")

        #Historica Checklist
        self.historical_checklist = (By.CSS_SELECTOR, "#Menu_Hw_Haccp_Historical")

        #Click left on calendar
        self.back_calendar = (By.CSS_SELECTOR, "i[class='fa fa-angle-left fa-fw']")

        #Click Expand
       # self.click_expand = (By.CSS_SELECTOR, "i[class='fn-global-expand fn-panel_icon']")

        #Click on Select An Option Drop Down
        self.select_option = (By.CSS_SELECTOR, "div[class='ng-value-container']")
        #self.select_option = (By.CSS_SELECTOR, "div[class='ng-dropdown-panel-items scroll-host']")

        #Click on Weekly Tasks
        self.select_weekly_tasks = (By.XPATH, "//span[text()='All Weekly Tasks for:']")






    #Return all the Visible Texts in Body
    def visible_texts(self):
        return self.driver.find_element(*self.visible_text_page).text

    #Return visible texts in Dashboard (Headers only)
    def test_texts(self):
        the_text = self.driver.find_element(*self.test_text)
        return the_text.find_elements(*self.test_text2)

    #Return the checklist value
    def return_comp_checklists(self):
        return self.driver.find_element(*self.completed_checklist_values).text

    #Return "No Tasks" as there are no tasks for the previous week
    def return_comp_no_data(self):
        return self.driver.find_element(*self.dashboard_comp_no_percent).text

    #Return the percentage for Previous Week Tasks
    def return_comp_previous_percentage(self):
        return self.driver.find_element(*self.dashboard_comp_previous_percent).text

    #Return the percentage for Current Week Tasks
    def return_comp_percentage(self):
        return self.driver.find_element(*self.dashboard_comp_percent).text

    #Return the Escalated Value on the Dashboard
    def return_escalated_value(self):
        return self.driver.find_element(*self.dashboard_escalated_value).text

    #Return the percentage for the Previous Escalated Week
    def return_escalated_previous_percentage(self):
        return self.driver.find_element(*self.dashboard_escalated_previous_percent).text

    #Return the percentage for the Current Escalated Week
    def return_escalated_percentage(self):
        return self.driver.find_element(*self.dashboard_escalated_percent).text

    def return_total_tasks(self):
        return self.driver.find_elements(*self.comments)

    def return_esc_tasks(self):
        return self.driver.find_elements(*self.esc_tasks)

    def return_completed_tasks(self):
        return self.driver.find_elements(*self.completed_icon)

    def return_temp_tasks(self):
        return self.driver.find_elements(*self.temp_tasks)

    def return_exception_value(self):
        return self.driver.find_element(*self.dashboard_exceptions_tasks).text

    def return_exception_previous_percentage(self):
        return self.driver.find_element(*self.dashboard_exception_previous_percent).text

    def return_exception_percentage(self):
        return self.driver.find_element(*self.dashboard_exception_percent).text

    def return_exception_no_data(self):
        return self.driver.find_element(*self.dashboard_exception_no_data).text

    def return_exception_no_data_1(self):
        return self.driver.find_element(*self.dashboard_exception_no_data_1).text

   # def return_exception_no_data_escalation(self):
     #   return self.driver.find_element(*self.dashboard_exception_no_esc_data).text

    def return_exception_no_data_escalation_1(self):
        return self.driver.find_element(*self.dashboard_exception_no_esc_data_1).text

    def the_escalated_icon(self):
        return self.driver.find_element(*self.escalated_icon)

    def return_expand(self):
        page_checklist = self.driver.find_element(*self.total_checklists)
        return page_checklist.find_elements(*self.list_checklists)

    def return_expand_weekly(self):
        weekly_page_checklist = self.driver.find_element(*self.total_checklists)
        return weekly_page_checklist.find_elements(*self.list_checklists_weekly)

    def return_select_options_element(self):
        return self.driver.find_element(*self.select_option)

    def return_weekly_options_element(self):
        return self.driver.find_element(*self.select_weekly_tasks)


    ######  METHODS
    def wait_for_loader(self):
        self.use_base.invisible_element_located((self.loader))

    def click_on_dashboard(self):
        self.use_base.invisible_element_located((self.loader))
        self.use_base.element_clickable((self.dashboard))
        self.use_base.invisible_element_located((self.loader))

    def click_on_historial_checklist(self):
        self.use_base.invisible_element_located((self.loader))
        self.use_base.element_clickable((self.historical_checklist))
        self.use_base.invisible_element_located((self.loader))


    def click_on_back_calendar(self):
        self.use_base.invisible_element_located((self.loader))
        self.use_base.element_clickable((self.back_calendar))
        self.use_base.invisible_element_located((self.loader))


    def click_on_weekly_tasks(self):
        self.use_base.invisible_element_located((self.loader))
        self.use_base.move_mouse_to_right()
       # self.use_base.hover_mouse(self.return_select_options_element(),self.return_weekly_options_element())
        self.use_base.element_clickable((self.select_option))
        self.use_base.element_clickable(((self.select_weekly_tasks)))
        self.use_base.invisible_element_located((self.loader))


    def scroll_up_page(self):
        self.use_base.scroll_up()

    #Click on Dashboard and wait for the percentages to load
    def wait_for_percentages_load(self):
        self.use_base.invisible_element_located((self.loader))
        self.use_base.element_clickable((self.dashboard))
        self.use_base.visible_element((self.dashboard_comp_percent))
















