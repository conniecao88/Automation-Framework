import unittest
from UData.ExcelFiles import GetData
from BasePages.Base import BaseClassWaits
from BasePages.Base import BaseClassLoginOrgSaved
from Pages.QAServerPages.ZipInventoryApplicationPages.ZipInventoryCreditMemoPage import ZipInventoryCredit
from datetime import date
import time


class InventoryCreditMemoTest(BaseClassLoginOrgSaved):
    #CREDITLINK = "https://qa24680.hubworks.com/hwapp/#/inventory/en/main/eyJpc1NTT011bHRpcGxlT3JnRXhpc3RzIjpmYWxzZSwid0luZGV4Ijo2LCJzY2FQSyI6MzkxNDAsInNhUEsiOjEzLCJzYXVQSyI6Mzk2NTgsInNjdVBLIjo0MDMxMiwic2NQSyI6MzgyNTksInNjY1BLIjozODMwOSwic3NQSyI6MjA0NCwibWlkIjoiTWVudV9JbnZlbnRvcnlfY3JlZGl0TWVtbyIsImR2bFBrIjpudWxsLCJjbVBLIjpudWxsLCJwbWlkIjoiTWVudV9JbnZlbnRvcnlfY3JlZGl0TWVtbyJ9/creditMemo"
    CREDITLINK = "https://qa24680.hubworks.com/hwapp/#/inventory/en/main/eyJpc1NTT011bHRpcGxlT3JnRXhpc3RzIjpmYWxzZSwid0luZGV4Ijo2LCJzY2FQSyI6MzkxNDAsInNhUEsiOjEzLCJzYXVQSyI6Mzk2NTgsInNjdVBLIjo0MDMxMiwic2NQSyI6MzgyNTksInNjY1BLIjozODMwOSwic3NQSyI6MjA0NCwibWlkIjoiTWVudV9JbnZlbnRvcnlfY3JlZGl0TWVtbyIsImR2bFBrIjpudWxsLCJjbVBLIjpudWxsLCJwbWlkIjoiTWVudV9JbnZlbnRvcnlfY3JlZGl0TWVtbyJ9/creditMemo"
    PATH = "/UData/QAData/ZipInventory/ZipInventoryCreditMemo.xlsx"
    def setUp(self):
        self.driver.get("https://hubworks.com/")

    def tearDown(self):
        pass

    #Validate whether the left side bar works
    def test_credit(self):
        self.driver.get("https://qa24680.hubworks.com/hwapp/#/inventory/en/main/eyJpc1NTT011bHRpcGxlT3JnRXhpc3RzIjpmYWxzZSwid0luZGV4Ijo2LCJzY2FQSyI6MzkxNDAsInNhUEsiOjEzLCJzYXVQSyI6Mzk2NTgsInNjdVBLIjo0MDMxMiwic2NQSyI6MzgyNTksInNjY1BLIjozODMwOSwic3NQSyI6MjA0NCwibWlkIjoiTWVudV9JbnZlbnRvcnlfSW52U3VtbWFyeSJ9/invSummary")
        use_base = BaseClassWaits(self.driver)
        click_left = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(click_left.loader)
        use_base.element_clickable(click_left.credit_left)
        #self.assertTrue(use_base.element_clickable_instant(click_left.add_credit))
        self.assertTrue("Credit Memo" in self.driver.page_source)

    #Validate whether a credit memo can be added
    def testadd_credit(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        click_credit = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(click_credit.loader)
        use_base.element_clickable(click_credit.add_credit)
        self.assertTrue(use_base.visible_element_instant(click_credit.add_credit_screen))

    #Validate whether suppliers are all clickable
    def testadd_supplier(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        click_supplier = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(click_supplier.loader)
        use_base.element_clickable(click_supplier.add_credit)
        file = GetData(self.PATH, "Suppliers")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            expected_results = file.read_data_string(rows,2)
            use_base.element_clickable(click_supplier.supplier_drop)
            the_list = click_supplier.list_suppliers()
            the_list[rows-1].click()
            file.write_data(rows,3,click_supplier.suppliers_box())
            if expected_results == click_supplier.suppliers_box():
                file.write_data(rows,4,"Pass")
            else:
                file.write_data(rows,4,"Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data(rows,4) == "Pass")

    #Validate whether dates can be chosen (current date)
    def testadd_date(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        click_date = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(click_date.loader)
        use_base.element_clickable(click_date.add_credit)
        use_base.element_clickable(click_date.date_click)
        use_base.element_clickable(click_date.current_date)
        get_date = date.today()
        today_date = get_date.strftime("%m/%d/%Y")
        self.assertTrue(today_date == click_date.date_box())

    #Validate whether the warning for a created credit memo is correct
    def test_credit_memo(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        click_ok = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(click_ok.loader)
        use_base.element_clickable(click_ok.add_credit)
        use_base.element_clickable(click_ok.supplier_drop)
        use_base.element_clickable(click_ok.supplier_select)
        use_base.element_clickable(click_ok.date_click)
        use_base.element_clickable(click_ok.current_date)
        use_base.element_clickable(click_ok.ok_button)
        use_base.visible_element(click_ok.manual_message)
        self.assertTrue(click_ok.man_message() == "Manual Credit Memo created successfully.")

    #Validate whether the created credit memo has all the information
    def test_created_memo(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        created_memo = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(created_memo.loader)
        use_base.element_clickable(created_memo.add_credit)
        use_base.element_clickable(created_memo.supplier_drop)
        use_base.element_clickable(created_memo.supplier_select)
        use_base.element_clickable(created_memo.date_click)
        use_base.element_clickable(created_memo.current_date)
        use_base.element_clickable(created_memo.ok_button)
        #Make sure the page is loaded
        use_base.visible_element(created_memo.close_button)
        file = GetData(self.PATH, "SupplierInfo")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            if file.read_data_string(rows,2) in self.driver.page_source:
                file.write_data(rows,3, "Pass")
            else:
                file.write_data(rows,3,"Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data(rows,3) == "Pass")
        get_date = date.today()
        today_date = get_date.strftime("%m/%d/%Y")
        self.assertTrue(today_date in self.driver.page_source)

    #Validate whether the save warning appears correctly when nothing is entered for the required boxes
    def test_savecreatedwarning(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        click_save = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(click_save.loader)
        use_base.element_clickable(click_save.add_credit)
        use_base.element_clickable(click_save.supplier_drop)
        use_base.element_clickable(click_save.supplier_select)
        use_base.element_clickable(click_save.date_click)
        use_base.element_clickable(click_save.current_date)
        use_base.element_clickable(click_save.ok_button)
        use_base.invisible_element_located(click_save.manual_message)
        use_base.element_clickable(click_save.save_button)
        use_base.visible_element(click_save.manual_message)
        self.assertTrue(click_save.man_message() == "There should be atleast one item for Credit Memo.")

    #Validate whether the finalized warning appears correctly when nothing is entered for the required boxes
    def test_finalizecreditwarning(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        click_finalize = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(click_finalize.loader)
        use_base.element_clickable(click_finalize.add_credit)
        use_base.element_clickable(click_finalize.supplier_drop)
        use_base.element_clickable(click_finalize.supplier_select)
        use_base.element_clickable(click_finalize.date_click)
        use_base.element_clickable(click_finalize.current_date)
        use_base.element_clickable(click_finalize.ok_button)
        use_base.invisible_element_located(click_finalize.manual_message)
        use_base.element_clickable(click_finalize.finalize_button)
        use_base.visible_element(click_finalize.manual_message)
        self.assertTrue(click_finalize.man_message() == "Credit Notes cannot be blank.")

    #Validate whether a warning appears when a credit note is entered with no order number and is saved
    def test_finalize_note_warning(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        finalize_nonote_warning = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(finalize_nonote_warning.loader)
        use_base.element_clickable(finalize_nonote_warning.add_credit)
        use_base.element_clickable(finalize_nonote_warning.supplier_drop)
        use_base.element_clickable(finalize_nonote_warning.supplier_select)
        use_base.element_clickable(finalize_nonote_warning.date_click)
        use_base.element_clickable(finalize_nonote_warning.current_date)
        use_base.element_clickable(finalize_nonote_warning.ok_button)
        use_base.visible_element(finalize_nonote_warning.credit_note)
        file = GetData(self.PATH, "NoCreditNote")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 3)
            finalize_nonote_warning.type_credit(file.read_data_string(rows, 1))
            finalize_nonote_warning.type_order(file.read_data_string(rows,2))
            use_base.element_clickable(finalize_nonote_warning.finalize_button)
            use_base.visible_element(finalize_nonote_warning.manual_message)
            file.write_data(rows, 4, finalize_nonote_warning.man_message())
            if expected_results == finalize_nonote_warning.man_message():
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
            use_base.invisible_element(finalize_nonote_warning.manual_message)
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data(rows, 4) == "Pass")

        # Validate whether a warning appears when a credit note is entered with no order number and is saved

    def test_finalize_order_warning(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        finalize_noorder_warning = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(finalize_noorder_warning.loader)
        use_base.element_clickable(finalize_noorder_warning.add_credit)
        use_base.element_clickable(finalize_noorder_warning.supplier_drop)
        use_base.element_clickable(finalize_noorder_warning.supplier_select)
        use_base.element_clickable(finalize_noorder_warning.date_click)
        use_base.element_clickable(finalize_noorder_warning.current_date)
        use_base.element_clickable(finalize_noorder_warning.ok_button)
        use_base.visible_element(finalize_noorder_warning.credit_note)
        file = GetData(self.PATH, "NoCreditNote")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 3)
            finalize_noorder_warning.type_credit(file.read_data_string(rows, 1))
            finalize_noorder_warning.type_order(file.read_data_string(rows, 2))
            use_base.element_clickable(finalize_noorder_warning.finalize_button)
            use_base.visible_element(finalize_noorder_warning.manual_message)
            file.write_data(rows, 4, finalize_noorder_warning.man_message())
            if expected_results == finalize_noorder_warning.man_message():
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
            use_base.invisible_element(finalize_noorder_warning.manual_message)
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data(rows, 4) == "Pass")





    #Validate whether the close button works correctly
    def test_closecredit(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        click_close = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(click_close.loader)
        use_base.element_clickable(click_close.add_credit)
        use_base.element_clickable(click_close.supplier_drop)
        use_base.element_clickable(click_close.supplier_select)
        use_base.element_clickable(click_close.date_click)
        use_base.element_clickable(click_close.current_date)
        use_base.element_clickable(click_close.ok_button)
        use_base.element_clickable(click_close.close_button)
        self.assertTrue(use_base.visible_element(click_close.add_credit))

    #Validate whether a note can be added
    def test_add_note(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        add_note = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(add_note.loader)
        use_base.element_clickable(add_note.add_credit)
        use_base.element_clickable(add_note.supplier_drop)
        use_base.element_clickable(add_note.supplier_select)
        use_base.element_clickable(add_note.date_click)
        use_base.element_clickable(add_note.current_date)
        use_base.element_clickable(add_note.ok_button)
        use_base.visible_element(add_note.credit_note)
        file = GetData(self.PATH, "CreditNote")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            expected_results = file.read_data_string(rows,2)
            add_note.type_credit(file.read_data_string(rows,1))
            file.write_data(rows,3,add_note.credit_note_box())
            if expected_results == add_note.credit_note_box():
                file.write_data(rows,4,"Pass")
            else:
                file.write_data(rows,4,"Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data(rows,4) == "Pass")

    def test_add_order_number(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        add_order_num = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(add_order_num.loader)
        use_base.element_clickable(add_order_num.add_credit)
        use_base.element_clickable(add_order_num.supplier_drop)
        use_base.element_clickable(add_order_num.supplier_select)
        use_base.element_clickable(add_order_num.date_click)
        use_base.element_clickable(add_order_num.current_date)
        use_base.element_clickable(add_order_num.ok_button)
        use_base.visible_element(add_order_num.credit_note)
        file = GetData(self.PATH, "OrderNote")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 2)
            add_order_num.type_order(file.read_data_string(rows, 1))
            file.write_data(rows, 3, add_order_num.order_note_box())
            if expected_results == add_order_num.order_note_box():
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data(rows, 4) == "Pass")

    def test_add_invoice_number(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        add_invoice_num = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(add_invoice_num.loader)
        use_base.element_clickable(add_invoice_num.add_credit)
        use_base.element_clickable(add_invoice_num.supplier_drop)
        use_base.element_clickable(add_invoice_num.supplier_select)
        use_base.element_clickable(add_invoice_num.date_click)
        use_base.element_clickable(add_invoice_num.current_date)
        use_base.element_clickable(add_invoice_num.ok_button)
        use_base.visible_element(add_invoice_num.credit_note)
        file = GetData(self.PATH, "InvoiceNumber")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 2)
            add_invoice_num.type_invoice(file.read_data_string(rows, 1))
            file.write_data(rows, 3, add_invoice_num.invoice_box())
            if expected_results == add_invoice_num.invoice_box():
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data(rows, 4) == "Pass")

    def test_add_authorization_number(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        add_auth_num = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(add_auth_num.loader)
        use_base.element_clickable(add_auth_num.add_credit)
        use_base.element_clickable(add_auth_num.supplier_drop)
        use_base.element_clickable(add_auth_num.supplier_select)
        use_base.element_clickable(add_auth_num.date_click)
        use_base.element_clickable(add_auth_num.current_date)
        use_base.element_clickable(add_auth_num.ok_button)
        use_base.visible_element(add_auth_num.credit_note)
        file = GetData(self.PATH, "InvoiceNumber")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 2)
            add_auth_num.type_authorization(file.read_data_string(rows, 1))
            file.write_data(rows, 3, add_auth_num.authorization_box())
            if expected_results == add_auth_num.authorization_box():
                file.write_data(rows, 4, "Pass")
            else:
                file.write_data(rows, 4, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data(rows, 4) == "Pass")

    def test_add_item(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        click_add_item = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(click_add_item.loader)
        use_base.element_clickable(click_add_item.add_credit)
        use_base.element_clickable(click_add_item.supplier_drop)
        use_base.element_clickable(click_add_item.supplier_select)
        use_base.element_clickable(click_add_item.date_click)
        use_base.element_clickable(click_add_item.current_date)
        use_base.element_clickable(click_add_item.ok_button)
        use_base.visible_element(click_add_item.credit_note)
        use_base.element_clickable(click_add_item.item_drop)
        use_base.element_clickable(click_add_item.item_drop_child)
        file = GetData(self.PATH, "SearchItem")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            if file.read_data_string(rows,2) in self.driver.page_source:
                file.write_data(rows,3, "Pass")
            else:
                file.write_data(rows,3, "Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows,3) == "Pass")

    #Enter the item quantity and see if only numbers can be entered
    def test_item_quantity(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        type_itemq = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(type_itemq.loader)
        use_base.element_clickable(type_itemq.add_credit)
        use_base.element_clickable(type_itemq.supplier_drop)
        use_base.element_clickable(type_itemq.supplier_select)
        use_base.element_clickable(type_itemq.date_click)
        use_base.element_clickable(type_itemq.current_date)
        use_base.element_clickable(type_itemq.ok_button)
        use_base.visible_element(type_itemq.credit_note)
        use_base.element_clickable(type_itemq.item_drop)
        use_base.element_clickable(type_itemq.item_drop_child)
        file = GetData(self.PATH, "ItemQuantity")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            expected_results = file.read_data_string(rows,3)
            type_itemq.type_quantity(file.read_data_string(rows,2))
            file.write_data(rows,4,type_itemq.received_box())
            if expected_results == type_itemq.received_box():
                file.write_data(rows,5,"Pass")
            else:
                file.write_data(rows,5,"Fail")
        for rows in range (2, total_rows+1):
            self.assertTrue(file.read_data_string(rows,5) == "Pass")

    #Enter the item quantity and see if the credit amount/total credit amount changes based on this
    def test_item_quantity_entered(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        enter_itemq = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(enter_itemq.loader)
        use_base.element_clickable(enter_itemq.add_credit)
        use_base.element_clickable(enter_itemq.supplier_drop)
        use_base.element_clickable(enter_itemq.supplier_select)
        use_base.element_clickable(enter_itemq.date_click)
        use_base.element_clickable(enter_itemq.current_date)
        use_base.element_clickable(enter_itemq.ok_button)
        use_base.visible_element(enter_itemq.credit_note)
        use_base.element_clickable(enter_itemq.item_drop)
        use_base.element_clickable(enter_itemq.item_drop_child)
        file = GetData(self.PATH, "EnterQuantity")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results_credit = file.read_data_string(rows, 3)
            expected_results_total_credit = file.read_data_string(rows,4)
            enter_itemq.type_quantity_enter(file.read_data_string(rows, 2))
            file.write_data(rows,5, enter_itemq.credit_amount_box())
            file.write_data(rows,6, enter_itemq.total_credit_amount_box())
            if expected_results_credit == enter_itemq.credit_amount_box() and expected_results_total_credit == enter_itemq.total_credit_amount_box():
                file.write_data(rows, 7, "Pass")
            else:
                file.write_data(rows, 7, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data_string(rows, 7) == "Pass")

    #Enter the credit amount textbox and see if only numbers can be entered
    def test_credit_amount(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        type_credita = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(type_credita.loader)
        use_base.element_clickable(type_credita.add_credit)
        use_base.element_clickable(type_credita.supplier_drop)
        use_base.element_clickable(type_credita.supplier_select)
        use_base.element_clickable(type_credita.date_click)
        use_base.element_clickable(type_credita.current_date)
        use_base.element_clickable(type_credita.ok_button)
        use_base.visible_element(type_credita.credit_note)
        use_base.element_clickable(type_credita.item_drop)
        use_base.element_clickable(type_credita.item_drop_child)
        file = GetData(self.PATH, "CreditAmount")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 3)
            type_credita.type_credit_amount(file.read_data_string(rows, 2))
            file.write_data(rows, 4, type_credita.credit_amount_box())
            if expected_results == type_credita.credit_amount_box():
                file.write_data(rows, 5, "Pass")
            else:
                file.write_data(rows, 5, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data_string(rows, 5) == "Pass")

    #Enter in the credit amount textbox and see if the total credit amount changes based on this
    #Dont exceed 7 digits numbers on excel, clear button doesnt work, only backspace can be used, and page consists of 9 backspaces
    def test_credit_amount_entered(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        enter_credita = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(enter_credita.loader)
        use_base.element_clickable(enter_credita.add_credit)
        use_base.element_clickable(enter_credita.supplier_drop)
        use_base.element_clickable(enter_credita.supplier_select)
        use_base.element_clickable(enter_credita.date_click)
        use_base.element_clickable(enter_credita.current_date)
        use_base.element_clickable(enter_credita.ok_button)
        use_base.visible_element(enter_credita.credit_note)
        use_base.element_clickable(enter_credita.item_drop)
        use_base.element_clickable(enter_credita.item_drop_child)
        file = GetData(self.PATH, "EnterCAmount")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            expected_results = file.read_data_string(rows, 3)
            enter_credita.type_credit_enter(file.read_data_string(rows, 2))
            file.write_data(rows,4, enter_credita.total_credit_amount_box())
            if expected_results == enter_credita.total_credit_amount_box():
                file.write_data(rows, 5, "Pass")
            else:
                file.write_data(rows, 5, "Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data_string(rows, 5) == "Pass")

    def test_item_trash_click(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        click_item_trash = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(click_item_trash.loader)
        use_base.element_clickable(click_item_trash.add_credit)
        use_base.element_clickable(click_item_trash.supplier_drop)
        use_base.element_clickable(click_item_trash.supplier_select)
        use_base.element_clickable(click_item_trash.date_click)
        use_base.element_clickable(click_item_trash.current_date)
        use_base.element_clickable(click_item_trash.ok_button)
        use_base.visible_element(click_item_trash.credit_note)
        use_base.element_clickable(click_item_trash.item_drop)
        use_base.element_clickable(click_item_trash.item_drop_child)
        use_base.element_clickable(click_item_trash.item_trashcan)
        self.assertFalse("SKU No." in self.driver.page_source)

    #Test whether a credit memo can be saved successfully
    #Number for item quantity can be hard coded, since you just want to test if it can be saved
    def test_save_successful(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        save_success = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(save_success.loader)
        use_base.element_clickable(save_success.add_credit)
        use_base.element_clickable(save_success.supplier_drop)
        use_base.element_clickable(save_success.supplier_select)
        use_base.element_clickable(save_success.date_click)
        use_base.element_clickable(save_success.current_date)
        use_base.element_clickable(save_success.ok_button)
        use_base.visible_element(save_success.credit_note)
        use_base.invisible_element_located(save_success.manual_message)
        use_base.element_clickable(save_success.item_drop)
        use_base.element_clickable(save_success.item_drop_child)
        save_success.type_quantity_enter(3)
        use_base.element_clickable(save_success.save_button)
        use_base.visible_element(save_success.manual_message)
        self.assertTrue(save_success.man_message() == "Credit Memo updated successfully.")

    def test_finalize_successful(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        finalize_success = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(finalize_success.loader)
        use_base.element_clickable(finalize_success.add_credit)
        use_base.element_clickable(finalize_success.supplier_drop)
        use_base.element_clickable(finalize_success.supplier_select)
        use_base.element_clickable(finalize_success.date_click)
        use_base.element_clickable(finalize_success.current_date)
        use_base.element_clickable(finalize_success.ok_button)
        use_base.visible_element(finalize_success.credit_note)
        use_base.invisible_element_located(finalize_success.manual_message)
        use_base.element_clickable(finalize_success.item_drop)
        use_base.element_clickable(finalize_success.item_drop_child)
        finalize_success.type_quantity_enter(3)
        finalize_success.type_credit("hello")
        finalize_success.type_order("hello")
        use_base.element_clickable(finalize_success.finalize_button)
        use_base.visible_element(finalize_success.manual_message)
        self.assertTrue(finalize_success.man_message() == "Credit Memo finalized successfully.")

    def test_editing_credit_memo(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        edit_memo = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(edit_memo.loader)
        use_base.element_clickable(edit_memo.click_created_memo)
        use_base.visible_element_instant(edit_memo.credit_note)
        self.assertTrue("Credit Note:" in self.driver.page_source)

    def test_delete_credit_memo(self):
        self.driver.get(self.CREDITLINK)
        use_base = BaseClassWaits(self.driver)
        delete_memo = ZipInventoryCredit(self.driver)
        use_base.invisible_element_located(delete_memo.loader)
        use_base.element_clickable(delete_memo.delete_memo_trashcan)
        use_base.visible_element(delete_memo.manual_message)
        self.assertTrue(delete_memo.man_message() == "Credit Memo deleted successfully.")






if __name__ == "__main__":
    unittest.main()