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


def evaluate_groceries(grocery_list):
    for index, name in enumerate(grocery_list):
        print(index + 1, name['name'])


evaluate_groceries(grocery_list)

