import unittest
from BasePages.Base import BaseClassLoginOrgSaved
from Pages.QAServerPages.ZipHACCP.ZipHACCPDashboard import HACCP_Dashboard
from BasePages.Base import BaseClassWaits
from UData.ExcelFiles import GetData
from datetime import datetime

class HACCP_Dashboard_Test(BaseClassLoginOrgSaved):
    HACCP_LINK = "https://qa24680.hubworks.com/hwapp/hwHaccp/#/redirect/eyJzc1BLIjoyOTI1LCJzY2NQSyI6NTg4MDQsInNjYVBLIjo2MDIwNCwic2FQSyI6MjcsInNjUEsiOjU4NzU0LCJzY3VQSyI6NjExNTUsInNhdVBLIjo2MDQwNSwibWlkIjoiTWVudV9Ib21lIn0="
    PATH = "/Users/prodmgmt20/PycharmProjects/Altametrics/UData/QAData/ZipHACCP/ZipHACCPDashboard.xlsx"

    def setUp(self):
        self.driver.get(self.HACCP_LINK)
        self.click_dashboard = HACCP_Dashboard(self.driver)

    def tearDown(self):
        pass

    #Tests whether the Dashboard on the left side can be clicked on and leads to the correct page
    def test_click_dashboard(self):
        self.click_dashboard.click_on_dashboard()
        self.assertTrue(self.driver.current_url == "https://qa24680.hubworks.com/hwapp/hwHaccp/#/haccp/main/dashboard")


    #Tests whether the headers for Dashboard is accurate
    def test_dashboard_info(self):
        self.click_dashboard.click_on_dashboard()
        file = GetData(self.PATH,"Dashboard")
        total_rows = file.get_rows()
        for rows in range(2, total_rows + 1):
            #Grab all the texts from the dashboard on the screen
            the_texts = self.click_dashboard.test_texts()
            file.write_data(rows,3,the_texts[rows-2].text)
            if file.read_data_string(rows,2) == the_texts[rows-2].text:
                file.write_data(rows,4,"Pass")
            else:
                file.write_data(rows,4,"Fail")
        for rows in range(2, total_rows + 1):
            self.assertTrue(file.read_data_string(rows,4) == "Pass")

    #Tests whether the previous percentage is accurate
    def test_dash_previous_percent(self):
        self.click_dashboard.click_on_historial_checklist()
        current_date = datetime.today().isoweekday()
        self.total_completed_1 = []
        self.total_completed_and_uncompleted_1 = []
        self.total_tasks_completed_1 = []
        self.total_tasks_1 = []
        self.comp_task_value_1 = 0
        self.tot_tasks_value_1 = 0
        #Begin by starting to go back to Sunday
        for date in range(0, current_date):
            #Click on the back calendar
            self.click_dashboard.click_on_back_calendar()
        #Always going to get the 7 days worth of data
        for date in range(0, 7):
            list_of_checklists = self.click_dashboard.return_expand()
            for numbers in list_of_checklists:
                numbers.click()
                self.click_dashboard.wait_for_loader()
                self.total_completed_1 = self.click_dashboard.return_completed_tasks()
                self.total_completed_and_uncompleted_1 = self.click_dashboard.return_total_tasks()
            self.total_tasks_completed_1.append(len(self.total_completed_1))
            self.total_tasks_1.append(len(self.total_completed_and_uncompleted_1))
            self.click_dashboard.scroll_up_page()
            self.click_dashboard.click_on_back_calendar()
        for comp_tasks in range(0,len(self.total_tasks_completed_1)):
            self.comp_task_value_1 = self.comp_task_value_1 + int(self.total_tasks_completed_1[comp_tasks])
        for tot_tasks in range(0, len(self.total_tasks_1)):
            self.tot_tasks_value_1 = self.tot_tasks_value_1 + int(self.total_tasks_1[tot_tasks])
        self.click_dashboard.wait_for_percentages_load()
        if int(self.tot_tasks_value_1) == 0:
            self.final_actual_value_1 = "No task exist"
            self.assertTrue(self.final_actual_value_1 == self.click_dashboard.return_comp_no_data())
        else:
            self.total_values_1 = float(self.comp_task_value_1) / float(self.tot_tasks_value_1)
            self.actual_value_1 = self.total_values_1 * 100
            self.final_actual_value_1 = ("%.2f" % self.actual_value_1)
            self.click_dashboard.wait_for_percentages_load()
            actual_value_text = self.final_actual_value_1 + "% Complete"
            self.assertTrue(actual_value_text == self.click_dashboard.return_comp_previous_percentage())

    #Tests whether the percentage of completed tasks is correct
    def test_dash_current_percent(self):
        self.click_dashboard.click_on_historial_checklist()
        current_date = datetime.today().isoweekday()
        self.total_completed = []
        self.total_completed_and_uncompleted = []
        self.total_completed_weekly = []
        self.total_completed_and_uncompleted_weekly = []
        self.total_tasks_completed = []
        self.total_tasks = []
        self.comp_task_value = 0
        self.tot_tasks_value = 0
        for date in range(0,current_date):
            list_of_checklists = self.click_dashboard.return_expand()
            for numbers in list_of_checklists:
                numbers.click()
                self.click_dashboard.wait_for_loader()
                self.total_completed = self.click_dashboard.return_completed_tasks()
                self.total_completed_and_uncompleted = self.click_dashboard.return_total_tasks()
            self.total_tasks_completed.append(len(self.total_completed))
            self.total_tasks.append(len(self.total_completed_and_uncompleted))
            #print(len(self.total_completed_and_uncompleted))
            self.click_dashboard.scroll_up_page()
            self.click_dashboard.click_on_back_calendar()
        self.click_dashboard.click_on_dashboard()
        self.click_dashboard.click_on_historial_checklist()
        self.click_dashboard.click_on_weekly_tasks()
        self.click_dashboard.wait_for_loader()
        list_of_checklists_weekly = self.click_dashboard.return_expand_weekly()
        for numbers in list_of_checklists_weekly:
            numbers.click()
            self.click_dashboard.wait_for_loader()
            self.total_completed_weekly = self.click_dashboard.return_completed_tasks()
            self.total_completed_and_uncompleted_weekly = self.click_dashboard.return_total_tasks()
        #Don't grab weekly tasks from weelky tasks if the current date is Sunday as it will be displayed
        if current_date == 7:
            self.total_tasks_completed.append(0)
            self.total_tasks.append(0)
        else:
            self.total_tasks_completed.append(len(self.total_completed_weekly))
            self.total_tasks.append(len(self.total_completed_and_uncompleted_weekly))
        for comp_tasks in range(0,len(self.total_tasks_completed)):
            self.comp_task_value = self.comp_task_value + int(self.total_tasks_completed[comp_tasks])
        for tot_tasks in range(0, len(self.total_tasks)):
            self.tot_tasks_value = self.tot_tasks_value + int(self.total_tasks[tot_tasks])
        self.total_values = float(self.comp_task_value) / float(self.tot_tasks_value)
        self.actual_value = (self.total_values * 100)
        self.final_actual_value = ("%.2f" % self.actual_value)
        if self.final_actual_value.endswith(".00"):
            self.final_actual_value = ("%.0f" % float(self.final_actual_value))
        else:
            self.final_actual_value = self.final_actual_value
        self.click_dashboard.wait_for_percentages_load()
        actual_value_text = self.final_actual_value + "% Complete"
        print(actual_value_text)
        print(self.click_dashboard.return_comp_percentage())
        self.assertTrue(actual_value_text == self.click_dashboard.return_comp_percentage())

    def test_previous_escalated_percent(self):
        self.click_dashboard.click_on_historial_checklist()
        current_date = datetime.today().isoweekday()
        self.total_esc_tasks_1 = []
        self.total_tasks_for_escalation_1 = []
        self.final_esc_tasks_1 = []
        self.total_tasks_1_esc = []
        self.week_esc_tasks_1 = 0
        self.total_total_tasks_1 = 0
        # Begin by going back to Sunday
        for date in range(0, current_date):
            self.click_dashboard.click_on_back_calendar()
        # Always grab 7 days as there are 7 days in a week
        for date in range(0, 7):
            list_of_checklists = self.click_dashboard.return_expand()
            for numbers in list_of_checklists:
                numbers.click()
                self.click_dashboard.wait_for_loader()
                self.total_esc_tasks_1 = self.click_dashboard.return_esc_tasks()
                self.total_tasks_for_escalation_1 = self.click_dashboard.return_total_tasks()
            self.final_esc_tasks_1.append(len(self.total_esc_tasks_1))
            self.total_tasks_1_esc.append(len(self.total_tasks_for_escalation_1))
            self.click_dashboard.scroll_up_page()
            self.click_dashboard.click_on_back_calendar()
        for numbers in range(0, len(self.final_esc_tasks_1)):
            self.week_esc_tasks_1 = self.week_esc_tasks_1 + int(self.final_esc_tasks_1[numbers])
        for tasks in range(0, len(self.total_tasks_1_esc)):
            self.total_total_tasks_1 = self.total_total_tasks_1 + int(self.total_tasks_1_esc[tasks])
        self.click_dashboard.wait_for_percentages_load()
        # Always going to have No escalated Task exist if you have 0 Escalated Tasks
        if int(self.week_esc_tasks_1) == 0:
            self.act_escalation_text = "No escalated Task exist"
            self.assertTrue(self.act_escalation_text == self.click_dashboard.return_exception_no_data_escalation_1())
        else:
            escalation_percentage = float(self.week_esc_tasks_1) / float(self.total_total_tasks_1)
            self.act_escalation_percentage_1 = escalation_percentage * 100
            # Grabs 2 decimal places
            self.act_final_escalation_percentage_1 = ("%.2f" % self.act_escalation_percentage_1)
            if self.act_final_escalation_percentage_1.endswith(".00"):
                self.act_final_escalation_percentage_1 = ("%.0f" % float(self.act_final_escalation_percentage_1))
            else:
                self.act_final_escalation_percentage_1 = self.act_final_escalation_percentage_1
            self.act_escalation_text_1 = self.act_final_escalation_percentage_1 + "% Exception"
            self.assertTrue(self.act_escalation_text_1 == self.click_dashboard.return_escalated_previous_percentage())


    #Tests whether the percentage of the escalated percent is correct
    def test_escalated_percent(self):
        self.click_dashboard.click_on_historial_checklist()
        current_date = datetime.today().isoweekday()
        self.total_esc_completed_weekly = []
        self.total_tasks_canduc_weekly = []
        self.total_esc_tasks = []
        self.total_tasks_week = []
        self.final_esc_tasks = []
        self.total_tasks_esc = []
        self.week_esc_tasks = 0
        self.total_total_tasks = 0
        # Begin by going back to Sunday
        for date in range(0, current_date):
            list_of_checklists = self.click_dashboard.return_expand()
            for numbers in list_of_checklists:
                numbers.click()
                self.click_dashboard.wait_for_loader()
                self.total_esc_tasks = self.click_dashboard.return_esc_tasks()
                self.total_tasks_week = self.click_dashboard.return_total_tasks()
            self.final_esc_tasks.append(len(self.total_esc_tasks))
            self.total_tasks_esc.append(len(self.total_tasks_week))
            self.click_dashboard.scroll_up_page()
            self.click_dashboard.click_on_back_calendar()
        self.click_dashboard.click_on_dashboard()
        self.click_dashboard.click_on_historial_checklist()
        self.click_dashboard.click_on_weekly_tasks()
        self.click_dashboard.wait_for_loader()
        list_of_checklists_weekly = self.click_dashboard.return_expand_weekly()
        for numbers in list_of_checklists_weekly:
            numbers.click()
            self.click_dashboard.wait_for_loader()
            self.total_esc_completed_weekly = self.click_dashboard.return_completed_tasks()
            self.total_tasks_canduc_weekly = self.click_dashboard.return_total_tasks()
        if current_date == 7:
            self.final_esc_tasks.append(0)
            self.total_tasks_esc.append(0)
        else:
            self.final_esc_tasks.append(len(self.total_esc_completed_weekly))
            self.total_tasks_esc.append(len(self.total_tasks_canduc_weekly))
        for numbers in range(0, len(self.final_esc_tasks)):
            self.week_esc_tasks = self.week_esc_tasks + int(self.final_esc_tasks[numbers])
        for tasks in range(0, len(self.total_tasks_esc)):
            self.total_total_tasks = self.total_total_tasks + int(self.total_tasks_esc[tasks])
        self.click_dashboard.wait_for_percentages_load()
        self.escalation_percentage = float(self.week_esc_tasks) / float(self.total_total_tasks)
        self.act_escalation_percentage = self.escalation_percentage * 100
        # Grabs 2 decimal places
        self.act_final_escalation_percentage = ("%.2f" % self.act_escalation_percentage)
        if self.act_final_escalation_percentage.endswith(".00"):
            self.act_final_escalation_percentage = ("%.0f" % float(self.act_final_escalation_percentage))
        else:
            self.act_final_escalation_percentage = self.act_final_escalation_percentage
        self.act_escalation_text = self.act_final_escalation_percentage + "% Escalated"
        self.assertTrue(self.act_escalation_text == self.click_dashboard.return_escalated_percentage())

    #Tests whether the previous percentage of the failed temperature percent is correct
    #This won't work if you started a new account and do no have a historical checklist the day before
    def test_previous_temp_failed_percent(self):
        self.click_dashboard.click_on_historial_checklist()
        current_date = datetime.today().isoweekday()
        self.total_weekly_tasks = []
        self.total_temp_tasks_1 = []
        self.final_temp_tasks_1 = []
        self.week_temp_tasks_1 = 0
        #Begin by going back to Sunday
        for date in range(0, current_date):
            self.click_dashboard.click_on_back_calendar()
        #Always grab 7 days as there are 7 days in a week
        for date in range(0,7):
            list_of_checklists_1 = self.click_dashboard.return_expand()
            for numbers in list_of_checklists_1:
                numbers.click()
                self.click_dashboard.wait_for_loader()
                self.total_temp_tasks_1 = self.click_dashboard.return_temp_tasks()
            self.final_temp_tasks_1.append(len(self.total_temp_tasks_1))
            self.click_dashboard.scroll_up_page()
            self.click_dashboard.click_on_back_calendar()
        self.click_dashboard.click_on_dashboard()
        self.click_dashboard.click_on_historial_checklist()
        self.click_dashboard.click_on_weekly_tasks()
        self.click_dashboard.wait_for_loader()
        list_of_checklists_weekly = self.click_dashboard.return_expand_weekly()
        for numbers in list_of_checklists_weekly:
            self.click_dashboard.wait_for_loader()
            numbers.click()
            self.click_dashboard.wait_for_loader()
            self.total_weekly_tasks = self.click_dashboard.return_temp_tasks()
        if current_date == 7:
            self.final_temp_tasks_1.append(0)
        else:
            self.final_temp_tasks_1.append(len(self.total_weekly_tasks))
        for numbers in range(0, len(self.final_temp_tasks_1)):
            self.week_temp_tasks_1 = self.week_temp_tasks_1 + int(self.final_temp_tasks_1[numbers])
        #Always going to have No Failed Temperature Tasks if you have 0 Temperature Tasks
        self.click_dashboard.click_on_dashboard()
        self.exception_value_1 = self.click_dashboard.return_exception_value()
        if self.week_temp_tasks_1 == 0:
            self.act_exception_text = "No Failed Temperature Tasks exist"
            self.assertTrue(self.act_exception_text == self.click_dashboard.return_exception_no_data_1())
        else:
            exception_percentage = float(self.exception_value_1) / float(self.week_temp_tasks_1)
            self.act_exception_percentage_1 = exception_percentage * 100
            #Grabs 2 decimal places
            self.act_final_exception_percentage_1 = ("%.2f" % self.act_exception_percentage_1)
            if self.act_final_exception_percentage_1.endswith(".00"):
                self.act_final_exception_percentage_1 = ("%.0f" % float(self.act_final_exception_percentage_1))
            else:
                self.act_final_exception_percentage_1 = self.act_final_exception_percentage_1
            self.act_exception_text_1 = self.act_final_exception_percentage_1 + "% Exception"
            print(self.act_exception_text_1)
            self.assertTrue(self.act_exception_text_1 == self.click_dashboard.return_exception_previous_percentage())


    #Tests whether the percentage of the failed temperature percent is correct
    def test_temp_failed_percent(self):
        self.click_dashboard.click_on_historial_checklist()
        current_date = datetime.today().isoweekday()
        self.total_temp_tasks = []
        self.final_temp_tasks = []
        self.week_temp_tasks = 0
        for date in range(0,current_date):
            list_of_checklists = self.click_dashboard.return_expand()
            for numbers in list_of_checklists:
                numbers.click()
                self.click_dashboard.wait_for_loader()
                self.total_temp_tasks = self.click_dashboard.return_temp_tasks()
            self.final_temp_tasks.append(len(self.total_temp_tasks))
            self.click_dashboard.scroll_up_page()
            self.click_dashboard.click_on_back_calendar()
        for numbers in range(0, len(self.final_temp_tasks)):
            self.week_temp_tasks = self.week_temp_tasks + int(self.final_temp_tasks[numbers])
        self.click_dashboard.wait_for_percentages_load()
        self.exception_value = self.click_dashboard.return_exception_value()
       # Always going to have No Failed Temperature Tasks if you have 0 Temperature Tasks
        if int(self.week_temp_tasks) == 0:
            self.act_exception_text = "No Failed Temperature Tasks exist"
            self.assertTrue(self.act_exception_text == self.click_dashboard.return_exception_no_data())
        else:
            exception_percentage = float(self.exception_value) / float(self.week_temp_tasks)
            self.act_exception_percentage = exception_percentage * 100
            #Grabs 2 decimal places
            self.act_final_exception_percentage = ("%.2f" % self.act_exception_percentage)
            if self.act_final_exception_percentage.endswith(".00"):
                self.act_final_exception_percentage = ("%.0f" % float(self.act_final_exception_percentage))
            else:
                self.act_final_exception_percentage = self.act_final_exception_percentage
            self.act_exception_text = self.act_final_exception_percentage + "% Exception"
            self.assertTrue(self.act_exception_text == self.click_dashboard.return_exception_percentage())


if __name__ == "__main__":
    unittest.main()



