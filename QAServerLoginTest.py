import unittest
from Pages.QAServerPages.QAMainPages.QAServerLoginPage import QAHubLogIn
from UData.ExcelFiles import GetData
from BasePages.Base import BaseClassWaits
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class LogInForHubworks(unittest.TestCase):
    path = "/UData/QAData/QAServerLoginDataExcel.xlsx"

    def setUp(self):
        self.get_options = Options()
        self.get_options.add_argument("--headless")
        # This window size is for hovering as actions won't be performed if this window size isn't specified
        self.get_options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome("/Users/prodmgmt20/chromedriver",options=self.get_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.driver.get("https://qa24680.hubworks.com/hwsso/#/login/")

    def tearDown(self):
        self.driver.quit()

    #Test if you can successfully log in
    #Test multiple times with valid input (Capitalized emails and etc)
    #Emails are NOT case sensitive
    def test_success(self):
        file = GetData(self.path,"QALoginPass")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            log_success = QAHubLogIn(self.driver)
            log_success.email_textbox(file.read_data_string(rows, 1))
            log_success.password_textbox(file.read_data_string(rows, 2))
            log_success.submit_button()
            #Change this to an explicit wait later
            time.sleep(5)
            the_url = self.driver.current_url
            if "custLangPage" in the_url or "launch-app" in the_url:
                file.write_data(rows, 5, "Log in Successfully")
                file.write_data(rows, 6, "Pass")
            else:
                file.write_data(rows, 5, "Log in NOT successful")
                file.write_data(rows, 6, "Fail")
            #change this to an explicit wait later
            time.sleep(5)
            self.driver.get("https://qa24680.hubworks.com/hwsso/#/login/")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows, 6) == "Pass")

    #Test whether users cant log in with an incorrect email/password
    #Test multiple times with invalid input (Capitalized passwords etc)
    #Passwords are case sensitive
    def test_fail(self):
        file = GetData(self.path,"QALoginFail")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            log_fail = QAHubLogIn(self.driver)
            log_fail.email_textbox(file.read_data_string(rows, 1))
            log_fail.password_textbox(file.read_data_string(rows, 2))
            log_fail.submit_button()
            #Change this to an explicit wait later
            time.sleep(5)
            if self.driver.current_url == "https://qa24680.hubworks.com/hwsso/#/login/":
                file.write_data(rows, 5, "User cannot log in")
                file.write_data(rows, 6, "Pass")
            else:
                file.write_data(rows, 5, "User is able to log in")
                file.write_data(rows, 6, "Fail")
                self.driver.get("https://qa24680.hubworks.com/hwsso/#/login/")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows, 6) == "Pass")

    #Test whether the correct warning appears when a user logins with a valid email and invalid password
    #There should only be ONE data set, if you want to include more data sets, you gotta add a wait option until
    #the error disappears before re-trying the data
    def test_warning_login(self):
        file = GetData(self.path,"QALoginWarning")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            login_warning = QAHubLogIn(self.driver)
            login_warning.email_textbox(file.read_data_string(rows,1))
            login_warning.password_textbox(file.read_data_string(rows,2))
            login_warning.submit_button()
            expected_results = file.read_data_string(rows,4)
            try:
                use_base = BaseClassWaits(self.driver)
                use_base.visible_elements(login_warning.log_warning())
                file.write_data(rows, 5, login_warning.log_warning_text())
                if expected_results == login_warning.log_warning_text():
                    file.write_data(rows,6, "Pass")
                else:
                    file.write_data(rows,6, "Fail")
            except:
                file.write_data(rows,5,"No Warning Message")
                file.write_data(rows, 6, "Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows,6) == "Pass")

    #Test whether the correct warning appears when a user enters an invalid email
    def test_email_warning(self):
        file = GetData(self.path,"QAEmailWarning")
        total_rows = file.get_rows()
        check_email_warning = QAHubLogIn(self.driver)
        check_email_warning.submit_button()
        for rows in range(2, total_rows+1):
            check_email_warning.email_textbox(file.read_data_string(rows,1))
            check_email_warning.password_textbox(file.read_data_string(rows,2))
            check_email_warning.submit_button()
            expected_results = file.read_data_string(rows, 3)
            try:
                use_base = BaseClassWaits(self.driver)
                use_base.visible_elements(check_email_warning.incorrect_email_warning())
                file.write_data(rows, 4, check_email_warning.incorrect_email_warning_text())
                if check_email_warning.incorrect_email_warning_text() == expected_results:
                    file.write_data(rows, 5, "Pass")
                else:
                    file.write_data(rows, 5, "Fail")
            except:
                file.write_data(rows, 4, "No warning message appeared")
                file.write_data(rows, 5, "Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows, 5) == "Pass")

    #Test whether the correct warning appears when a user does not enter a password
    #Test this with an account that is in multiple organizations ( Logout button is different based on how many organizations
    #user is in
    def test_password_warning(self):
        file = GetData(self.path,"QAPasswordWarning")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            check_password = QAHubLogIn(self.driver)
            check_password.email_textbox(file.read_data_string(rows,1))
            check_password.password_textbox(file.read_data_string(rows,2))
            #Fix this later, this is a bug you gotta type twice
            check_password.submit_button()
            check_password.submit_button()
            expected_results = file.read_data_string(rows,3)
            try:
                use_base = BaseClassWaits(self.driver)
                use_base.visible_elements(check_password.wrong_password())
                file.write_data(rows,4,check_password.wrong_password_text())
                if check_password.wrong_password_text() == expected_results:
                    file.write_data(rows,5, "Pass")
                else:
                    file.write_data(rows,5, "Fail")
            except:
                file.write_data(rows, 4, "No error message")
                file.write_data(rows, 5, "Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data(rows,5) == "Pass")


    #Test whether the Remember Me Button can be checked
    def test_remember(self):
        rem_box = QAHubLogIn(self.driver)
        rem_box.remember_checkbox()
        self.assertTrue(rem_box.remember_me_checkbox().is_selected())

    #Test whether the Remember me button works correctly
    #Should only include one data set, just did a for loop since i didn't want to hardcode the rows
    def test_remember_works(self):
        file = GetData(self.path,"QARememberMe")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            remember_works = QAHubLogIn(self.driver)
            remember_works.email_textbox(file.read_data_string(rows,1))
            remember_works.password_textbox(file.read_data_string(rows,2))
            remember_works.remember_checkbox()
            remember_works.submit_button()
            #change this to an explicit wait later
            time.sleep(5)
            self.driver.get("https://qa24680.hubworks.com/hwsso/#/login/")
            #CHange this to an explicit wait later
            time.sleep(5)
            if "custLangPage" in self.driver.current_url or "launch-app" in self.driver.current_url:
                file.write_data(rows,4, "User is not logged out after exiting screen")
                file.write_data(rows,5, "Pass")
            else:
                file.write_data(rows,4, "User is logged out")
                file.write_data(rows,5, "Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows, 5) == "Pass")

    #Test whether the Forgot Pwd Screen appears

    def test_forgot_pwd(self):
        password_forgot = QAHubLogIn(self.driver)
        password_forgot.forgot_hubworks_pwd()
        try:
            use_base = BaseClassWaits(self.driver)
            use_base.visible_elements(password_forgot.forgot_pwd_reset())
            the_test = "Pass"
        except:
            the_test = "Fail"
        self.assertTrue(the_test == "Pass")

     # Test whether the SAML Login Button works correctly

    def test_saml_login(self):
        saml_login = QAHubLogIn(self.driver)
        saml_login.saml_login()
        try:
            use_base = BaseClassWaits(self.driver)
            use_base.visible_elements(saml_login.saml_id_textbox())
            the_test = "Pass"
        except:
            the_test = "Fail"
        self.assertTrue(the_test == "Pass")

    # Test whether it can be switched back to user after clicking saml
    def test_saml_to_log(self):
        self.driver.get("https://sso.hubworks.com/hwsso/#/login/")
        saml_switch = QAHubLogIn(self.driver)
        saml_switch.saml_login()
        saml_switch.switch_saml_to_user()
        try:
            use_base = BaseClassWaits(self.driver)
            use_base.visible_elements(saml_switch.email_box())
            the_test = "Pass"
        except:
            the_test = "Fail"
        self.assertTrue(the_test == "Pass")

    #Test whether the We Can Help Button leads to another window
    def test_help(self):
        click_helpbutton = QAHubLogIn(self.driver)
        self.current_window = self.driver.window_handles[0]
        click_helpbutton.help_button()
        self.next_window = self.driver.window_handles[1]
        self.driver.switch_to.window(self.next_window)
        self.assertTrue(self.driver.current_url == "https://hubworks.com/contact-us.html")

if __name__ == "__main__":
    unittest.main()
