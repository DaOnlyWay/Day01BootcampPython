class GotCharacter():
    """got char"""

    def __init__(self, first_name, is_alive):
        self.finame = first_name
        self.alive = is_alive


class Stark(GotCharacter):
    """got family"""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = 'Stark'
        self.house_words = 'Hehe boi'

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.alive = False
