value = ' Молоко,Яйца,Сахар,Соль'

def get_list_of_groceries(value):
    for item in value.split(','):
        print(item.strip())


get_list_of_groceries(value)