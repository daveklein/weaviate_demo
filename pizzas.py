import json
from json import JSONEncoder
import random

class Pizza:
    def __init__(self, cheese, meats, veggies):
        self.cheese = cheese
        self.meats = meats
        self.veggies = veggies
    
class PizzaEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__    
    
def calc_cheese():
    i = random.randint(0, 6)
    cheeses = ['extra', 'none', 'three cheese', 'goat cheese', 'extra', 'three cheese', 'goat cheese']
    return cheeses[i]

def calc_meats():
    i = random.randint(0, 4)
    meats = ['pepperoni', 'sausage', 'ham', 'anchovies', 'salami', 'bacon', 'pepperoni', 'sausage', 'ham', 'anchovies', 'salami', 'bacon']
    selection = []
    if i == 0:
        return 'none'
    else:
        for n in range(i):
            selection.append(meats[random.randint(0, 11)])
    return ' & '.join(set(selection))

def calc_veggies():
    i = random.randint(0, 4)
    veggies = ['tomato', 'olives', 'onions', 'peppers', 'pineapple', 'mushrooms', 'tomato', 'olives', 'onions', 'peppers', 'pineapple', 'mushrooms']
    selection = []
    if i == 0:
        return 'none'
    else:
        for n in range(i):
            selection.append(veggies[random.randint(0, 11)])
    return ' & '.join(set(selection))

def gen_pizza():
    cheese = calc_cheese()
    meats = calc_meats()
    veggies = calc_veggies()
    return Pizza(cheese, meats, veggies)
    

def random_pizzas(quantity):
    pizzas = []
    for _ in range(quantity):
        pizzas.append(gen_pizza())

    j_pizzas = json.dumps(pizzas, indent=4, cls=PizzaEncoder)
    return j_pizzas

