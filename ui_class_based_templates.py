

class UserMenueItem:
    def __init__(self, name: str, action: str):
        self.name = name
        self.action = action
    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, action={self.action})"
    def __str__(self):
        return f"[]"

class UserMenue:
    def __init__(self, name: str, choices: dict[UserMenueItem]):
        self.name = name
        self.choices = choices
    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, choices={self.choices})"
    def __str__(self):
        menue_string = "{separator}\n{menu_choices}\n{menue_title}".format(
            separator="-" * 20,
            menue_title="-" * 5 + self.name + "-" * 5,
            menu_choices="\n".join(f"[{k}]{v.name[1:]}" for k, v in self.choices.items())
        )
        return menue_string

# Build the menue system:

register_item = UserMenueItem(name="Register", action="Register")
change_item = UserMenueItem(name="Change", action="Change")
search_item = UserMenueItem(name="Search", action="Search")
back_item = UserMenueItem(name="Back", action="Back")
quit_item = UserMenueItem(name="Quit", action="Quit")

default_menue_items = {
    "R": register_item,
    "C": change_item,
    "S": search_item,
    "B": back_item,
    "Q": quit_item,
}

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

