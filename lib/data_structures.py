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
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names          
    pass
get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food ["heat_level"] > 5]  
    return spiciest
    pass
get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:    
        print(food["name"] + " " + "(" + food["cuisine"] + ")" +" " + "|" + " " + "Heat Level:" +" " + "🌶" * food["heat_level"] )
        pass
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    pass
get_spicy_food_by_cuisine(spicy_foods, "American")

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
       if food["heat_level"] > 5:
        print(food["name"] + " " + "(" + food["cuisine"] + ")" + " " + "|" + " "  + "Heat Level:" + " " + "🌶" * food["heat_level"] )
    pass
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    sum = 0
    total = len(spicy_foods)
    for food in spicy_foods:
        sum+=food["heat_level"]
    average = sum/ total  
    return average
    pass
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
create_spicy_food(spicy_foods,  spicy_food =  {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    )
