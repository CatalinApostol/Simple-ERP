""" Human resources (HR) module
Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util


DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def get_employees():
    result = data_manager.read_table_from_file(DATAFILE)
    return [HEADERS] + result


# def write_employees(position):
#     file = open(DATAFILE, 'a')
#     final = ';'.join(position)
#     file.write("\n" + final)
    
    
# def delete_employees(selected_unit):
#     with open(DATAFILE, 'r') as file:
#         lines = file.readlines()
#     with open(DATAFILE, 'w') as file2:
#         for index in enumerate(lines):
#             if selected_unit != index[0] :
#                 file2.write(index[1])


def get_clearence(sub):
    final_list = [] 
    with open (DATAFILE, 'r') as file:
        lines = file.read().splitlines()
        for ele in lines:
            position = ele.split(";")
            if str(sub) in position[4]:
                final_list.append(position)
    if len(final_list) == 0:
        return [HEADERS] + [["0","0","0","0","0"]]
    else:
        return [HEADERS] + final_list

    
def get_age():
    maximum = []
    minimum = []
    result = []
    templist = []
    with open(DATAFILE, 'r') as file:
        lines = file.read().splitlines()
        for ele in lines:
            position = ele.split(";")
            templist.append(position[2])
        maximum.append(str(max(templist)))
        minimum.append(str(min(templist)))


    with open(DATAFILE, 'r') as file:
        lines = file.read().splitlines()
    for ele in lines:
        position = ele.split(";")
        if str(maximum[0]) in position[2]:
            result.append(position)
        if str(minimum[0]) in position[2]:
            result.append(position)
    
    return [HEADERS] + result


def count_employees():
    department_list = []
    departaments = []
    result = []
    with open(DATAFILE, 'r') as file:
        lines = file.read().splitlines()
        for ele in lines:
            position  = ele.split(";")
            department_list.append(position[3])
    for x in department_list:
        if str(x) not in departaments:
            departaments.append(str(x))
    for ele in departaments:
        occurrences = department_list.count(ele)
        result.append(str(occurrences))
    return [departaments, result]