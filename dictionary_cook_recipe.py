def cook_recipe(recipe_name, pantry):
    recipe = recipes.get(recipe_name)
    if not recipe:
        print(f"Recipe '{recipe_name}' is not fount!")
        return

    for ingredient in recipe:
        if pantry[ingredient] == 0:
            print("Insufficient materals in the panrty!")
            break
        if ingredient in pantry:
            pantry[ingredient] -= 1
        else:
            print(f"Error: ingredient '{ingredient}' not found in the pantry !")
    print(f"Recipe '{recipe_name}' is cooked successfully.")
# Observe the dictionary above and write a menu driven python program to create recipes.
# Once one recipe is done then the quantity of the items in pantry should also be reduced.



def print_pantry(pantry):
    print("pantry: ")
    for item, quantity in pantry.items():
        print(f"{item}: {quantity}")

def print_recipe_menu():
    for index, recipe in enumerate(recipes.keys()):
        print(f"{index + 1}. {recipe}")

pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
    "tin opener": 1,
    "spoon": 10,
}


recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}

while True:
    print_recipe_menu()
    selection = input("Enter the recipe number (q to quit): ")
    if selection == "q":
        break

    try:
        recipe_number = int(selection) - 1
        recipe_name = list(recipes.keys())[recipe_number]

    except (ValueError, IndexError):
        print("Invalid recipe number!")
        continue

    cook_recipe(recipe_name, pantry)
    print_pantry(pantry)