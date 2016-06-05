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


class AccountingTester(unittest.TestCase):
    points = 0
    input_file = "game_stat.txt"

    def test_1_count_games(self):
        result = accounting.count_games(self.input_file)
        self.assertEqual(result, 24)
        if result == 24:
            self.points += 2
            print("Function 'count_games' is passed.")


def main():
    unittest.main()

if __name__ == '__main__':
    main()