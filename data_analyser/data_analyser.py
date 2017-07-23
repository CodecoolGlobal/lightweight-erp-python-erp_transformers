# This module creates reports for marketing department.
# This module can run independently from other modules.
# Has no own datastructure but uses other modules.
# Avoud using the database (ie. .csv files) of other modules directly.
# Use the functions of the modules instead.

# todo: importing everything you need

# importing everything you need
import os
import ui
import common
from sales import sales
from crm import crm
from customer_sales_association import customer_sales_association


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


def display_the_last_buyer():
    """
    Displays (prints) the _name_ of the customer made sale last.

    Returns:
        None
    """

    # your code

    pass


def get_the_last_buyer_id():
    """
    Returns the customer id of the customer made sale last.

    Returns:
        Customer id of the last buyer
    """

    # your code

    pass


def display_the_buyer_spent_most_and_the_money_spent():
    """
    Displays the _name_ of the customer who spent more in sum and the money (s)he spent.

    Returns:
        None
    """
    # your code

    pass


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer who spent more in sum and the money (s)he spent.
    Returns a tuple of customer id and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer id and the sum the customer spent
    """

    # your code

    pass


def display_the_most_frequent_buyers_and_their_num_of_sales():
    """
    Gets an input from the user, how many customers they want to see.
    Displays a table with the name of the customers and the number of sales they made.

    Returns:
        None
    """

    # your code

    pass


def get_the_most_frequent_buyers(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent.
    Returns an ordered list of tuples of customer id and the number their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer ids and num of sales
    """

    # your code

    pass
