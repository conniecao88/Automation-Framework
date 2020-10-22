import unittest
import os
from HTMLTestRunner import HTMLTestRunner
from Tests.QAServerTests.ZipInventoryApplicationTest.ZipInventoryTransferTest import Transfer_Test
#import Tests.QAServerTests.QAServerLoginTest
#import Tests.QAServerTests.QAServerOrganizationTest
#import Tests.QAServerTests.ZipInventoryApplicationTest.ZipInventoryApplicationDashboardTest
#import Tests.QAServerTests.ZipInventoryApplicationTest.ZipInventoryCreditMemoTest
direct = os.getcwd()


class QaLoginResults(unittest.TestCase):
    def testLoginResultsforQA(self):
        testLogQA_Results = unittest.TestSuite()
        testLogQA_Results.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Transfer_Test)
        ])

        outfile = open(direct + "/QA_Results.html", "w")

        runner = HTMLTestRunner.HTMLTestRunner(
            stream = outfile,
            title = "QA Tests Results",
            description = "QA Results"
        )

        runner.run(testLogQA_Results)

        outfile.close()


if __name__ == "__main__":
    unittest.main()