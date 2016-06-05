# Do not modify this file

import sys
import os
from importlib.machinery import SourceFileLoader
main_path = os.path.dirname(os.path.abspath(__file__))
# User Interface module
ui = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Store module
store = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Human Resources module
hr = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Tool manager module
tool_manager = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Accounting module
accounting = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Selling module
selling = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Customer Relationship Management (CRM) module
crm = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == 1:
        store.start()
    elif option == 2:
        hr.start()
    elif option == 3:
        tool_manager.start()
    elif option == 4:
        accounting.start()
    elif option == 5:
        selling.start()
    elif option == 6:
        crm.start()
    elif option == 0:
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Store manager",
               "Human resources manager",
               "Tool manager",
               "Accounting manager",
               "Selling manager",
               "Customer Relationship Management (CRM)"]

    ui.print_menu("Main menu", options, "Exit program")


def main():
    while True:
        try:
            handle_menu()
        except KeyError as err:
            ui.print_error_message(err)
        # uncomment the next line when you implemented function ui.get_inputs
        # choose()


if __name__ == '__main__':
    main()
