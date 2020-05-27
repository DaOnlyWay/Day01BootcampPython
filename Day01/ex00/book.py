from recipe import Recipe
import datetime


class Book():
    """book of recipes"""

    def __init__(self, name):
        self.n = name
        self.rl = {'starter': [], 'lunch': [], 'dessert': []}
        self.cd = datetime.datetime.now()
        self.lu = datetime.datetime.now()

    def get_recipe_by_name(self, name):
        for values in self.rl.values():
            for recipes in values:
                if recipes.n == name:
                    print(str(recipes))

    def get_recipe_by_types(self, recipe_type):
        for keys in self.rl.keys():
            if keys == recipe_type:
                for recipe in self.rl[keys]:
                    print(str(recipe))
                    print('--------------')

    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe) == 1:
            if recipe.r == 'starter':
                self.rl['starter'].append(recipe)
            elif recipe.r == 'lunch':
                self.rl['lunch'].append(recipe)
            elif recipe.r == 'dessert':
                self.rl['dessert'].append(recipe)
            self.lu = datetime.datetime.now()
        else:
            print("Error, the given arg is not a Recipe")
            return
