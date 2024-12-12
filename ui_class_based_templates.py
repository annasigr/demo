
# Classes for the presentaiont of the user interface

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
    
    
