""" Common module
implement commonly used functions here
"""

import random

import main

import ui


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    ID_LENGTH = 8
    ID_LIST_INDEX = 0
    generated = ''
    FEW_UNICODE_CHAR = {'!': 33, "'": 39, '0': 48, '9': 57, ':': 58, ';': 59, '@': 64, 'A': 65, 'Z': 90, 'a': 97, 'z': 122}
    # your code
    char_counter_list = [('!', "'"), ('0', '9'), ('A', 'Z'), ('a', 'z'), ('!', "'"), ('0', '9'), ('A', 'Z'), ('a', 'z')]
    special_id_list_in_file = [row[ID_LIST_INDEX] for row in table]
    char_counter = 0
    for special_char_id in range(ID_LENGTH):
        first_char_in_group, last_char_in_group = char_counter_list[char_counter][0], char_counter_list[char_counter][1]
        special_char_id = chr(random.randint(FEW_UNICODE_CHAR[first_char_in_group], FEW_UNICODE_CHAR[last_char_in_group]))
        generated += special_char_id
        char_counter += 1
    if generated in special_id_list_in_file:
        generate_random(table)
    return generated


def sub_menu(dict_menu, options, title):
    while True:
        ui.print_menu(title, options, 'Back to main menu: ')
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option in dict_menu.keys():
                dict_menu[option]()
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
        except KeyError as err:
            ui.print_error_message(str(err))
