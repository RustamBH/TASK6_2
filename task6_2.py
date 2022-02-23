cook_book = {}

with open('recipes.txt', 'rt') as fp:
    while True:
        dish = fp.readline().strip()
        if len(dish) > 0:
            ingred_num = int(fp.readline().strip())
            recipe_list = []
            for i in range(0, ingred_num):
                recipe_dict = {}
                recipe_str = fp.readline().strip()
                ingred_line = recipe_str.split(' | ')
                recipe_dict['ingredient_name'] = ingred_line[0]
                recipe_dict['quantity'] = int(ingred_line[1])
                recipe_dict['measure'] = ingred_line[2]
                recipe_list.append(recipe_dict)

            cook_book[dish] = recipe_list
            space = fp.readline().strip()
        else:
            break


# print(cook_book)

def get_shop_list_by_dishes(dishes, n_person):
    for dish_one in dishes:
        if dish_one in cook_book:
            for ingr_line in cook_book.get(dish_one):
                if ingr_line.get('ingredient_name') in ingredient_dict:
                    # print(ingredient_dict[ingr_line.get('ingredient_name')].get('quantity'))
                    ingr_measure_dict = {
                        'quantity': ingredient_dict[ingr_line.get('ingredient_name')].get('quantity') + ingr_line.get(
                            'quantity')
                    }
                    ingredient_dict[ingr_line.get('ingredient_name')] = ingr_measure_dict
                else:
                    ingr_measure_dict = {'measure': ingr_line.get('measure'),
                                         'quantity': ingr_line.get('quantity') * n_person}
                    ingredient_dict[ingr_line.get('ingredient_name')] = ingr_measure_dict
        else:
            print(f'{dish_one} - is absent')
    return ingredient_dict


person_count = 1
ingredient_dict = {}
# dishes_ordered = ['Запеченный картофель', 'Омлет']
dishes_ordered = ['Запеченный картофель', 'Запеченный картофель', 'Омлет', 'Омлет', 'Омлет']
# dishes_ordered = ['Омлет', 'Омлет', 'Омлет']
# dishes_ordered = ['Омлет']
print(get_shop_list_by_dishes(dishes_ordered, person_count))
