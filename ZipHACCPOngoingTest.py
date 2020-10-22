import unittest
from BasePages.Base import BaseClassLoginOrgSaved
from Pages.QAServerPages.ZipHACCP.ZipHACCPOngoing import HACCP_Ongoing_Checklist
from BasePages.Base import BaseClassWaits
from UData.ExcelFiles import GetData


class HACCP_OngoingC_Test(BaseClassLoginOrgSaved):
    HACCP_LINK = "https://qa24680.hubworks.com/hwapp/hwHaccp/#/redirect/eyJzc1BLIjoyOTI1LCJzY2NQSyI6NTg4MDQsInNjYVBLIjo2MDIwNCwic2FQSyI6MjcsInNjUEsiOjU4NzU0LCJzY3VQSyI6NjExNTUsInNhdVBLIjo2MDQwNSwibWlkIjoiTWVudV9Ib21lIn0="
    PATH = "/Users/prodmgmt20/PycharmProjects/Altametrics/UData/QAData/ZipHACCP/ZipHACCPOngoing.xlsx"

    def setUp(self):
        self.driver.get(self.HACCP_LINK)
        self.click_dashboard = HACCP_Ongoing_Checklist(self.driver)
        self.use_base = BaseClassWaits(self.driver)
        self.use_base.invisible_element_located(self.click_dashboard.loader)
        self.use_base.visible_element(self.click_dashboard.dashboard)

    def tearDown(self):
        pass

    def test_ongoing_checklist(self):
        self.use_base.element_clickable(self.click_dashboard.ongoing_checklist)
        self.use_base.invisible_element_located(self.click_dashboard.loader)
        file = GetData(self.PATH, "Ongoing Checklists")
        total_rows = file.get_rows()
        for rows in range(2, total_rows+1):
            list_of_checklists = self.click_dashboard.return_checklist_names()
            actual_results = file.write_data(rows,3,list_of_checklists[rows-2].text)
            results = (list_of_checklists[rows-2].text)
            expected_results = file.read_data_string(rows,2)
            if results == expected_results:
                file.write_data(rows,4,"Pass")
            else:
                file.write_data(rows,4,"Fail")
        for rows in range(2, total_rows+1):
            self.assertTrue(file.read_data_string(rows,4) == "Pass")

    def test_individual_checklist(self):













if __name__ == "__main__":
    unittest.main()






