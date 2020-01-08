""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ['show table',
                'add',
                'remove',
                'update',
                'get count by manufacturers',
                'get average by manufacturer']
    dict_menu = {'1': show_table_wrapper,
                '2': add_wrapper,
                '3': remove_wrapper,
                '4': update_wrapper,
                '5': get_counts_by_manufacturers_wrapper,
                '6': get_average_by_manufacturer_wrapper}
    common.sub_menu(dict_menu, options, "Store menu")


def show_table_wrapper():
    table = data_manager.get_table_from_file('store/games.csv')
    show_table(table)


def add_wrapper():
    table = data_manager.get_table_from_file('store/games.csv')
    add(table)


def remove_wrapper():
    table = data_manager.get_table_from_file('store/games.csv')
    remove(table, ui.get_inputs(['ID'], 'Enter ID: '))


def update_wrapper():
    table = data_manager.get_table_from_file('store/games.csv')
    update(table, ui.get_inputs(['ID'], 'Enter ID: '))


def get_counts_by_manufacturers_wrapper():
    table = data_manager.get_table_from_file('store/games.csv')
    get_counts_by_manufacturers(table)


def get_average_by_manufacturer_wrapper():
    table = data_manager.get_table_from_file('store/games.csv')
    get_average_by_manufacturer(table, ui.get_inputs(['Manufacturer'], 'Enter manufacturer: '))


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table,'Store')


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    ID = 0
    line_counter = 0
    for row in table:
        if row[ID] == id_[ID]:
            table.remove(row)
        line_counter += 1
    data_manager.write_table_to_file('store/games.csv', table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    # your code
