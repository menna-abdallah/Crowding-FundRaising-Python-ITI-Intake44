import re
from datetime import datetime

def is_number(s):
    try:
        s = int (s)
        if s:
            return True
    except ValueError:
        return False

def is_string(s):
    pattern = re.compile("^[a-zA-Z][a-zA-Z0-9 ' ']*$")
    if re.match(pattern, s ):
            return True
    else:
            return False
    
def is_valid_date(date_str, format='%Y-%m-%d'):
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False

def print_project (project):
        print()
        print("Title:", project.title)
        print("Details:", project.details)
        print("Total Target:", project.total_target)
        print("Start Date:", project.start_date.strftime("%Y-%m-%d"))
        print("End Date:", project.end_date.strftime("%Y-%m-%d"))
        print()