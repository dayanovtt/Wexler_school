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
    for grocery in range(len(grocery_list)):
        print(grocery + 1, grocery_list[grocery]['name'])


evaluate_groceries(grocery_list)