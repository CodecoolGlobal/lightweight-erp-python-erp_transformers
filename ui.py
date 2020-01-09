""" User Interface (UI) module """
import data_manager

def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    dash_char = "-"
    max_len_column = [0,0,0,0,0,0,0]
    column_counter = 0

    #maximum length of every element in title data base (max_len_column)
    for rows in title_list:
        if len(rows) > max_len_column[column_counter]:
            max_len_column[column_counter] = len(rows)
            column_counter += 1

    #maximum Length of every row in table data base. (max_len_column)
    for rows in table:
        column_counter = 0
        for column in rows:
            if len(column) > max_len_column[column_counter]:
                max_len_column[column_counter] = len(column)
            column_counter += 1

    #header
    print("/",end = '')
    counter = 0
    for i in max_len_column:
        if i != 0:
            counter += 1
            if counter == len(title_list):
                print(f"{dash_char * (i + 1)}\\",end = '')
            else:
                print(f"{dash_char * (i + 1)}|",end = '')
    print("")


    #title
    counter = 0
    for title in title_list:
        print(f'| {title.center(max_len_column[counter])}', end = "")
        counter += 1
    print("|")

    #data
    for rows in table:
        counter = 0
        for i in max_len_column:
            if i != 0:
                print(f"|{dash_char * (i + 1)}", end = '')
        print("|")
        for column in rows:
            print(f"| {column.center(max_len_column[counter])}", end = "")
            counter += 1
        print('|')

    #footer
    print("\\",end = '')
    counter = 0
    for i in max_len_column:
        if i != 0:
            counter += 1
            if counter == len(title_list):
                print(f"{dash_char * (i + 1)}/",end = '')
            else:
                print(f"{dash_char * (i + 1)}|",end = '')


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f'\n{title}: ')
    options_counter = 1
    for option in list_options:
        print(f'({options_counter}) {option}')
        options_counter += 1
    print(f'(0) {exit_message}')


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(f'{title}')
    for label in list_labels:
        get_input = input(label)
        inputs.append(get_input)
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f'{message}')
