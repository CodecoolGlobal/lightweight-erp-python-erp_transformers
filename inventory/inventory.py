""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
                'get available items',
                'get_average_durability_by_manufacturers']
    dict_menu = {'1': show_table_wrapper,
                '2': add_wrapper,
                '3': remove_wrapper,
                '4': update_wrapper,
                '5': get_available_items_wrapper,
                '6': get_average_durability_by_manufacturers_wrapper}
    common.sub_menu(dict_menu, options, "Inventory menu")
    # your code

def show_table_wrapper():
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    show_table(table)


def add_wrapper():
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    add(table)


def remove_wrapper():
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    remove(table, ui.get_inputs(['ID :'], 'Enter ID: '))


def update_wrapper():
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    update(table, ui.get_inputs(['ID :'], 'Enter ID: '))


def get_available_items_wrapper():
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    get_available_items_wrapper(table)


def get_average_durability_by_manufacturers_wrapper():
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    get_average_durability_by_manufacturers(table, ui.get_inputs(['Manufacturer'], 'Enter manufacturer: '))

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    titles_list = ['id: ', 'name: ', 'manufacturer: ', 'purchase_year: ', 'durability: ']
    ui.print_table(table, titles_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    ID_INDEX = 0
    record = ui.get_inputs(['name: ', 'manufacturer: ', 'purchase_year: ', 'durability: '], "Please insert data: ")
    record.insert(ID_INDEX, common.generate_random(table))
    print(record)
    table.append(record)
    data_manager.write_table_to_file('inventory/inventory.csv', table)
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

    ID_LIST_INDEX = 0
    for row in table:
        if row[ID_LIST_INDEX] == id_[ID_LIST_INDEX]:
            table.remove(row)
    data_manager.write_table_to_file('inventory/inventory.csv', table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    ID_LIST_INDEX = 0
    iterate = 0
    for row in table:
        if row[ID_LIST_INDEX] == id_[ID_LIST_INDEX]:
            updated_record = ui.get_inputs(['id: ', 'name: ', 'manufacturer: ', 'purchase_year: ', 'durability: '], row)
            table[iterate] = updated_record
            data_manager.write_table_to_file('inventory/inventory.csv', table)
            break
        iterate += 1
    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
