# Do not modify this file (if you want to modify anyway, contact a mentor before, who will explain why do not modify)

from test import *

# Data Analyser module
from data_analyser import data_analyser


class DataAnalyserTester(unittest.TestCase):
    def test_forbidden_functions(self):
        check_forbidden_functions(self, "data_analyser/data_analyser.py")


class Week2CRMTester(unittest.TestCase):
    data_file = "crm/customers_test.csv"

    def test_week2_crm_get_name_by_id(self):
        self.assertEqual(crm.get_name_by_id("kH94Jc#&"), "Daniele Coach")
        self.assertEqual(crm.get_name_by_id("kP94Jc#&"), None)

    def test_week2_crm_get_name_by_id_from_table(self):
        table = data_manager.get_table_from_file(self.data_file)
        self.assertEqual(crm.get_name_by_id_from_table(table, "kH94Jc#&"), "Daniele Coach")
        self.assertEqual(crm.get_name_by_id_from_table(table, "kP94Jc#&"), None)


class Week2SalesTester(unittest.TestCase):
    data_file = "sales/sales_test.csv"

    def test_week2_sales_get_title_by_id(self):
        result = sales.get_title_by_id("kH35Ju#&")
        expected = "Age of Empires"
        self.assertEqual(result, expected)

        result = sales.get_title_by_id("PH35Ju#&")
        expected = None
        self.assertEqual(result, expected)

    def test_week2_sales_get_title_by_id_from_table(self):
        table = data_manager.get_table_from_file(self.data_file)

        result = sales.get_title_by_id_from_table(table, "kH35Ju#&")
        expected = "Age of Empires"
        self.assertEqual(result, expected)

        result = sales.get_title_by_id_from_table(table, "PH35Ju#&")
        expected = None
        self.assertEqual(result, expected)

    def test_week2_sales_get_item_id_sold_last(self):
        result = sales.get_item_id_sold_last()
        expected = "kH34Ju#&"
        self.assertEqual(result, expected)

    def test_week2_sales_get_item_id_sold_last_from_table(self):
        table = data_manager.get_table_from_file(self.data_file)

        result = sales.get_item_id_sold_last_from_table(table)
        expected = "kH34Ju#&"
        self.assertEqual(result, expected)


    def test_week2_sales_get_the_sum_of_prices(self):
        item_ids = ["kH34Ju#&", "jH34Ju#&", "tH34Ju#&", "eH34Ju#&"]
        result = sales.get_the_sum_of_prices(item_ids)
        expected = 127
        self.assertEqual(result, expected)

    def test_week2_sales_get_the_sum_of_prices_from_table(self):
        table = data_manager.get_table_from_file(self.data_file)
        item_ids = ["kH34Ju#&", "jH34Ju#&", "tH34Ju#&", "eH34Ju#&"]
        result = sales.get_the_sum_of_prices_from_table(table, item_ids)
        expected = 127
        self.assertEqual(result, expected)

    def test_week2_sales_get_customer_id_by_sale_id(self):
        result = sales.get_customer_id_by_sale_id("kH38Je#&")
        expected = "kH14Jt#&"
        self.assertEqual(result, expected)

    def test_week2_sales_get_customer_id_by_sale_id_from_table(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = sales.get_customer_id_by_sale_id_from_table(table, "kH38Je#&")
        expected = "kH14Jt#&"
        self.assertEqual(result, expected)

    def test_week2_sales_get_all_customer_ids(self):
        result = sales.get_all_customer_ids()
        expected = {"jH34Jk#&", "kH14Jt#&", "kH14Jh#&"}
        self.assertEqual(result, expected)

    def test_week2_sales_get_all_customer_ids_from_table(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = sales.get_all_customer_ids_from_table(table)
        expected = {"jH34Jk#&", "kH14Jt#&", "kH14Jh#&"}
        self.assertEqual(result, expected)

    def test_week2_sales_get_all_sales_ids_for_customer_ids(self):
        result = sales.get_all_sales_ids_for_customer_ids()
        expected = {"jH34Jk#&": ["kH34Ju#&", "jH34Ju#&", "tH34Ju#&", "eH34Ju#&", "kH14Ju#&", "kH35Ju#&", "kH38Ju#&",
                                 "kH94Ju#&", "tH34Jl#&", "eH34Jy#&", "bH34Jx#&"],
                    "kH14Jt#&": ["bH34Ju#&", "vH34Ju#&", "kH34Ji#&", "vH34Jz#&", "kH14Jt#&", "kH35Jr#&", "kH38Je#&",
                                 "kH94Jw#&"],
                    "kH14Jh#&": ["jH34Jk#&"]}
        self.assertEqual(result, expected)

    def test_week2_sales_get_all_sales_ids_for_customer_ids_from_table(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = sales.get_all_sales_ids_for_customer_ids_from_table(table)
        expected = {"jH34Jk#&": ["kH34Ju#&", "jH34Ju#&", "tH34Ju#&", "eH34Ju#&", "kH14Ju#&", "kH35Ju#&", "kH38Ju#&",
                                 "kH94Ju#&", "tH34Jl#&", "eH34Jy#&", "bH34Jx#&"],
                    "kH14Jt#&": ["bH34Ju#&", "vH34Ju#&", "kH34Ji#&", "vH34Jz#&", "kH14Jt#&", "kH35Jr#&", "kH38Je#&",
                                 "kH94Jw#&"],
                    "kH14Jh#&": ["jH34Jk#&"]}
        self.assertEqual(result, expected)

    def test_week2_sales_get_num_of_sales_per_customer_ids(self):
        result = sales.get_num_of_sales_per_customer_ids()
        expected = {"jH34Jk#&": 11, "kH14Jt#&": 8, "kH14Jh#&": 1}
        self.assertEqual(result, expected)

    def test_week2_sales_get_num_of_sales_per_customer_ids_from_table(self):
        table = data_manager.get_table_from_file(self.data_file)

        result = sales.get_num_of_sales_per_customer_ids_from_table(table)
        expected = {"jH34Jk#&": 11, "kH14Jt#&": 8, "kH14Jh#&": 1}
        self.assertEqual(result, expected)


class Week2DataAnalyserTester(unittest.TestCase):

    def test_week2_data_analyser_get_the_last_buyer_name(self):
        result = data_analyser.get_the_last_buyer_name()
        expected = "Missy Stoney"
        self.assertEqual(result, expected)

    def test_week2_data_analyser_get_the_last_buyer_id(self):
        result = data_analyser.get_the_last_buyer_id()
        expected = "jH34Jk#&"
        self.assertEqual(result, expected)

    def test_week2_data_analyser_get_the_buyer_name_spent_most_and_the_money_spent(self):
        result = data_analyser.get_the_buyer_name_spent_most_and_the_money_spent()
        expected = ("Missy Stoney", 434)
        self.assertEqual(result, expected)

    def test_week2_data_analyser_get_the_buyer_id_spent_most_and_the_money_spent(self):
        result = data_analyser.get_the_buyer_id_spent_most_and_the_money_spent()
        expected = ("jH34Jk#&", 434)
        self.assertEqual(result, expected)

    def test_week2_data_analyser_get_the_most_frequent_buyers_names(self):
        result = data_analyser.get_the_most_frequent_buyers_names(1)
        expected = [("Missy Stoney", 11)]
        self.assertEqual(result, expected)

        result = data_analyser.get_the_most_frequent_buyers_names(2)
        expected = [("Missy Stoney", 11), ("Sadye Hession", 8)]
        self.assertEqual(result, expected)

    def test_week2_data_analyser_get_the_most_frequent_buyers_ids(self):
        result = data_analyser.get_the_most_frequent_buyers_ids(1)
        expected = [("jH34Jk#&", 11)]
        self.assertEqual(result, expected)

        result = data_analyser.get_the_most_frequent_buyers_ids(2)
        expected = [("jH34Jk#&", 11), ("kH14Jt#&", 8)]
        self.assertEqual(result, expected)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
