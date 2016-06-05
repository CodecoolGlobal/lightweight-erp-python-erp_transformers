import unittest
import os
from importlib.machinery import SourceFileLoader
main_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Store manager
store = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Human manager
hr = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Inventory manager
tool_manager = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Accounting manager
accounting = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Selling manager
selling = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Customer Relationship Management (CRM)
crm = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Decision Support System (DSS)
dss = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()


def check_forbidden_functions(tester, file_name):
    with open(file_name, "r") as file:
        lines = file.read()
        tester.assertEqual(lines.find("find("), -1)
        tester.assertEqual(lines.find("sort("), -1)
        tester.assertEqual(lines.find("sorted("), -1)
        tester.assertEqual(lines.find("sum("), -1)
        tester.assertEqual(lines.find("count("), -1)
        tester.assertEqual(lines.find("index("), -1)
        tester.assertEqual(lines.find("print("), -1)
        tester.assertEqual(lines.find("input("), -1)


class AccountingTester(unittest.TestCase):
    data_file = "accounting/items_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "accounting/accounting.py")


class CRMTester(unittest.TestCase):
    data_file = "crm/customer_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "crm/crm.py")


class HRTester(unittest.TestCase):
    data_file = "hr/persons_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "hr/hr.py")


class SellingTester(unittest.TestCase):
    data_file = "selling/sellings_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "selling/selling.py")


class StoreTester(unittest.TestCase):
    data_file = "store/games_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "store/store.py")


class ToolManagerTester(unittest.TestCase):
    data_file = "tool_manager/tools_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "tool_manager/tool_manager.py")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
