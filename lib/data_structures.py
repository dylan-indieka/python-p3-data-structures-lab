spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # Return a list of names from the spicy_foods list
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # Return foods with heat_level > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # Print each food formatted with 🌶 emojis
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Return the first food that matches the cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    # Print only foods with heat_level > 5 formatted with 🌶 emojis
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")

def get_average_heat_level(spicy_foods):
    # Return the average heat level of all spicy foods
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    # Return a new list with the new spicy_food added
    return spicy_foods + [spicy_food]
