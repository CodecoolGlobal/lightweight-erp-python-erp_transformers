# Do not modify this file
# run the program (the ERP software) by this file from the terminal from thd root directory of this project


import sys
import os
import ui  # User Interface
from importlib.machinery import SourceFileLoader
# Store module
import store.store
# Human Resources module
import hr.hr
# Tool manager module
import tool_manager.tool_manager
# Accounting module
import accounting.accounting
# Sales module
import selling.selling
# Customer Relationship Management (CRM) module
import crm.crm


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        store.start_module()
    elif option == "2":
        hr.start_module()
    elif option == "3":
        tool_manager.start_module()
    elif option == "4":
        accounting.start_module()
    elif option == "5":
        selling.start_module()
    elif option == "6":
        crm.start_module()
    elif option == "0":
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
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()
