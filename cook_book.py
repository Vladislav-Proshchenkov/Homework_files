with open('recipes.txt', encoding='utf-8') as recipe_dictionary:
    cook_book = {}
    for line in recipe_dictionary:
        dish_name = line.strip()
        ingredients_count = int(recipe_dictionary.readline().strip())
        ingredients = []
        for i in range(ingredients_count):
            ingredient_name, quantity, measure = recipe_dictionary.readline().strip().split('|')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        recipe_dictionary.readline()
        cook_book[dish_name] = ingredients

print(cook_book)