# Do not modify this file

import sys
import os
from importlib.machinery import SourceFileLoader
main_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Store manager
store = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Human manager
hr = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Inventory manager
tool_manager = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Accounting manager
accounting = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Selling manager
selling = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Customer Relationship Management (CRM)
crm = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()
# Decision Support System (DSS)
dss = SourceFileLoader("module.name", main_path + "/accounting/accounting.py").load_module()


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
    elif option == 7:
        dss.start()
    elif option == 0:
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Selling manager",
               "Customer Relationship Management (CRM)",
               "Decision Support System (DSS)"]

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
