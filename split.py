lol = 'Молоко,Яйца,Сахар,Соль'

def get_list_of_groceries(lol):
    nlol = lol.split(',')
    for element in nlol:
        print(element)

get_list_of_groceries(lol)