# Исходные данные
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
# Пишем функцию по поиску общей выручки. Инициализируем переменную total и через цикл суммируем в нее результат
# каждой итерации.
def total_revenue(purchases):
    total = 0
    for i in purchases:
        total += i['price'] * i['quantity']
    return total

# Пишем функцию, которая возвращает cписок товаров по категориям.
def items_by_category(purchases):
    my_dict = {} # создаем словарь в который будем добавлять категории с товарами
    for i in purchases: # запускаем цикл для извлечения категорий и товаров
        category = i['category']
        item = i['item']
        if category not in my_dict: # проверяем если категории нет в нашем новом списке, добавляем ее с пустым списком,
            # в который будем добавлять товары
            my_dict[category] = []
        my_dict[category].append(item) # добавляем товары
    return my_dict # выводим наш новый список

# Пишем функцию, которая выводит список покупок, где цена за товар больше заданного значения, пусть это значение будет 1
def expensive_purchases(purchases, min_price):
    return list(filter(lambda x: x['price'] >= min_price, purchases)) # фильтруем наш исходный список и возвращаем новый

# Пишем функцию, которая находит среднюю цену товаров по категориям.
def average_price_by_category(purchases):
    my_dict2 = {} # создаем словарь в который будем добавлять категории с ценами
    for i in purchases: # запускаем цикл для извлечения категорий и цен
        category = i['category']
        price = i['price']
        if category not in my_dict2: # проверяем если категории нет в нашем новом списке, добавляем ее с пустым списком,
            # в который будем добавлять цены
            my_dict2[category] = []
        my_dict2[category].append(price) # добавляем цены
    for i in my_dict2: # еще раз запускаем цикл, но уже по новому списку, чтобы найти среднюю цену
        price = my_dict2[i] # извлекаем список цен
        my_dict2[i] = sum(price) / len(price) if price else 0 # находим среднее
    return my_dict2 # возвращаем результат

# Пишем функцию, которая находит категория с наибольшим числом проданных товаров.
def most_frequent_category(purchases):
    purchases1 = sorted(purchases, key=lambda x: x['quantity']) # сортируем наш исходный список
    # по возрастанию кол-ва товаров
    return purchases1[-1]['category'] # возвращаем последнее значение сортированного списка

# Выводим результаты
print(f'''Общая выручка: {total_revenue(purchases)}
Товары по категориям: {items_by_category(purchases)}
Покупки дороже 1.0: {expensive_purchases(purchases, min_price=1)}
Средняя цена по категориям: {average_price_by_category(purchases)}
Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}
''')