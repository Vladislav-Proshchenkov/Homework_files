def get_shop_list_by_dishes(dishes, person_count):
    with open('recipes.txt', encoding='utf-8') as shop_list:
        cook_book = {}
        for line in shop_list:
            dish_name = line.strip()
            ingredients_count = int(shop_list.readline().strip())
            ingredients = []
            for i in range(ingredients_count):
                ingredient_name, quantity, measure = shop_list.readline().strip().split('|')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            shop_list.readline    shop_list_by_dishes = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            shop_list_by_dishes[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': ing['quantity']*person_count}
    return shop_list_by_dishes

print(get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 2))
