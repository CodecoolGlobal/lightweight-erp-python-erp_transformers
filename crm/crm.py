# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # your code

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):

    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass


# functions supports data analyser
# --------------------------------


def get_name_by_id_(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    # your code

    pass


def get_name_by_id(table, id):

    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    # your code

    pass
