import unittest
from BasePages.Base import BaseClass
from BasePages.Base import BaseClassWaits
from Pages.WebPages.HubworksSignUpPage import HubworksSignUpScreen
from UData.ExcelFiles import GetData


class TestHubworksSignUpPage(BaseClass):
    path = "/Users/prodmgmt20/PycharmProjects/Altametrics/UData/HubworksWebData/HubworksSignUpPageExcelData.xlsx"

    def setUp(self):
        self.driver.get("https://app001.hubworks.com/hwot001/#/hwSignup/0/eyJ0cmFja2VyUEsiOiIiLCJzZWFyY2hUZXJtIjoiIiwidXRtX3NvdXJjZSI6IiIsInNvdXJjZV9kZXRhaWwiOiIiLCJzYWxlc19jaGFubmVsX2lkIjoiIn0=")

    def tearDown(self):
        self.driver.get("https://hubworks.com/")

    #Validate whether what you type in name (test_name) appears in the text box
    def test_enter_name_success(self):
        file = GetData(self.path,"NameTextBox")
        total_rows = file.get_rows()
        for rows in range(2,total_rows+1):
            expected_results = file.read_data_string(rows,2)
            self.test_name = file.read_data_string(rows,1)
            name_success = HubworksSignUpScreen(self.driver)
            name_success.sign_up_name(self.test_name)
            file.write_data(rows,3,name_success.sign_up_name_results())
            if name_success.sign_up_name_results() == expected_results:1
                file.write_data(rows,4,"Pass")
            else:
                file.write_data(rows,4,"Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows,4) == "Pass")


    #Validate the warnings for Name
    def test_sign_name_box_warning(self):
        file = GetData(self.path,"NameTextBoxWarning")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            name_warning = HubworksSignUpScreen(self.driver)
            name_warning.sign_up_name(file.read_data_string(rows, 1))
            name_warning.email_name(file.read_data_string(rows, 2))
            name_warning.search_business_name(file.read_data_string(rows,3))
            name_warning.week_day_name(file.read_data_string(rows,4))
            name_warning.phone_number(file.read_data_string(rows, 5))
            name_warning.offer_code(file.read_data_string(rows, 6))
            name_warning.next_button_click()
            expected_results = file.read_data_string(rows, 7)
            file.write_data(rows,8, name_warning.name_warning_results())
            if name_warning.name_warning_results() == expected_results:
                file.write_data(rows, 9, "Pass")
            else:
                file.write_data(rows, 9, "Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows, 9) == "Pass")

    #Validate whether what you type in Email(testEmployee) appears in the text box
    def test_employee_box_success(self):
        file = GetData(self.path,"EmailTextBox")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data(rows,2)
            email_success = HubworksSignUpScreen(self.driver)
            email_success.email_name(file.read_data_string(rows, 1))
            file.write_data(rows, 3, email_success.email_name_results())
            if email_success.email_name_results() == expected_results:
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data_string(rows, 4) == "Pass")

    #Validate the warnings for Emails
    def test_for_email_warning(self):
        file = GetData(self.path,"EmailTextBoxWarning")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            the_email_warning = HubworksSignUpScreen(self.driver)
            the_email_warning.sign_up_name(file.read_data_string(rows, 1))
            the_email_warning.email_name(file.read_data_string(rows, 2))
            the_email_warning.search_business_name(file.read_data_string(rows,3))
            the_email_warning.week_day_name(file.read_data_string(rows, 4))
            the_email_warning.phone_number(file.read_data_string(rows, 5))
            the_email_warning.offer_code(file.read_data_string(rows, 6))
            the_email_warning.next_button_click()
            expected_results = file.read_data_string(rows, 7)
            file.write_data(rows, 8, the_email_warning.email_warning_results())
            if the_email_warning.email_warning_results() == expected_results:
                file.write_data(rows, 9, "Pass")
            else:
                file.write_data(rows, 9, "Fail")
        for rows in range (2, total_rows+1):
            self.assertTrue(file.read_data_string(rows, 9) == "Pass")

    def test_business_name_success(self):
        file = GetData(self.path,"BusinessTextBox")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            expected_results = file.read_data_string(rows, 2)
            bus_success = HubworksSignUpScreen(self.driver)
            bus_success.search_business_name(file.read_data_string(rows,1))
            file.write_data(rows,3,bus_success.business_name_results())
            if bus_success.business_name_results() == expected_results:
                file.write_data(rows,4,"Pass")
            else:
                file.write_data(rows,4, "Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows,4) == "Pass")

    def test_business_warning(self):
        file = GetData(self.path,"BusinessTextBoxWarning")
        total_rows = file.get_rows()
        for rows in range(2,total_rows+1):
            get_buswarning = HubworksSignUpScreen(self.driver)
            get_buswarning.sign_up_name(file.read_data_string(rows,1))
            get_buswarning.email_name(file.read_data_string(rows,2))
            get_buswarning.search_business_name(file.read_data_string(rows, 3))
            get_buswarning.week_day_name(file.read_data_string(rows, 4))
            get_buswarning.phone_number(file.read_data_string(rows, 5))
            get_buswarning.offer_code(file.read_data_string(rows, 6))
            get_buswarning.next_button_click()
            get_buswarning.next_button_click()
            expected_results = file.read_data_string(rows, 7)
            file.write_data(rows, 8, get_buswarning.business_warning_results())
            if get_buswarning.business_warning_results() == expected_results:
                file.write_data(rows, 9, "Pass")
            else:
                file.write_data(rows, 9, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data_string(rows, 9) == "Pass")

    #Validate whether when entering the week name, the week name appears
    def test_weekday_success(self):
        file = GetData(self.path,"WeekDayEnter")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            week_day = file.read_data_string(rows,1)
            week_day_enter = HubworksSignUpScreen(self.driver)
            week_day_enter.week_day_name(week_day)
            expected_results = file.read_data_string(rows, 2)
            file.write_data(rows,3,week_day_enter.weekday_name_results_select())
            if week_day_enter.weekday_name_results_select() == expected_results:
                file.write_data(rows,4,"Pass")
            else:
                file.write_data(rows,4,"Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows,4) == "Pass")

    #Iterate through the drop down menu
    def test_weekday_dropdown_select(self):
        file = GetData(self.path,"WeekDayDropDownMenu")
        total_rows = file.get_rows()
        row_start = 2
        for i in range(7):
            select_dropdown_menu = HubworksSignUpScreen(self.driver)
            week_days = select_dropdown_menu.weekday_dropdown_menu()
            week_days[i].click()
            week_day_selected = select_dropdown_menu.weekday_name_results_select()
            file.write_data(row_start, 3, week_day_selected)
            row_start = row_start + 1
        for rows in range(2, total_rows+1):
            expected_results = file.read_data_string(rows,3)
            if file.read_data(rows,3) == expected_results:
                file.write_data(rows,4,"Pass")
            else:
                file.write_data(rows,4,"Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows, 4) == "Pass")

    def test_phone_number_success(self):
        file = GetData(self.path,"PhoneNumberTextBox")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            expected_results = file.read_data_string(rows, 2)
            phone_entered = HubworksSignUpScreen(self.driver)
            phone_entered.phone_number(file.read_data_string(rows, 1))
            file.write_data(rows, 3, phone_entered.phone_num_results())
            if expected_results == phone_entered.phone_num_results():
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows, 4) == "Pass")

    def test_phone_number_warning(self):
        file = GetData(self.path,"PhoneNumberTextBoxWarning")
        total_rows = file.get_rows()
        for rows in range(2,total_rows+1):
            number_warning = HubworksSignUpScreen(self.driver)
            number_warning.sign_up_name(file.read_data_string(rows, 1))
            number_warning.email_name(file.read_data_string(rows, 2))
            number_warning.search_business_name(file.read_data_string(rows, 3))
            number_warning.week_day_name(file.read_data_string(rows, 4))
            number_warning.phone_number(file.read_data_string(rows, 5))
            number_warning.offer_code(file.read_data_string(rows, 6))
            number_warning.next_button_click()
            number_warning.next_button_click()
            expected_results = file.read_data_string(rows, 7)
            file.write_data(rows, 8, number_warning.phone_num_warning_results())
            if number_warning.phone_num_warning_results() == expected_results:
                file.write_data(rows, 9, "Pass")
            else:
                file.write_data(rows, 9, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data_string(rows, 9) == "Pass")

    def test_offer_code(self):
        file = GetData(self.path, "OfferCodeTextBox")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 2)
            code_entered = HubworksSignUpScreen(self.driver)
            code_entered.offer_code(file.read_data_string(rows, 1))
            file.write_data(rows, 3, code_entered.offer_results())
            if expected_results == code_entered.offer_results():
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data_string(rows, 4) == "Pass")


if __name__ == "__main__":
    unittest.main()


