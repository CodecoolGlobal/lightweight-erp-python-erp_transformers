# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string
# amount: number (dollar)
#
# implement these functionalities:
# * module menu like in main.py
# * default functionalities: list, add, remove, update
# * special functionalities


from .. import ui
from .. import data_manager


# start this manager by a menu
def start():

    # you code

    pass


# print the default table of records from the file
def show_table(table):

    # your code

    pass


# Ask a new record as an input from the user than add it to @table, than return @list
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

# the question: In which year was the maximum total of amounts? (2015 or 2016)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average amount in a given year?
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
