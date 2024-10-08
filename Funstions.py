import re

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "No valid input."
    fname = f_name.title()
    lname = l_name.title()

    return(f"{fname} {lname}")

print(format_name(input(), input()))

