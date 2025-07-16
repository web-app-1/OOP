'''
class Dog:

    def __init__(self, age):
        self._age = age

    
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 < new_age < 30:
            self._age = new_age
        else:
            print(f'Please enter a valid age')

    age = property(get_age, set_age)


my_dog = Dog(8)
print(f'My dog is {my_dog.age} years old')
print('One year later')
my_dog.age += 1
print(f'My dog is now {my_dog.age} years old')
'''

class Circle:

    VALID_COLORS = ('red', 'blue', 'black')

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius
    
    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print('Please enter a valid radius')

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color
        
    
    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
            print(f'Color changed to {new_color}')
        else:
            print('Please enter a valid color')

    color = property(get_color, set_color)

circle1 = Circle('12', 'blue')
circle1.radius = 21
print(circle1.get_radius())


print(circle1.get_color())
circle1.set_color('red')