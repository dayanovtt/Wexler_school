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
    for grocery in grocery_list:
        print(grocery['name'])

show_groceries(grocery_list)