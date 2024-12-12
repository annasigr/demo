from ui_templates import print_root_menue, print_table_menue, display_error, root_menue_options, table_menue, work_report_menue, print_work_report_menue


breadcrums = []

def get_user_input(valid_options) -> str:
    """Get the user's selection."""
    user = ""
    while user != "Q":
        user = input("Choose.. ").strip().upper()
        if user in valid_options:
            return user
        else:
            message = f"'{user}' is not a valid option. Please try again.."
            display_error(message)
            current_menue = breadcrums.pop()
            if current_menue == "root":
                return root_menue()
            return display_menu(current_menue)

def backing_handler():
    if len(breadcrums) < 2:
        return root_menue()
    _ = breadcrums.pop()   # current_menue
    last_menue = breadcrums.pop()
    if last_menue == "root":
        return root_menue()
    return display_menu(last_menue)

def root_menue():
    breadcrums.append("root")
    valid_options = root_menue_options
    print_root_menue()
    choice = get_user_input(valid_options.keys())
    if choice == "Q":
        return quiting()
    display_menu(valid_options[choice])

def display_menu(table):
    breadcrums.append(table)
    if table == "Activity Report, Property":
        menue = work_report_menue
        print_work_report_menue(table)
    else:
        menue = table_menue
        print_table_menue(table)
    choice = get_user_input(menue.keys())
    if choice == "Q":
        return quiting()
    if choice == "B":
        return backing_handler()
    return display_menu(menue[choice])

def quiting():
    print("\nChuck Norris is closing the program... you don't need to do anything.\n")


if __name__ == "__main__":
    root_menue()
