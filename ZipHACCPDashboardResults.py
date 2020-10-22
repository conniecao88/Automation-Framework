import unittest
import os
from HTMLTestRunner import HTMLTestRunner
from Tests.QAServerTests.ZipHACCPTest.ZipHACCPDashTest import HACCP_Dashboard_Test

direct = os.getcwd()


class HACCPDash_Test_Results_Run(unittest.TestCase):
    def test_HACCPDash_Results(self):
        HACCPDash_TestSuite = unittest.TestSuite()
        HACCPDash_TestSuite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(HACCP_Dashboard_Test)
        ])

        outfile = open(direct + "/Zip HACCP Dashboard Test Results.html", "w")

        runner = HTMLTestRunner.HTMLTestRunner(
            stream = outfile,
            title = "Test Results for Zip HACCP",
            description = "Here are all the tests ran for Zip HACCP for the Dashboard Screen")


        runner.run(HACCPDash_TestSuite)

        outfile.close()



