from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    clean_list = set(dish_ingredients)
    return dish_name, clean_list
    #set1= set()
    #for item in dish_ingredients:
        #set1.add(item)
        #return dish_name, set1



def check_drinks(drink_name, drink_ingredients):
    clean_list = set(drink_ingredients)
    from sets_categories_data import ALCOHOLS
    if clean_list.intersection(ALCOHOLS):
        drink_name = (f"{drink_name} Cocktail")
        return drink_name
    else:
        drink_name = (f"{drink_name} Mocktail")
        return drink_name

