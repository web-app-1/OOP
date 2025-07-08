class Laptop:
    tipo_dispositivo = "Computadora"

    def __init__(self, marca, precio, color):
        self.marca = marca      #instance attribute. Atributos que tendra el objeto al crearse. Self hace referecia a si mismo, el objeto.
        self.precio = precio
        self.color = color


mi_laptop = Laptop("Lenovo",1200, "Negro")

print(mi_laptop.tipo_dispositivo, mi_laptop.color)

class Circle:
    def __init__(self, radius):
            self.radio = radius
            

circle1 = Circle(20)
print(circle1)


class Rectangle:
     def __init__(self, length, width):
          self.length = length
          self.width = width


class Movie:
     def __init__(self, title, year, lang, rating):
          self.title = title
          self.year = year
          self.lang = lang
          self.rating = rating


favorite_movie = Movie('The Matrix',2000, 'es', 5.0)
print(favorite_movie.title)

# how to create instances:

class Backpack:
     
    max_num_items = 10

    def __init__(self, color):
        self.items = []
        self.color = color


my_bag = Backpack("red")

my_bag.color = "blue"
print(my_bag.color)



class Circle2:
     def __init__(self, radius=5):
          self.radius = radius


my_circle2 = Circle2()
my_circle3 = Circle2(7)

print(my_circle2.radius)
print(my_circle3.radius)

#----- Assignment

class Donut:
     def __init__(self, flavor, toppings, filling, size):
          self. flavor = flavor
          self.toppings = toppings
          self.filling = filling
          self.size = size

my_donut =  Donut('vainilla', 'no topping', 'no filling', 'medium')
print(my_donut.flavor, my_donut.toppings, my_donut.filling, my_donut.size)

class Customer:
     def __init__(self, name, age, address, favorite_desert):
          self.name = name
          self.age = age
          self.address = address
          self.favorite_desert = favorite_desert

Customer1 = Customer('Luis', 39, 'at home', 'Donut')
print(Customer1.name, Customer1.age, Customer1.address, Customer1.favorite_desert)

class Cake:
     def __init__(self, flavor, price, quality):
          self.flavor = flavor
          self.price = price
          self.quality = quality

Cake1 = Cake('Maple', 10.00, 'OK')
print(Cake1.flavor, Cake1.price, Cake1.quality)

#----- end of Assignment

# Class attributes

class Dog:

    species = "Canis Lupus"     
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
