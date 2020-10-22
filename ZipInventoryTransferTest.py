import unittest
from Pages.QAServerPages.ZipInventoryApplicationPages.ZipInventoryTransferPage import Transfer_Page
from BasePages.Base import BaseClassWaits
from BasePages.Base import BaseClassLoginOrgSaved
from UData.ExcelFiles import GetData

class Transfer_Test(BaseClassLoginOrgSaved):
    TRANSFERLINK = "https://qa24680.hubworks.com/hwapp/#/inventory/en/main/eyJpc1NTT011bHRpcGxlT3JnRXhpc3RzIjpmYWxzZSwid0luZGV4Ijo2LCJzY2FQSyI6MzkxNDAsInNhUEsiOjEzLCJzYXVQSyI6Mzk2NTgsInNjdVBLIjo0MDMxMiwic2NQSyI6MzgyNTksInNjY1BLIjozODMwOSwic3NQSyI6MjA0NCwibWlkIjoiTWVudV9JbnZlbnRvcnlfVHJhbnNmZXIiLCJkdmxQayI6bnVsbCwiY21QSyI6bnVsbCwicG1pZCI6Ik1lbnVfSW52ZW50b3J5X1RyYW5zZmVyIn0=/transfer"
    PATH = "/UData/QAData/ZipInventory/ZipInventoryTransfers.xlsx"

    def setUp(self):
        self.driver.get("https://hubworks.com/")
        #self.driver.implicitly_wait(60)

    def tearDown(self):
        pass

    #Click Transfer on the Side
    def test_side_transfer(self):
        self.driver.get("https://qa24680.hubworks.com/hwapp/#/inventory/en/main/eyJpc1NTT011bHRpcGxlT3JnRXhpc3RzIjpmYWxzZSwid0luZGV4Ijo2LCJzY2FQSyI6MzkxNDAsInNhUEsiOjEzLCJzYXVQSyI6Mzk2NTgsInNjdVBLIjo0MDMxMiwic2NQSyI6MzgyNTksInNjY1BLIjozODMwOSwic3NQSyI6MjA0NCwibWlkIjoiTWVudV9JbnZlbnRvcnlfSG9tZSIsImR2bFBrIjpudWxsLCJjbVBLIjpudWxsLCJwbWlkIjoiTWVudV9JbnZlbnRvcnlfSG9tZSJ9/home")
        use_base = BaseClassWaits(self.driver)
        click_side = Transfer_Page(self.driver)
        use_base.invisible_element(click_side.loader)
        use_base.element_clickable(click_side.transfer_button)
        self.assertTrue("Transfer Out" in click_side.visible_texts())

    #Click Transfer out button
    def test_add_transfer_out(self):
        self.driver.get(self.TRANSFERLINK)
        use_base = BaseClassWaits(self.driver)
        click_transfer_out = Transfer_Page(self.driver)
        use_base.invisible_element(click_transfer_out.loader)
        use_base.element_clickable(click_transfer_out.add_transfer_out)
        self.assertTrue(use_base.visible_element_instant(click_transfer_out.transfer_popup))


    #Validate going through the site list
    def testadd_site(self):
        self.driver.get(self.TRANSFERLINK)
        use_base = BaseClassWaits(self.driver)
        click_site = Transfer_Page(self.driver)
        use_base.invisible_element_located(click_site.loader)
        use_base.element_clickable(click_site.add_transfer_out)
        file = GetData(self.PATH, "TransferOut")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 2)
            use_base.element_clickable(click_site.site_drop)
            the_list = click_site.list_sites()
            the_list[rows - 1].click()
            file.write_data(rows, 3, click_site.site_box())
            if expected_results == click_site.site_box():
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data(rows, 4) == "Pass")

    #Validate transfer in screen
    def test_transfer_in(self):
        self.driver.get(self.TRANSFERLINK)
        use_base = BaseClassWaits(self.driver)
        click_in = Transfer_Page(self.driver)
        use_base.invisible_element_located(click_in.loader)
        use_base.element_clickable(click_in.transfer_in_tab)
        file = GetData(self.PATH, "TransferIn")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 2)
            if file.read_data_string(rows,2) in click_in.visible_texts():
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data(rows, 4) == "Pass")

    #Validate Edit Transfer in Screen
    def test_edit_transfer_in(self):
        self.driver.get(self.TRANSFERLINK)
        use_base = BaseClassWaits(self.driver)
        click_edit = Transfer_Page(self.driver)
        use_base.invisible_element_located(click_edit.loader)
        use_base.element_clickable(click_edit.transfer_in_tab)
        #use_base.element_clickable(click_edit.edit_transfer_in)
        file = GetData(self.PATH, "EditTransferIn")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 2)
            if file.read_data_string(rows, 2) in click_edit.visible_texts():
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data(rows, 4) == "Pass")

    #Test whether finalize transfer button works correctly and the information is accurate
    def test_finalize_transfer(self):
        self.driver.get(self.TRANSFERLINK)
        use_base = BaseClassWaits(self.driver)
        finalize_transfer = Transfer_Page(self.driver)
        use_base.invisible_element(finalize_transfer.loader)
        #Select Site "Costa Mesa"
        use_base.element_clickable(finalize_transfer.select_sites)
        use_base.element_clickable(finalize_transfer.select_sites_child)
        #Click on "Transfer Out"
        use_base.visible_element(finalize_transfer.add_transfer_out)
        #Click on Add a Transfer Out
        use_base.element_clickable(finalize_transfer.add_transfer_out)
        #Select the Site "Site 2" to transfer to
        use_base.element_clickable(finalize_transfer.site_drop)
        use_base.element_clickable(finalize_transfer.site_site_chosen)
        #Click on the Add Button
        use_base.element_clickable(finalize_transfer.add_button)
        use_base.invisible_element_located(finalize_transfer.loader)
        file = GetData(self.PATH, "FinalizeTransfer")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            expected_results = file.read_data_string(rows, 4)
            finalize_transfer.type_item(file.read_data_string(rows,2))
            use_base.visible_element(finalize_transfer.select_item)
            finalize_transfer.select_items()
            use_base.visible_element(finalize_transfer.add_unit_1)
            finalize_transfer.add_first_unit(file.read_data_string(rows,3))
            use_base.element_clickable(finalize_transfer.transfer_out)
            use_base.visible_element(finalize_transfer.manual_message)
            use_base.invisible_element_located(finalize_transfer.manual_message)
            use_base.hover_mouse(finalize_transfer.switch_sites(), finalize_transfer.click_switched_site())
            use_base.invisible_element(finalize_transfer.loader)
            use_base.visible_element(finalize_transfer.transfer_in_tab)
            use_base.element_clickable(finalize_transfer.transfer_in_tab)
            use_base.element_clickable(finalize_transfer.edit_transfer_in)
            use_base.element_clickable(finalize_transfer.finalize_button)
            if file.read_data_string(rows, 4) in finalize_transfer.visible_texts() and file.read_data_string(rows,3) in finalize_transfer.visible_texts():
                file.write_data(rows, 6, "Pass")
            else:
                file.write_data(rows, 6, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data(rows, 6) == "Pass")





























if __name__ == "__main__":
    unittest.main()