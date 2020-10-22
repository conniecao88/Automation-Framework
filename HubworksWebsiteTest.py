from BasePages.Base import BaseClass
from Pages.WebPages.HubworksHomePage import HubworksHome
from selenium.webdriver.chrome.options import Options


class TestHomePage(BaseClass):

    def setUp(self):
        self.driver.get("https://hubworks.com/")

    def tearDown(self):
        pass

    #Test the App Store Button
    def testAppStore(self):
        iApp = HubworksHome(self.driver)
        iApp.appStoreButton()
        self.assertTrue(self.driver.current_url == iApp.appStoreButtonScreen())

    #Test the Integration Button
    def testIntegration(self):
        iIntegrate = HubworksHome(self.driver)
        iIntegrate.IntegrationsButton()
        self.assertTrue(self.driver.current_url == iIntegrate.IntegrationsButtonScreen())

    def testLearnOrderManagement(self):
        iLearnToOrderManagement = HubworksHome(self.driver)
        iLearnToOrderManagement.learnButtonOrderManagement()
        self.assertTrue(self.driver.current_url == iLearnToOrderManagement.learnButtonOrderManagementScreen())

    #Test the Employee Scheduling Button
    def testEmpScheduling(self):
        iEmpSchedule = HubworksHome(self.driver)
        iEmpSchedule.learnButtonEmployeeScheduling()
        self.assertTrue(self.driver.current_url == iEmpSchedule.learnButtonEmployeeSchedulingScreen())

    #Test the Employee Scheduling Apps Button
    def testEmpSchedulingApp(self):
        iEmpScheduleApps = HubworksHome(self.driver)
        iEmpScheduleApps.learnButtonEmployeeSchedulingApps()
        self.assertTrue(self.driver.current_url == iEmpScheduleApps.learnButtonEmployeeSchedulingAppsScreen())

    #Test the Food Safety Button
    def testFoodSafety(self):
        iFoodSafety = HubworksHome(self.driver)
        iFoodSafety.learnButtonFoodSafety()
        self.assertTrue(self.driver.current_url == iFoodSafety.learnButtonFoodSafetyScreen())

    #Test the Blog Button
    def testBlog(self):
        iBlog = HubworksHome(self.driver)
        iBlog.learnButtonBlog()
        self.assertTrue(self.driver.current_url == iBlog.learnButtonBlogScreen())

    #Test the Resources Button
    def testResources(self):
        iResources = HubworksHome(self.driver)
        iResources.learnButtonResources()
        self.assertTrue(self.driver.current_url == iResources.learnButtonResourcesScreen())

   # def testZipTraining(self):


    #Test the SignUp Button
    def testNewSignUp(self):
        iSign = HubworksHome(self.driver)
        iSign.SignUpButton()
        self.assertTrue(self.driver.current_url == iSign.SignUpButtonScreen())

    #Test the New Employee Button
    def testClickNewEmployee(self):
        iEmp = HubworksHome(self.driver)
        iEmp.NewEmployeeButton()
        self.assertTrue(self.driver.current_url == iEmp.NewEmployeeScreen())

        # Test the Login Button

    def testClickLogin(self):
        iLog = HubworksHome(self.driver)
        iLog.LoginButton()
        self.assertTrue(self.driver.current_url == iLog.LoginButtonScreen())

  #  def testShoppingCart(self):
       # iCart = HubworksHome(self.driver)
       # iCart.cartButton()
       # self.assertTrue("Your Shopping Cart" in self.driver.page_source)

    #Test the Get Started Button
    def testStartButton(self):
        iStart = HubworksHome(self.driver)
        iStart.getStartedButton()
        self.assertTrue(self.driver.current_url == iStart.getStartedScreen())

    #Test the Zip Schedules Button
    def testzipSchedulesButton(self):
        iZipSchedules = HubworksHome(self.driver)
        iZipSchedules.zipSchedulesButton()
        self.assertTrue(self.driver.current_url == iZipSchedules.zipSchedulesScreen())

    #Test the Zip Clock Button
    def testzipClockButton(self):
        iZipClock = HubworksHome(self.driver)
        iZipClock.zipClockButton()
        self.assertTrue(self.driver.current_url == iZipClock.zipClockScreen())

    def testzipChecklistButton(self):
        iZipCheckList = HubworksHome(self.driver)
        iZipCheckList.zipChecklistButton()
        self.assertTrue(self.driver.current_url == iZipCheckList.zipChecklistScreen())

    def testZipHaccpButton(self):
        iZipHaccp = HubworksHome(self.driver)
        iZipHaccp.zipHACCPButton()
        self.assertTrue(self.driver.current_url == iZipHaccp.zipHACCPScreen())

    def testZipInventoryButton(self):
        iZipInventory = HubworksHome(self.driver)
        iZipInventory.zipInventoryButton()
        self.assertTrue(self.driver.current_url == iZipInventory.zipInventoryScreen())

    def testZipOrderingButton(self):
        iZipOrdering = HubworksHome(self.driver)
        iZipOrdering.zipOrderingButton()
        self.assertTrue(self.driver.current_url == iZipOrdering.zipOrderingScreen())

    def testzipPOSDashboardButton(self):
        iZipPOSDashboard = HubworksHome(self.driver)
        iZipPOSDashboard.zipPOSDashboardButton()
        self.assertTrue(self.driver.current_url == iZipPOSDashboard.zipPOSDashboardScreen())

    def testzipForecastingButton(self):
        iZipForecasting = HubworksHome(self.driver)
        iZipForecasting.zipForecastingButton()
        self.assertTrue(self.driver.current_url == iZipForecasting.zipForecastingScreen())

    def testZipReportingButton(self):
        iZipReporting = HubworksHome(self.driver)
        iZipReporting.zipReportingButton()
        self.assertTrue(self.driver.current_url == iZipReporting.zipReportingScreen())

    def testZipShiftbookButton(self):
        iZipShiftbook = HubworksHome(self.driver)
        iZipShiftbook.zipShiftBookButton()
        self.assertTrue(self.driver.current_url == iZipShiftbook.zipShiftbookScreen())

    def testPlumPOSButton(self):
        iPlumPOS = HubworksHome(self.driver)
        iPlumPOS.plumPOSButton()
        self.assertTrue(self.driver.current_url == iPlumPOS.plumPOSScreen())

    def testSmarterKitchenButton(self):
        iSmarterKitchen = HubworksHome(self.driver)
        iSmarterKitchen.smartKitchenButton()
        self.assertTrue(self.driver.current_url == iSmarterKitchen.smarterKitchenScreen())

    def testPlumMailButton(self):
        iPlumMail = HubworksHome(self.driver)
        iPlumMail.plumMailButton()
        self.assertTrue(self.driver.current_url == iPlumMail.plumMailScreen())

    def testAnyConnectorButton(self):
        iAnyConnector = HubworksHome(self.driver)
        iAnyConnector.anyConnectorButton()
        self.assertTrue(self.driver.current_url == iAnyConnector.anyConnectorScreen())

    def testZipSupplyChain(self):
        iZipSupplyChain = HubworksHome(self.driver)
        iZipSupplyChain.zipSupplyChainButton()
        self.assertTrue(self.driver.current_url == iZipSupplyChain.zipSupplyChainScreen())

    def testViewMoreHappyCustomers(self):
        iViewHappy = HubworksHome(self.driver)
        iViewHappy.viewMoreHappyCustomersButton()
        self.assertTrue(self.driver.current_url == iViewHappy.viewMoreHappyCustomersScreen())

    def testRequestDemo(self):
        iDemo = HubworksHome(self.driver)
        iDemo.requestDemoButton()
        self.assertTrue(self.driver.current_url == iDemo.requestDemoScreen())

    def testWebinar(self):
        iWebinar = HubworksHome(self.driver)
        self.WebWindow1 = self.driver.window_handles[0]
        iWebinar.signUpWebinarButton()
        self.WebWindow2 = self.driver.window_handles[1]
        self.driver.switch_to.window(self.WebWindow2)
        self.assertTrue(self.driver.current_url == iWebinar.signUpWebinarScreen())

if __name__ == "__main__":
    unittest.main()



