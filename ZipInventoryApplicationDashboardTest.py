import unittest
from BasePages.Base import BaseClassLoginOrgSaved
from Pages.QAServerPages.ZipInventoryApplicationPages.ZipInventoryDashboardPage import ZipInventoryDashboard
from BasePages.Base import BaseClassWaits
import time


class InventoryDashboardTest(BaseClassLoginOrgSaved):
    DASHBOARDLINK = "https://qa24680.hubworks.com/hwapp/#/inventory/en/main/eyJpc1NTT011bHRpcGxlT3JnRXhpc3RzIjpmYWxzZSwid0luZGV4Ijo2LCJzY2FQSyI6MzkxNDAsInNhUEsiOjEzLCJzYXVQSyI6Mzk2NTgsInNjdVBLIjo0MDMxMiwic2NQSyI6MzgyNTksInNjY1BLIjozODMwOSwic3NQSyI6MjA0NCwibWlkIjoiTWVudV9JbnZlbnRvcnlfSG9tZSIsImR2bFBrIjpudWxsLCJjbVBLIjpudWxsLCJwbWlkIjoiTWVudV9JbnZlbnRvcnlfSG9tZSJ9/home"
    def setUp(self):
        self.driver.get("https://hubworks.com/")
        self.driver.implicitly_wait(60)

    def tearDown(self):
        pass

    def test_dashboard(self):
        #This is a link to a different screen to test whether the drop down dashboard leads to dashboard screen
        self.driver.get("https://qa24680.hubworks.com/hwapp/#/inventory/en/main/eyJpc1NTT011bHRpcGxlT3JnRXhpc3RzIjpmYWxzZSwid0luZGV4IjozLCJzY2FQSyI6MzkxNDAsInNhUEsiOjEzLCJzYXVQSyI6Mzk2NTgsInNjdVBLIjo0MDMxMiwic2NQSyI6MzgyNTksInNjY1BLIjozODMwOSwic3NQSyI6MjA0NCwibWlkIjoiTWVudV9JbnZlbnRvcnlfSG9tZSIsInNpdGVBcHBQSyI6MTMsImR2bFBrIjpudWxsLCJjbVBLIjpudWxsLCJwbWlkIjoiTWVudV9JbnZlbnRvcnlfSG9tZSJ9/home")
        click_dash = ZipInventoryDashboard(self.driver)
        use_base = BaseClassWaits(self.driver)
        use_base.invisible_element_located(click_dash.loader)
        use_base.element_clickable(click_dash.dash_board)
        self.assertTrue("Needing Action" in click_dash.visible_texts())

    def test_dashboard_inventorydollars(self):
        self.driver.get(self.DASHBOARDLINK)
        click_inventory = ZipInventoryDashboard(self.driver)
        use_base = BaseClassWaits(self.driver)
        use_base.invisible_element_located(click_inventory.loader)
        use_base.element_clickable(click_inventory.dash_inventory_dollars)
        self.assertTrue("INVENTORY $" in click_inventory.visible_texts())

    def test_dashboard_weeklydeliveries(self):
        self.driver.get(self.DASHBOARDLINK)
        click_weeklydeliveries = ZipInventoryDashboard(self.driver)
        use_base = BaseClassWaits(self.driver)
        use_base.invisible_element_located(click_weeklydeliveries.loader)
        use_base.element_clickable(click_weeklydeliveries.dash_weekly_deliveries)
        self.assertTrue("WEEKLY DELIVERIES $" in click_weeklydeliveries.visible_texts())

    def test_dashboard_actualfoodcost(self):
        self.driver.get(self.DASHBOARDLINK)
        click_actualfoodcost = ZipInventoryDashboard(self.driver)
        use_base = BaseClassWaits(self.driver)
        use_base.invisible_element_located(click_actualfoodcost.loader)
        use_base.element_clickable(click_actualfoodcost.dash_act_foodcost)
        self.assertTrue("ACTUAL FOOD COST %" in click_actualfoodcost.visible_texts())

    def test_dashboard_variance(self):
        self.driver.get(self.DASHBOARDLINK)
        click_actualvariance = ZipInventoryDashboard(self.driver)
        use_base = BaseClassWaits(self.driver)
        use_base.invisible_element_located(click_actualvariance.loader)
        use_base.element_clickable(click_actualvariance.dash_variance)
        self.assertTrue("VARIANCE %" in click_actualvariance.visible_texts())

    def test_change_dashboard_click(self):
        self.driver.get(self.DASHBOARDLINK)
        click_changes = ZipInventoryDashboard(self.driver)
        use_base = BaseClassWaits(self.driver)
        use_base.invisible_element_located(click_changes.loader)
        use_base.element_clickable(click_changes.dash_variance)
        use_base.element_clickable(click_changes.dash_act_foodcost)
        self.assertTrue("ACTUAL FOOD COST %" in click_changes.visible_texts())


        


if __name__ == "__main__":
    unittest.main()
