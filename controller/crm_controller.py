from model.crm import crm as crm
from view import terminal as view
from model import util as util

def list_customers():
    customers_list = crm.get_customers()
    view.print_table(customers_list)


def add_customer():
    customers_list = crm.data_manager.read_table_from_file(crm.DATAFILE)
    list_customers()
    name = input("Add name: ")
    email = input("Add email: ")
    subscription = input("""Would you like to get a subscription?
                            <> 1 for yes <>
                            <> 0 for no  <>
                            >>> """)
    if subscription!='1' and subscription !='0':
        subscription='0'
    
    customer = []
    customer.append(util.generate_id())
    customer.append(name)
    customer.append(email)
    customer.append(subscription)
    customers_list.append(customer)
    customers_list = crm.data_manager.write_table_to_file(crm.DATAFILE,customers_list, separator=';')

    list_customers()
        

def update_customer():
    list_customers()
    table = crm.data_manager.read_table_from_file(crm.DATAFILE, separator=';')
    update = input("ID you want to update: ")
    for line in table:
        if line[0] == update:
            choose = input("What do you want to update name/email/subscription: ")
            if choose == "name":
                name = input("Enter new name: ")
                line[1] = name 
            elif choose == "email":
                email = input("Enter new email: ")
                line[2] = email
            elif choose == "subscription":
                subscription = input("""Would you like to get a subscription?
                                     <> 1 for yes <>
                                     <> 0 for no  <>
                                     >>> """)
                if subscription != "1" and subscription!='0':
                    subscription = '0'
                line[3]= subscription
    
    table = crm.data_manager.write_table_to_file(crm.DATAFILE, table, separator=';')
    list_customers()
            

def delete_customer():
    customer = crm.data_manager.read_table_from_file(crm.DATAFILE, separator=';')
    select_id = input("Id to be deleted: ")
    selected_unit = 0
    for ele in customer:
        if select_id == ele[0]:
            break
        else:
            selected_unit += 1
    crm.delete_customer(selected_unit)
    list_customers()

def get_subscribed_emails():
    customers_list_subscribed = crm.get_emails(sub=1)
    view.print_table(customers_list_subscribed)
    


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)