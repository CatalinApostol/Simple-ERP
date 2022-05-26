from model.hr import hr
from view import terminal as view
from model import util as util


def list_employees():
    employee_list = hr.get_employees()
    view.print_table(employee_list)


def add_employee():
    employee_list = hr.data_manager.read_table_from_file(hr.DATAFILE, separator=';')
    name = input("Add name: ")
    date_of_birth = input("Add date of birth: ")
    department = input("Add department: ")
    clearance = input("Add clearance: ")
    
    employee = []
    employee.append(util.generate_id())
    employee.append(name)
    employee.append(date_of_birth)
    employee.append(department)
    employee.append(clearance)
    
    table = hr.data_manager.read_table_from_file(hr.DATAFILE, separator=';')
    
    table.append(employee)
    employee_list = hr.data_manager.write_table_to_file(hr.DATAFILE,table,separator=';')
    list_employees()
    
    
def update_employee():
    list_employees()
    table = hr.data_manager.read_table_from_file(hr.DATAFILE, separator=';')
    update = input("ID you want to update: ")
    for line in table:
        if line[0] == update:
            choose = input("What do you want to update name/date_of_birth/department/clearance: ")
            if choose == "name":
                name = input("Enter new name: ")
                line[1] = name 
            elif choose == "date_of_birth":
                date_of_birth = input("Enter new date_of_birth: ")
                line[2] = date_of_birth
            elif choose == "department":
                department = input("What is the new department?: ")
                line[3] = department
            elif choose == "clearance":
                clearance = input("Provide clearance: ")
                line[4] = clearance

    table = hr.data_manager.write_table_to_file(hr.DATAFILE, table, separator=';')
    list_employees()


def delete_employee():
    employee = hr.data_manager.read_table_from_file(hr.DATAFILE, separator=';')
    list_employees()
    del_line=view.get_input("Enter the ID of the transation you want to delete:")
    for i in employee:
        if i[0] == del_line:
            employee.remove(i)
    hr.data_manager.write_table_to_file(hr.DATAFILE,employee,separator=';')
    list_employees()


def get_oldest_and_youngest():
    employee_list = hr.get_age()
    view.print_table(employee_list)


def get_average_age():
    employee_list=hr.data_manager.read_table_from_file(hr.DATAFILE, separator=';')
    average=0
    count=0
    current_date=input('What day is it today? YYYY-MM-DD : ').split('-')
    for i in range(len(employee_list)):
        age= employee_list[i][2].split('-')
        if age[1] > current_date[1]:
            average += int(current_date[0]) - int(age[0]) -1
            count += 1
        else:
            average += int(current_date[0]) - int(age[0])
            count += 1
    view.print_general_results(int(average/count), 'The average age is')


def next_birthdays():
    employee_list=hr.data_manager.read_table_from_file(hr.DATAFILE, separator=';')
    current_date=input('What day is it today? YYYY-MM-DD: ').split('-')
    next_birthdays=[]
    for i in range(len(employee_list)):
        result=float
        age= employee_list[i][2].split('-')
        result = ((int(age[1])-1) *30 + int(age[2])) - ((int(current_date[1])-1) * 30 + int(current_date[2])) 
        if result <= 14 and result >=0:
            name_bday=[]
            name_bday.append(employee_list[i][1])
            name_bday.append(employee_list[i][2])
            next_birthdays.append(name_bday)
    view.print_general_results(next_birthdays,'The people who have their birthdays coming in 2 weeks are: ')



def count_employees_with_clearance():
    select = input("Clearence: ")
    alist = hr.get_clearence(select)
    view.print_table(alist)


def count_employees_per_department():
    final_list = hr.count_employees()
    view.print_table(final_list)


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)