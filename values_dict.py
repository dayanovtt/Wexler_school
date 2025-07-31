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

def get_sum(grocery_list):
    total = 0
    for grocery in grocery_list:
        total += grocery['price']


get_sum(grocery_list)