"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
items = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_one_product(items_sold): # посчитать сумму продаж одного товара
    sum_items = 0
    for items in items_sold:
      sum_items += items
    return sum_items

for one_product in items:
    sum_one_product = count_one_product(one_product['items_sold'])
    print(f"Суммарное количество продаж товара {one_product['product']}: {sum_one_product}")

def count_one_product_average(items_sold): # посчитать среднюю сумму продаж одного товара
    sum_items = 0
    for items in items_sold:
      sum_items += items
    scores_avg = sum_items / len(items_sold)
    return scores_avg

for one_product in items:
    sum_one_product_avg = round(count_one_product_average(one_product['items_sold']))
    print(f"Среднее количество продаж товара {one_product['product']}: {sum_one_product_avg}")

avg_product_sum = 0

for one_product in items:
    avg_product_sum += count_one_product(one_product ['items_sold'])

print(f"Cуммарное количество продаж всех товаров: {avg_product_sum}")

product_avg = avg_product_sum / len(items)
print(f"Cреднее количество продаж всех товаров: {product_avg}")
