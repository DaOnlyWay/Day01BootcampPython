from recipe import Recipe
from book import Book


recipe = Recipe("pâte", 1, 10, ['pasta', 'sauce'], "", "lunch")
recipe2 = Recipe("bonpaté", 2, 9, ['paure', 'chiottes propres'], '', 'lunch')
recipe3 = Recipe("willy", 2, 8, ['un bon pet', 'binouze'], '', 'dessert')
print("test affichage recipe --->", str(recipe))
print("test affichage recipe2 --->", str(recipe2), '\n')
test2 = Book('oui')
test2.add_recipe(recipe)
test2.add_recipe(recipe2)
test2.add_recipe(recipe3)
test2.get_recipe_by_name('bonpatésamere')
test2.get_recipe_by_types('lunch')
