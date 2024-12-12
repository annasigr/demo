from ui_class_based_templates import UserMenue, UserMenueItem

# ---------------------------------
# Build the menue system
# ---------------------------------

# Common menue items:
register_item = UserMenueItem(name="Register", action="Register")
change_item = UserMenueItem(name="Change", action="Change")
search_item = UserMenueItem(name="Search", action="Search")
back_item = UserMenueItem(name="Back", action="Back")
quit_item = UserMenueItem(name="Quit", action="Quit")

# Commen menue:
default_menue_items = {
    "R": register_item,
    "C": change_item,
    "S": search_item,
    "B": back_item,
    "Q": quit_item,
}

# ---------------------------------
# The actual user interfaces:

login_menue = UserMenue(
    name="Login",
    choices={
        "U": UserMenueItem(name= "User", action="Root"),
        "M": UserMenueItem(name= "Manager", action="Root"),
        "Q": quit_item,
    }
)

root_menue = UserMenue(
    name="Root",
    choices={
        "E": UserMenueItem(name="Employee", action="DefaultTable"),
        "P": UserMenueItem(name="Property", action="DefaultTable"),
        "L": UserMenueItem(name="Location", action="DefaultTable"),
        "W": UserMenueItem(name="Work Order", action="DefaultTable"),
        "A": UserMenueItem(name="Activity Report, Property", action="WorkReportTable"),
        "Q": quit_item,
    }
)

employee_menue = UserMenue(name="Employee", choices=default_menue_items)

property_menue = UserMenue(name="Property", choices=default_menue_items)

location_menue = UserMenue(name="Location", choices=default_menue_items)

work_order_menue = UserMenue(name="Work Order", choices=default_menue_items)

work_report_menue = UserMenue(
    name="Activity Report, Property",
    choices={
        "R": UserMenueItem(name="Register Work Report", action="Register"),
        "A": UserMenueItem(name="Approve Work Report", action="Approve"),
        "L": UserMenueItem(name="List Work Reports", action="List"),
        "S": UserMenueItem(name="Search Work Reports", action="Search"),
        "B": back_item,
        "Q": quit_item,
    }
)

register_work_report_menue = UserMenue(
    name="Register Work Report",
    choices={
        "N": UserMenueItem(name="New Work Report", action="NewWorkReport"),
        "B": back_item,
        "Q": quit_item,
    }
)

# ---------------------------------
# Usage:

print(login_menue)
print(root_menue)
print(employee_menue)

# ---------------------------------

def get_user_choice(choices):
    choice = ""
    while not choice:
        user_input = input("Choose action: ").strip().upper()
        if user_input in choices:
            return user_input
        else:
            message = f"'{user_input}' is not a valid option. Please try again.."
            display_error(message)
            current_menue = breadcrums.pop()
            if current_menue == "root":
                return root_menue()
            return display_menu(current_menue)

# ---------------------------------

def login():
    print(login_menue)
    user


# ---------------------------------

if __name__ == "__main__":
    login()
