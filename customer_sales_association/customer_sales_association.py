# data structure:
# sale_id: string -- the id in the sales.csv
# customer_id: string -- the id in the customers.csv

# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    pass


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

    pass


def add(table, sale_id, customer_id):
    """
    Adds the given sale_id - customer_id pair to the table.

    Args:
        table: table to add new record to
        sale_id (str): sale id to add
        customer_id (str): customer id to add

    Returns:
        Table with a new record
    """

    # your code

    return table


def remove(table, sale_id):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id of a record to be removed

    Returns:
        Table without specified record.
    """

    # your code

    return table

# functions supports statistic
# ----------------------------


def get_all_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a set of customer_ids that are present in the table.

     Returns:
         set of customer_ids that are present in the table
    """

    # your code

    pass


def get_all_customer_ids(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): association table between sales and customers

    Returns:
         set of customer_ids that are present in the table
    """

    # your code

    pass


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a set of (customer_id, sale_ids) tuples where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

     Returns:
         (set of tuples (customer_id, (list) sale_ids)) where the sale_ids list in a tuple contains
         all the sales id belong to the given customer_id
    """

    # your code

    pass


def get_all_sales_ids_for_customer_ids(table):
    """
    Returns a set of (customer_id, sale_ids) tuples where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Args:
        table (list of list): association table between sales and customers

    Returns:
         (set of tuples (customer_id, (list) sale_ids)) where the sale_ids list in a tuple contains
         all the sales id belong to the given customer_id
    """

    # your code

    pass


def get_num_of_sales_per_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a set of (customer_id, num_of_sales) tuples where:
        customer_id:
        num_of_sales (number): number of sales the customer made

     Returns:
         set of tuples (customer_id (str), num_of_sales (number))
    """

    # your code

    pass


def get_num_of_sales_per_customer_ids(table):
    """
     Returns a set of (customer_id, num_of_sales) tuples where:
        customer_id:
        num_of_sales (number): number of sales the customer made

     Args:
        table (list of list): association table between sales and customers

     Returns:
         set of tuples (customer_id (str), num_of_sales (number))
    """

    # your code

    pass
