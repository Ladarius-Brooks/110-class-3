import os

def print_menu():
    print("-" * 30)
    print("Warehouse control")
    print("-" * 30)

    print('[1] Register new Item')
    print('[2] Display catalog')
    print('[3] Display items OOS')
    print('[4] Stock value')
    print('[5] Update item price')
    print('[6] Delete item') # homework

    print('[x] Close')

def clear():
    command = 'clear'
    if(os.name == 'nt'): # nt is the windows os  #os means operating system it must be imported
        command = 'cls'
    return os.system(command)



def print_item(item):
    print(
        str(item.id).ljust(3) 
        + " | " + item.title.ljust(15) 
        + " | " + item.category.ljust(15) 
        + " | " + str(item.stock).rjust(5) 
        + " | " + str(item.price).rjust(7)
    )

#  rjust(#)         |        ljust(#)


def print_header(title):
    clear()
    print("-" * 50)
    print(title)
    print("-" * 50)
