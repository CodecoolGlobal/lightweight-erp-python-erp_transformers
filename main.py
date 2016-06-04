# Do not modify this file

import os
import sys
import ui           # User interface module
import store        # Store manager
import hr           # Human manager
import inventory    # Inventory manager
import accounting   # Accounting manager
import selling      # Selling manager
import crm          # Customer Relationship Management (CRM)
import dss          # Decision Support System (DSS)


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == 1:
        store.start()
    elif option == 2:
        hr.start()
    elif option == 3:
        inventory.start()
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
