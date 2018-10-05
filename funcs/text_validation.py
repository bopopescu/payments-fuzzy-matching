import re

def valid_sort_code(sort_code):
    if (re.match("^[0-9]{2}[-][0-9]{2}[-][0-9]{2}$|^[0-9]{6}$", sort_code) != None):
        return True
    else:
        return False

def valid_account_number(acc_num):
    if (re.match("^(\d){8}$|0(\d){7}", acc_num) != None):
        return True
    else:
        return False