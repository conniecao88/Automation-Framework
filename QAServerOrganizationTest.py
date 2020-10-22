import unittest
from Pages.QAServerPages.QAMainPages.QAServerOrganizationPage import QAOrganizationKeys
from BasePages.Base import BaseClassLoginSaved
from BasePages.Base import BaseClassWaits


class QAOrganizationTest(BaseClassLoginSaved):

    def setUp(self):
        self.driver.get("https://qa24680.hubworks.com/hwsso/#/login/")

    def tearDown(self):
        pass


    def testApplicationOne(self):
        org_one = QAOrganizationKeys(self.driver)
        use_base = BaseClassWaits(self.driver)
        use_base.element_clickable(org_one.a_org)
        use_base.invisible_element_located(org_one.loader)
        use_base.element_clickable(org_one.dropdown_profile)
        self.assertTrue("Adam Yun's Organization" in self.driver.page_source)

    def testApplicationTwo(self):
        org_two = QAOrganizationKeys(self.driver)
        use_base = BaseClassWaits(self.driver)
        use_base.element_clickable(org_two.j_org)
        use_base.invisible_element_located(org_two.loader)
        use_base.element_clickable(org_two.dropdown_profile)
        self.assertTrue("Joe Schmoe's Delicious Eatery" in self.driver.page_source)

    def testApplicationThree(self):
        org_three = QAOrganizationKeys(self.driver)
        use_base = BaseClassWaits(self.driver)
        use_base.element_clickable(org_three.k_org)
        use_base.invisible_element_located(org_three.loader)
        use_base.element_clickable(org_three.dropdown_profile)
        self.assertTrue("K Horton's Organization" in self.driver.page_source)

    def testApplicationFour(self):
        org_four = QAOrganizationKeys(self.driver)
        use_base = BaseClassWaits(self.driver)
        use_base.element_clickable(org_four.m_org)
        use_base.invisible_element_located(org_four.loader)
        use_base.element_clickable(org_four.dropdown_profile)
        self.assertTrue("Micheal Scott's Organization" in self.driver.page_source)


if __name__ == "__main__":
    unittest.main()