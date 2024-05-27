import csv
def check_user_in_database(login, password, flag, type):
    if flag == "login":
        with open('./logins.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if any(row) and row['Login'] == login and row['Password'] == password and row['Permissions'] == type:
                    return True
            return False
    elif flag == "register":
        with open('./logins.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if any(row) and row['Login'] == login:
                    return True
            return False
        
def parse_value(value):
    if value.isdigit():
        return int(value)
    else:
        return value  