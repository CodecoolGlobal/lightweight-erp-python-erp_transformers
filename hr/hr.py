# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("module.name", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("module.name", current_file_path + "/../data_manager.py").load_module()


# start this manager by a menu
def start_module():

    # you code

    pass


# print the default table of records from the file
def show_table(table):

    # your code

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
