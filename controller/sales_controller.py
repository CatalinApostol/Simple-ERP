from model.sales import sales
from view import terminal as view

def list_transactions():
    rezultat=sales.get_sales()
    view.print_table(rezultat)


def add_transaction():
    nume=view.get_input("Add product: ")
    price=int(view.get_input("Add the price of the item:"))
    while price <=0:
        price=int(view.get_input("Add the price of the item: "))
    date1=[]
    zi=int(view.get_input("Enter the date starting with the day: "))
    while zi<=0 or zi>31:
        zi=int(view.get_input("Enter the date starting with the day: "))
    month=int(view.get_input("Enter the month: "))
    while month<=0 or month >12:
         month=int(view.get_input("Enter the month: "))
    year=int(view.get_input("Enter the year: "))
    while year <=1960 or year >2021:
        year=int(view.get_input("Enter the year: "))
    price=str(price)
    date1.append(str(year))
    date1.append("-")
    date1.append(str(month))
    date1.append("-")
    date1.append(str(zi))
    date=''.join(date1)
    product=[]
    product.append(sales.util.generate_id())
    product.append(sales.util.generate_id())
    product.append(nume)
    product.append(price)
    product.append(date)
    
    table=sales.data_manager.read_table_from_file(sales.DATAFILE,separator=';')
    
    table.append(product)
    rezultat=sales.data_manager.write_table_to_file(sales.DATAFILE,table,separator=';')
    list_transactions()


def update_transaction():
    list_transactions()
    table=sales.data_manager.read_table_from_file(sales.DATAFILE,separator=";")
    update=view.get_input("Eneter the ID of the transaction you want to update:")
    date1=[]
    for line in table:
        if line[0] ==update:
            choose=view.get_input("What do you want to update: name/price/date: ")
            if choose == "name":
                name=view.get_input("Enter new name: ")
                line[2] = name
            elif choose == "price":
                price = int(view.get_input("Enter new price: "))
                while price <=0:
                    price = int(view.get_input("Enter new price: "))
                line[3] = str(price)
            elif choose =="date":
                zi=int(view.get_input("Enter the date starting with the day: "))
                while zi<=0 or zi>31:
                    zi=int(view.get_input("Enter the date starting with the day: "))
                month=int(view.get_input("Enter the month:"))
                while month<=0 or month >12:
                    month=int(view.get_input("Enter the month:"))
                year=int(view.get_input("Enter the year: "))
                while year <=1960 or year >2021:
                    year=int(view.get_input("Enter the year:"))
                date1.append(str(year))
                date1.append("-")
                date1.append(str(month))
                date1.append("-")
                date1.append(str(zi))
                date=''.join(date1)
                line[4] = date
    sales.data_manager.write_table_to_file(sales.DATAFILE,table,separator=';')
    list_transactions()


def delete_transaction():
    list_transactions()
    table=sales.data_manager.read_table_from_file(sales.DATAFILE,separator=";")
    del_line=view.get_input("Enter the ID of the transation you want to delete:")
    for i in table:
        if i[0] == del_line:
            table.remove(i)
    sales.data_manager.write_table_to_file(sales.DATAFILE,table,separator=';')
    list_transactions()


def get_biggest_revenue_transaction():
    table=sales.data_manager.read_table_from_file(sales.DATAFILE,separator=";")
    biggest_cashout=0
    index=-1
    for i,line in enumerate(table):
        if float(line[3])>biggest_cashout:
            biggest_cashout=float(line[3])
            index = i
    print('\n')
    view.print_general_results(table[index], 'The transaction that made me the most money is')
    


def get_biggest_revenue_product():
    table=sales.data_manager.read_table_from_file(sales.DATAFILE,separator=";")
    products={}
    for i in range(len(table)):
        if table[i][2] not in products:
            products[table[i][2]]= float(table[i][3])
        else:
            products[table[i][2]]+= float(table[i][3])
    biggest_cashout=0
    index=-1
    for key in products:
        if float(products[key])>biggest_cashout:
            biggest_cashout=float(products[key])
            index = key
    print('\n')
    view.print_general_results((index +' '+str(biggest_cashout)), 'The most sold product and the amount of money it made are')
    
def count_transactions_between():
    list_transactions()
    table=sales.data_manager.read_table_from_file(sales.DATAFILE,separator=";")
    starting_date=input('Enter the starting date (YYYY-MM-DD): ').split('-')
    ending_date=input('Enter the ending date (YYYY-MM-DD): ').split('-')
    count=0
    for i in range(len(table)):
        current_date= table[i][4].split('-')
        if int(current_date[0])< int(starting_date[0]) or int(current_date[0]) > int(ending_date[0]) :
            continue
        elif (int(current_date[0]) == int(starting_date[0]) and int(current_date[1]) < int(starting_date[1])) \
            or  (int(current_date[0]) == int(ending_date[0]) and int(current_date[1]) > int(ending_date[1])):
            continue
        elif (int(current_date[0]) == int(starting_date[0]) and int(current_date[1]) == int(starting_date[1]) and int(current_date[2])< int(starting_date[2])) \
            or (int(current_date[0]) == int(ending_date[0]) and int(current_date[1]) == int(ending_date[1]) and int(current_date[2]) >int(ending_date[2])):
            continue
        else:
            count += 1
    print('\n')
    view.print_general_results(count, 'The number of transactions between the chosen dates is')
            


def sum_transactions_between():
    list_transactions()
    table=sales.data_manager.read_table_from_file(sales.DATAFILE,separator=";")
    starting_date=input('Enter the starting date (YYYY-MM-DD): ').split('-')
    ending_date=input('Enter the ending date (YYYY-MM-DD): ').split('-')
    count=0
    the_sum= 0.0
    for i in range(len(table)):
        current_date= table[i][4].split('-')
        if int(current_date[0])< int(starting_date[0]) or int(current_date[0]) > int(ending_date[0]) :
            continue
        elif (int(current_date[0]) == int(starting_date[0]) and int(current_date[1]) < int(starting_date[1])) \
            or  (int(current_date[0]) == int(ending_date[0]) and int(current_date[1]) > int(ending_date[1])):
            continue
        elif (int(current_date[0]) == int(starting_date[0]) and int(current_date[1]) == int(starting_date[1]) and int(current_date[2])< int(starting_date[2])) \
            or (int(current_date[0]) == int(ending_date[0]) and int(ending_date[1]) == int(ending_date[1]) and int(current_date[2]) >int(ending_date[2])):
            continue
        else:
            the_sum += float(table[i][3])
    print('\n')
    view.print_general_results(the_sum, 'The sum of transactions between the chosen dates is')


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
