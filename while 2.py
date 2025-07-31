grocery_list = [
    {'name': 'Сметана',
     'price': 50},
    {'name': 'Кофе',
     'price': 150},
    {'name': 'Торт',
     'price': 500},
    {'name': 'Пиво',
     'price': 90},
]

def show_groceries(grocery_list):

    index = 0
    while index < len(grocery_list):
        print(grocery_list[index]['name'])
        index += 1

show_groceries(grocery_list)