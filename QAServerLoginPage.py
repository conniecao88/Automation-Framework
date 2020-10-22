from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class QAHubLogIn():

    #class driver
    def __init__(self,driver):
        self.driver = driver
        #Email CSS
        self.email_id = (By.CSS_SELECTOR, "#sso-cust-email")
        #New Email CSS
        self.email_id2 = (By.CSS_SELECTOR,"#Entity_EOEmpMain_Field_email")
        #Password CSS
        self.email_pwd = (By.CSS_SELECTOR, "#sso-cust-pwd")
        #New Password CSS
        self.email_pwd2 = (By.CSS_SELECTOR, "#Entity_EOEmpMain_Field_PASSWORD")
        #CSS Login Button
        self.sub_but = (By.CSS_SELECTOR, "button[class='btn btn-success btn-block ng-scope']")
        #New CSS Login Button
        self.sub_but2 = (By.CSS_SELECTOR, "#button-content")
        #Checkbox CSS
        self.rem_check = (By.CSS_SELECTOR, "#rememberMe")
        #New Checkbox_CSS
        self.rem_check2 = (By.CSS_SELECTOR, "#id")
        #Forgot Password CS
        self.forgot_pwd = (By.CSS_SELECTOR, "#forgotPwd")
        #SAML Link Text
        self.saml_log = (By.LINK_TEXT, "SAML Login")
        #User Login Link Text
        self.saml_to_user = (By.LINK_TEXT, "User Login")
        #Register CSS
        self.register_now = (By.CSS_SELECTOR, "#registerNow")
        #We can help LINK Text
        self.trouble = (By.LINK_TEXT, "We can help!")
        #CSS Selector for Incorrect Login Warning
        self.login_fail = (By.CSS_SELECTOR, "#ui_notifIt")
        #CSS Selector for Incorrect Email ID
        self.incorrect_email = (By.CSS_SELECTOR, "div[class='sso-cust-emailpop alert alert-danger padding-5 closeField col-md-10 col-sm-10 col-xs-10']")
        #CSS Selector for Incorrect Password
        self.incorrect_password = (By.CSS_SELECTOR, "div[class='sso-cust-pwdpop alert alert-danger padding-5 closeField col-md-10 col-sm-10 col-xs-10']")

        #CSS Selector for Forgot Password Reset Box
        self.reset_forgot_password = (By.CSS_SELECTOR, "#sso-cust-frgt-pwd")

        #CSS Selector for SAML Login Box
        self.saml_login_textbox = (By.CSS_SELECTOR, "#sso-cust-samlUserID")


    #Email textbox
    def email_textbox(self,hubworks_email):
        self.driver.find_element(*self.email_id).clear()
        self.driver.find_element(*self.email_id).send_keys(hubworks_email)

    def email_textbox2(self, hubworks_email):
        self.driver.find_element(*self.email_id2).clear()
        self.driver.find_element(*self.email_id2).send_keys(hubworks_email)

    #Password Textbox
    def password_textbox(self, hubworks_password):
        self.driver.find_element(*self.email_pwd).clear()
        self.driver.find_element(*self.email_pwd).send_keys(hubworks_password)

    def password_textbox2(self, hubworks_password):
        self.driver.find_element(*self.email_pwd2).clear()
        self.driver.find_element(*self.email_pwd2).send_keys(hubworks_password)

    #submit button
    def submit_button(self):
        self.driver.find_element(*self.sub_but).click()

    def submit_button2(self):
        self.driver.find_element(*self.sub_but2).click()

    #Remember Me Checkbox
    def remember_checkbox(self):
        self.driver.find_element(*self.rem_check).click()

    def remember_checkbox2(self):
        self.driver.find_element(*self.rem_check2).click()

    #Forgot Password Screen
    def forgot_hubworks_pwd(self):
        self.driver.find_element(*self.forgot_pwd).click()

    #SAML Login Screen
    def saml_login(self):
        self.driver.find_element(*self.saml_log).click()

    #User Login Button to Switch back after SAML
    def switch_saml_to_user(self):
        self.driver.find_element(*self.saml_to_user).click()

    #Register Button Screen
    def register_now(self):
        self.driver.find_element(*self.register_now).click()

    #Help Button Screen
    def help_button(self):
        self.driver.find_element(*self.trouble).click()


# Results Screen

    def log_warning(self):
        return self.driver.find_element(*self.login_fail)

    def log_warning_text(self):
        return self.driver.find_element(*self.login_fail).text

    def incorrect_email_warning(self):
        return self.driver.find_element(*self.incorrect_email)

    def incorrect_email_warning_text(self):
        return self.driver.find_element(*self.incorrect_email).text

    def wrong_password(self):
        return self.driver.find_element(*self.incorrect_password)

    def wrong_password_text(self):
        return self.driver.find_element(*self.incorrect_password).text

    def remember_me_checkbox(self):
        return self.driver.find_element(*self.rem_check)

    def forgot_pwd_reset(self):
        return self.driver.find_element(*self.reset_forgot_password)

    def saml_id_textbox(self):
        return self.driver.find_element(*self.saml_login_textbox)

    def email_box(self):
        return self.driver.find_element(*self.email_id)

   # def wait_loader(self):
       # return self.driver.find_element(*self.loader)

   # def click_profile(self):
       # return self.driver.find_element(*self.drop_down_profile)

    #def actual_click_profile(self):
       # return self.driver.find_element(*self.drop_down_profile).click()

   # def click_profile_logout(self):
      #  return self.driver.find_element(*self.profile_logout).click()