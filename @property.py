'''
class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    # getter with @property
    @property
    def rating(self):
        return self._rating
    
    # setter with @ property
    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print('Please enter a valid rating')

    

favorite_movie = Movie('The Matrix', 4.8)
print(favorite_movie.rating)    # -- calls the getter(rating)

favorite_movie.rating = 4.9
print(favorite_movie.rating)


class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    
    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print('Please enter a valid list')


mybag = Backpack()
print(mybag.items)
mybag.items = ['Book', 'Pencil']
print(mybag.items)
mybag.items = 'Pen'
print(mybag.items)

'''


class Libro():
    
    def __init__(self, titulo, autor, precio):
        self._titulo = titulo
        self._autor = autor
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 1:
            self._precio = nuevo_precio
        else:
            print('Precio invalido')

    def mostrar_info(self):
        print(f'{self._titulo} de {self._autor}. Precio {self._precio}')

libro1 = Libro('1984', 'Orwell', 15.95)
libro1.precio = 0
libro1.mostrar_info()
