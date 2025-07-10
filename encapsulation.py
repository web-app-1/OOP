# Public vs non Public attributes


# PUBLIC
class Car1:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

my_car = Car1("Toyota", "Titan", 2026)
my_car.year = 2023
print(my_car.year)

#NON PUBLIC

class Car2:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year

my_car2 = Car2("Toyota", "Titan", 2026)
print(my_car2.model)


class Student:

    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self._age = age
        self.gpa = gpa


stu1 = Student(21, 'Luis', 39, 3.0)
print(stu1.age)

class Backpack:

    def __init__(self):
        self._items = []


class Book:


    def __init__(self, title):

        self._title = title

my_book = Book("RealPython")

print(my_book._title)

