""" Customer Relationship Management (CRM) module
Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def get_customers():
    result = data_manager.read_table_from_file(DATAFILE)
    return [HEADERS] + result


# def write_customer(customer):
#     file = open(DATAFILE, 'a')
#     final = ";".join(customer)
#     file.write("\n" + final)


def delete_customer(selected_unit):
    with open(DATAFILE, 'r') as file:
        lines = file.read().splitlines()
    with open(DATAFILE, 'w') as file:
        for index,ele in enumerate(lines):
            if selected_unit != index :
                file.write(ele+'\n')


def get_emails(sub):
    resulting_list =[]
    with open(DATAFILE, 'r') as file:
        lines = file.read().splitlines()
        for ele in lines:
            position = ele.split(";")
            if str(sub) in position[3] :
                resulting_list.append(position)
    if len(resulting_list) == 0:
            return [HEADERS] + [["0","0","0","0"]]
    else:
        return [HEADERS] + resulting_list