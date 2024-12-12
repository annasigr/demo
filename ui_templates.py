
root_menue_options = {
    "E": "Employee",
    "P": "Property",
    "L": "Location",
    "W": "Work Order",
    "A": "Activity Report, Property",
    "Q": "Quit",
}

table_menue = {
    "R": "Register",
    "C": "Change",
    "S": "Search",
    "B": "Back",
    "Q": "Quit",
}

work_report_menue = {
    "R": "Register Work Report",
    "A": "Approve Work Report",
    "L": "List Work Reports",
    "S": "Search Work Reports",
    "B": "Back",
    "Q": "Quit",
}

ui_root_choices = '\n'.join(f"[{k}]{v[1:]}" for k, v in root_menue_options.items())
ui_table_choices = '\n'.join(f"[{k}]{v[1:]}" for k, v in table_menue.items())
ui_work_report_choices = '\n'.join(f"[{k}]{v[1:]}" for k, v in work_report_menue.items())


separator = "-" * 20

def print_root_menue():
    print(ui_root_choices)
    print()
    print(separator)

def print_table_menue(table):
    print(ui_table_choices)
    print()
    print(separator)
    print("-" * 5, table, "-" * 5)

def print_work_report_menue(table):
    print(ui_work_report_choices)
    print()
    print(separator)
    print("-" * 5, table, "-" * 5)


def display_error(message):
    print(message)

