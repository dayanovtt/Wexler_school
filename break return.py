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


def check_item_in_list(grocery_list, item):
    for i in grocery_list:
        if i['name'] == item:
            print(i['name'])
            break
    else:
        print(f"Продукта {item} нет в списке")


check_item_in_list(grocery_list, 'Коф')