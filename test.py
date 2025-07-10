class Laptop:
    tipo_dispositivo = "Computadora"

    def __init__(self, marca, precio, color):
        self.marca = marca      #instance attribute. Atributos que tendra el objeto al crearse. Self hace referecia a si mismo, el objeto.
        self.precio = precio
        self.color = color


mi_laptop = Laptop("Lenovo",1200, "Negro")

print(mi_laptop.tipo_dispositivo, mi_laptop.color)

class Circle:
    
    radius = 5

    def __init__(self, color):
            self.color = color
            
my_circle = Circle('Red')
your_circle = Circle('Black')

Circle.radius = 10

print(my_circle.radius, your_circle.radius)




class Rectangle:
     def __init__(self, length, width):
          self.length = length
          self.width = width


class Movie:

     id_counter = 1

     def __init__(self, title, rating):
          self.id = Movie.id_counter
          self.title = title
          self.rating = rating
          

          Movie.id_counter += 1

my_movie = Movie('The Matrix Revolutions', 4.4)
your_movie = Movie('Saving Private Ryan', 4.2)


print(my_movie.id)
print(your_movie.id)


# how to create instances:

class Backpack:
     
    max_num_items = 10

    def __init__(self):
        self.items = []
        

my_bag = Backpack()
your_bag = Backpack()


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


print(Dog.species)


class Pizza:

     price = 12.99

     def __init__(self, description, toppings, crust):
          self.description = description
          self.toppings = toppings
          self.crust = crust

my_pizza = Pizza('PizzaCoco', ['Peperoni', 'Jam', 'Meat'], 'Cheese')

Pizza.price = 11.99

print(my_pizza.description, my_pizza.toppings, my_pizza.crust, my_pizza.price)

class MyClass:
 
    x = 5
 
    def __init__(self):
        MyClass.x += 1
 
 
obj1 = MyClass()
obj2 = MyClass()
MyClass.x = 26
obj3 = MyClass()
 
print(MyClass.x) # Output? 27