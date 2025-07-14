class Movie:

    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    #getter method -- recuerda que un metdodo es una funcion dentro de una clase
    #getters DO NOT TAKE ANY ARGUMENT, THEY ARE JUST CALLED
    def get_title(self):
        return self._title
    

my_movie = Movie("The Matrix", 5.0)

print(my_movie.get_title())

class Cat:

    def __init__(self, name, breed):
        self._name = name
        self.breed = breed

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

my_cat = Cat("Apollo", "Van Turco")
my_cat.set_name("Pipi")
print(my_cat.get_name())

my_cat.set_name("Leonel")
print(my_cat.get_name())

print('--Coding session--')

class Backpack:

    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items
    
    
    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print('Please enter a valid list of items')

bag1 = Backpack()
bag1.set_items(['Book', 'Pencil', 'Eraser'])
print(bag1.get_items())
bag1.set_items(['Laptop', 'Battery', 'Pen'])
print(bag1.get_items())