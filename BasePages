import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains as AC
from Pages.QAServerPages.QAMainPages.QAServerLoginPage import QAHubLogIn
from Pages.QAServerPages.QAMainPages.QAServerOrganizationPage import QAOrganizationKeys

class BaseClassLoginOrgSaved(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        cls.get_options = Options()
        #cls.get_options.add_argument("--headless")
        cls.get_options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Chrome("/Users/prodmgmt20/chromedriver", options=cls.get_options)
        #cls.driver.maximize_window()
        cls.driver.get("https://qa24680.hubworks.com/hwsso/#/login/")
        cls.to_login = QAHubLogIn(cls.driver)
        cls.to_login.email_textbox("conniecao2@qa.com")
        cls.to_login.password_textbox("1234")
        cls.to_login.remember_checkbox()
        cls.to_login.submit_button()
        cls.to_org = QAOrganizationKeys(cls.driver)
        use_base = BaseClassWaits(cls.driver)
        #This is for Logins that have more than one organization
        #use_base.element_clickable(cls.to_org.a_org)
        #This is for logins that only have one organization
        use_base.invisible_element_located(cls.to_org.loader)
        use_base.element_clickable(cls.to_org.dropdown_profile)


    @classmethod
    def tearDownClass(cls):
        pass
        #cls.driver.quit()


class BaseClassWaits():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 150)

    def visible_elements(self,element):
        return self.wait.until(EC.visibility_of(element))

    def visible_elements_instant(self,element):
        self.wait = WebDriverWait(self.driver,5)
        return self.wait.until(EC.visibility_of(element))


    def visible_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def visible_element_instant(self,locator):
        self.wait = WebDriverWait(self.driver,5)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def invisible_element(self,element):
        return self.wait.until(EC.invisibility_of_element(element))

    def invisible_element_located(self,locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def element_clickable_instant(self,locator):
        self.wait = WebDriverWait(self.driver,10)
        return self.wait.until(EC.element_to_be_clickable(locator))

    def element_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    def element_to_be_clickable(self,element):
        self.wait.until(EC.element_to_be_clickable(element)).click()

    def hover_mouse(self,element,element2):
        self.actions = AC(self.driver)
        self.actions.move_to_element(element).move_to_element(element2).click().perform()

    def move_mouse_to_right(self):
        self.actions = AC(self.driver)
        self.actions.move_by_offset(10,0)
        self.actions.perform()

    def scroll_up(self):
        return self.driver.execute_script("window.scrollTo(0, 0)")




# Ignore

class BaseClass(unittest.TestCase):

    driver = None
    @classmethod
    def setUpClass(cls):
        cls.get_options = Options()
        #cls.get_options.add_argument("--headless")
        #This window size is for hovering as actions won't be performed if this window size isn't specified
        #cls.get_options.add_argument("window-size=1920,1080")
        cls.driver = webdriver.Chrome("/Users/prodmgmt20/chromedriver")#, options=cls.get_options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(60)

    @classmethod
    def tearDownCls(cls):
        cls.driver.quit()


class BaseClassLoginSaved(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        cls.get_options = Options()
        #cls.get_options.add_argument("--headless")
        #cls.get_options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Chrome("/Users/prodmgmt20/chromedriver")#, options=cls.get_options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(120)
        cls.driver.get("https://qa24680.hubworks.com/hwsso/#/login/")
        cls.to_login = QAHubLogIn(cls.driver)
        cls.to_login.email_textbox("ccao@altametrics.com")
        cls.to_login.password_textbox("1234")
        cls.to_login.remember_checkbox()
        cls.to_login.submit_button()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



class newBaseLogin(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        cls.get_options = Options()
        #cls.get_options.add_argument("--headless")
        cls.get_options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Chrome("/Users/prodmgmt20/chromedriver", options=cls.get_options)
        #cls.driver.maximize_window()
        cls.driver.get("https://qa24680.hubworks.com/hwapp/hwHaccp/#/login")
        cls.to_login = QAHubLogIn(cls.driver)
        cls.to_login.email_textbox2("conniecao@qa.com")
        cls.to_login.password_textbox2("1234")
        cls.to_login.remember_checkbox2()
        cls.to_login.submit_button2()
        cls.to_org = QAOrganizationKeys(cls.driver)
        use_base = BaseClassWaits(cls.driver)
        use_base.invisible_element_located(cls.to_org.loader)
        use_base.element_clickable(cls.to_org.dropdown_profile)



      #  if use_base.visible_element(cls.to_org.pop_up):
           # use_base.element_clickable(cls.to_org.pop_up_exit)
          #  use_base.element_clickable(cls.to_org.dropdown_profile)
       # else:
           # use_base.element_clickable(cls.to_org.dropdown_profile)

    

