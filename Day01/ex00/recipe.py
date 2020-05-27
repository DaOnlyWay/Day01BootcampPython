class Recipe ():
    """recipes"""

    def __init__(self, name, c_lvl, c_time, ingr, desc, r_type):
        self.n = name
        self.cl = c_lvl
        self.ct = c_time
        self.ingr = ingr
        self.de = desc
        self.r = r_type
        if isinstance(self.n, str) == 0:
            print("Error, the name of the recipe contains a non-string type")
            return
        if isinstance(self.cl, int) == 0:
            print("Error, the cooking level contains a non-int element")
            return
        if isinstance(self.ct, int) == 0:
            print("Error, the cooking time contains a non-int element")
            return
        if isinstance(self.ingr, list) == 0:
            print("Error, the ingredients must be given as a list")
            return
        if isinstance(self.de, str) == 0:
            print("Error, the description contains a non-string element")
            return
        if self.r != "starter" and self.r != "lunch" and self.r != "dessert":
            print("Error, the recipe type you entered does not exist")
            return

    def __str__(self):
        txt = "{}:\nLevel: {}/5\nTime: {}\nIngredients: {}\nDesc: {}\nType: {}"
        txt = txt.format(self.n, self.cl, self.ct, self.ingr, self.de, self.r)
        return txt
