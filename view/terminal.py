def print_menu(title, list_options):
    """Prints options in standard menu format like this:
    
    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print('\n')
    print(title+ ' ')
    for x, ele in enumerate(list_options[1:], 1):
        print(x, ele)
    print(0, list_options[0])
    pass


def print_message(message):
    """Prints a single message to the terminal.
    
    Args:
        message: str - the message
    """
    print('\n'+ message)
    pass


def print_general_results(result, label):
    if type(result) is int:
        print(label+ ':' +str(result))
    elif type(result) is float:
        print(label+':'+str(round(result,2)))
    elif type(result) is str:
        print(label+':'+result)
    elif type(result) is list:
        print(label)
        for item in result:
            print(item)
    elif type(result) is dict:
        print(label)
        for key, value in result:
            print(str(key) + ':' +str(value))
    pass


# /--------------------------------\ 32
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \--------------------------------/
def print_table(table):
    length=0
    maxim=[]
    j=0
    print('\n')
    while j < len(table[1]):
        length=0
        for i in range(len(table)):
            if len(table[i][j]) > length:
                length= len(table[i][j])
        maxim.append(length)
        j +=1
    for j in range(len(table[0])):
        for i in range(len(table)):
            while len(table[i][j]) < maxim[j]:
                table[i][j] += ' '
    for j in range(len(table[0])):
        for i in range(len(table)):
            table[i][j]= ' '+ table[i][j] + ' '
            while len(table[i][j]) < maxim[j]:
                table[i][j]= ' '+ table[i][j] + ' '
            maxim[j]=len(table[i][j])
                
    print('/',end='')
    for i in range(len(table[1])):
        if i ==len(table[1])-1:
            print('-'*maxim[i]+'\\')
            continue
        print('-'*maxim[i]+'-', end='')
    for i in range(len(table)):
        for j in range(len(table[i])):
            print('|'+ table[i][j], end='')
        print('|')
        if i== len(table)-1:
            continue
        for i in range(len(table[1])):
            if i ==len(table[1])-1:
                print('|'+'-'*maxim[i]+'|')
                continue
            print('|'+'-'*maxim[i], end='')
    print('\\',end='')
    for i in range(len(table[1])):
        if i ==len(table[1])-1:
            print('-'*maxim[i]+'/')
            continue
        print('-'*maxim[i]+'-', end='')
    pass


def get_input(label):
    return input(label)
    pass


def get_inputs(labels):
    dictionary={}
    i=0
    while True:
        dictionary[input(label)]=i
        i += 1
    pass


def print_error_message(message):
    print(message)
    pass
