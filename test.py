# Do not modify this file (if you want to modify anyway, contact a mentor before, who will explain why do not modify)

import unittest
import os
import data_manager
# Store module
from store import store
# Human Resources module
from hr import hr
# Tool manager module
from inventory import inventory
# Accounting module
from accounting import accounting
# Sales module
from sales import sales
# Customer Relationship Management (CRM) module
from crm import crm


def compare_lists(tester, expected_list, result_list):
    for item in result_list:
        tester.assertTrue(item in expected_list)


def get_subscribed_list():
    return ["hv8@qsuotla508.com;Lieselotte Rainey",
            "t1ytt@vpm5xkvn.com;Maude Toll",
            "-cip@jlyzpvm.com;Fawn Lambrecht",
            "38ds7@0733we.com;Phylis Farberanmt",
            "net@bjewwj9.com;Genoveva Dingess",
            "rnh5z@zss4-n3.com;Royce Stager",
            "x0jp9xg4@2zh-j6v9ai6.com;Pierre Cotta",
            "p7zgwk@jszadvjsr.com;Concetta Nussbaum",
            "ixnqwxkgvlppx9@4qt-a5jtsj.com;Missy Stoney",
            "ufvp64.ghw5@r2l3f1.com;Sadye Hession",
            "u6vt7o4@n7a-0t.com;Kanesha Moshier",
            "qq9.-2o1cj2bii@g2fdac.com;Caleb Paschal"]


def get_item_sold_between_dates():
    return [["eH34Ju#&", "Astebreed", 25, 3, 10, 2016],
            ["bH34Ju#&", "Age of Wonders II: The Wizard's Throne", 20, 4, 1, 2016],
            ["vH34Ju#&", "AudioSurf", 23, 6, 2, 2016],
            ["kH35Ju#&", "Age of Empires", 11, 3, 7, 2016]]


def get_count_by_manufacturer_list():
    return {"Ensemble Studios": 4,
            "Edelweiss": 1,
            "Triumph Studios": 5,
            "Dylan Fitterer": 1,
            "Frictional Games": 1,
            "Related Designs, Ubisoft Blue Byte": 1,
            "Remedy Entertainment": 1,
            "Alexander Bruce": 1,
            "Bohemia Interactive": 2,
            "Valve Corporation": 1,
            "Eugen Systems": 1,
            "Innocent Grey": 2,
            "Black Element Software": 1,
            "Cyanide": 1,
            "Jagex": 1,
            "Hooksoft": 1,
            "Reflexive Entertainment": 1,
            "Advance Reality Interactive": 1,
            "Gears for Breakfast": 1,
            "Games Farm": 2}


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


def check_forbidden_list_functions(tester, file_name):
    with open(file_name, "r") as file:
        lines = file.read()
        tester.assertEqual(lines.find("find("), -1)
        tester.assertEqual(lines.find("sort("), -1)
        tester.assertEqual(lines.find("sorted("), -1)
        tester.assertEqual(lines.find("sum("), -1)
        tester.assertEqual(lines.find("count("), -1)
        tester.assertEqual(lines.find("index("), -1)


class CommonTester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "common.py")


class UITester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_list_functions(self, "ui.py")


class AccountingTester(unittest.TestCase):
    data_file = "accounting/items_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "accounting/accounting.py")

    def test_check_burnin_dates(self):
        with open("accounting/accounting.py", "r") as file:
            lines = file.read()
            self.assertEqual(lines.find("2015"), -1)
            self.assertEqual(lines.find("2016"), -1)

    def test_which_year_max(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = accounting.which_year_max(table)
        self.assertEqual(result, 2015)

    def test_avg_amount(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = accounting.avg_amount(table, 2016)
        self.assertEqual(result, 48.125)


class CRMTester(unittest.TestCase):
    data_file = "crm/customers_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "crm/crm.py")

    def test_get_longest_name_id(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = crm.get_longest_name_id(table)
        self.assertEqual(result, "kH14Ju#&")

    def test_get_subscribed_emails(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = get_subscribed_list()
        result = crm.get_subscribed_emails(table)
        compare_lists(self, expected, result)


class HRTester(unittest.TestCase):
    data_file = "hr/persons_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "hr/hr.py")

    def test_check_using_datetime(self):
        with open("hr/hr.py", "r") as file:
            lines = file.read()
            self.assertEqual(lines.find("datetime"), -1)

    def test_get_oldest_person(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = ["Barbara Streisand", "Joey Tribbiani", "Evelin Smile"]
        result = hr.get_oldest_person(table)
        compare_lists(self, expected, result)

    def test_get_persons_closest_to_average(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = ["Jimmy Hendrix"]
        result = hr.get_persons_closest_to_average(table)
        compare_lists(self, expected, result)


class SalesTester(unittest.TestCase):
    data_file = "sales/sales_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "sales/sales.py")

    def test_check_using_datetime(self):
        with open("sales/sales.py", "r") as file:
            lines = file.read()
            self.assertEqual(lines.find("datetime"), -1)

    def test_get_lowest_price_item_id(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = sales.get_lowest_price_item_id(table)
        self.assertEqual(result, "kH35Ju#&")

    def test_get_items_sold_between(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = get_item_sold_between_dates()
        result = sales.get_items_sold_between(table, 2, 12, 2016, 7, 6, 2016)
        compare_lists(self, expected, result)


class StoreTester(unittest.TestCase):
    data_file = "store/games_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "store/store.py")

    def test_get_counts_by_manufacturers(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = get_count_by_manufacturer_list()
        result = store.get_counts_by_manufacturers(table)
        self.assertEqual(result, expected)

    def test_get_average_by_manufacturer(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = store.get_average_by_manufacturer(table, "Ensemble Studios")
        self.assertEqual(result, 12.25)


class InventoryTester(unittest.TestCase):
    data_file = "inventory/inventory_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "inventory/inventory.py")

    def test_get_available_items(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = [["kH34Ju#&", "PlayStation 4", "Sony", 2013, 4], ["jH34Ju#&", "Xbox One", "Microsoft", 2013, 4]]
        result = inventory.get_available_items(table)
        compare_lists(self, expected, result)

    def test_get_average_durability_by_manufacturers(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = {"Sony": 3.5, "Microsoft": 4, "Nintendo": 3.25}
        result = inventory.get_average_durability_by_manufacturers(table)
        self.assertEqual(result, expected)

class DataAnalyserTester(unittest.TestCase):
    def test_forbidden_functions(self):
        check_forbidden_functions(self, "data_analyser/data_analyser.py")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
