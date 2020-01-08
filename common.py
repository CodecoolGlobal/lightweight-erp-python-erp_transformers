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

    generated = ''

    # your code

    return generated


def sub_menu(spec_func_1, spec_func_2, options):
    while True:
        ui.print_menu('Store menu', options, 'Back to main menu: ')
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                remove(table, id_)
            elif option == "4":
                update(table, id_)
            elif option == "5":
                spec_func_1
            elif option == "6":
                spec_func_2
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
        except KeyError as err:
            ui.print_error_message(str(err))
