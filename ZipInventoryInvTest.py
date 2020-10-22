import unittest
from Pages.QAServerPages.ZipInventoryApplicationPages.ZipInventoryInvPage import Inv_Page
from BasePages.Base import BaseClassWaits
from BasePages.Base import BaseClassLoginOrgSaved
from UData.ExcelFiles import GetData


class Inventory_Test(BaseClassLoginOrgSaved):
    INVENTORYLINK = "https://qa24680.hubworks.com/hwapp/#/inventory/en/main/eyJpc1NTT011bHRpcGxlT3JnRXhpc3RzIjpmYWxzZSwid0luZGV4Ijo1LCJzY2FQSyI6MzkxNDAsInNhUEsiOjEzLCJzYXVQSyI6Mzk2NTgsInNjdVBLIjo0MDMxMiwic2NQSyI6MzgyNTksInNjY1BLIjozODMwOSwic3NQSyI6MjE2OCwibWlkIjoiTWVudV9JbnZlbnRvcnlfSW52U3VtbWFyeSIsImR2bFBrIjpudWxsLCJjbVBLIjpudWxsfQ==/invSummary"
    PATH = "/UData/QAData/ZipInventory/ZipInventoryInventory.xlsx"

    def setUp(self):
        self.driver.get("https://hubworks.com/")

    def tearDown(self):
        pass

    def test_add_inventory(self):
        self.driver.get(self.INVENTORYLINK)
        use_base = BaseClassWaits(self.driver)
        add_inv = Inv_Page(self.driver)
        use_base.invisible_element(add_inv.loader)
        use_base.element_clickable(add_inv.add_inventory)
        self.assertTrue(use_base.visible_element_instant(add_inv.add_popup))

    def test_add_inv_count(self):
        self.driver.get(self.INVENTORYLINK)
        use_base = BaseClassWaits(self.driver)
        add_count = Inv_Page(self.driver)
        use_base.invisible_element(add_count.loader)
        use_base.element_clickable(add_count.)












