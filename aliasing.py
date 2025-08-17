class Circle:
    def __init__(self, radius):
        self._radius = radius


my_circle = Circle(4)
your_circle = my_circle

print(my_circle is your_circle)


class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            print('This item is not in the backpak')

my_bag = Backpack()
your_bag = my_bag
her_bag = your_bag

my_bag.add_item('Pencil')
my_bag.add_item('Book')
my_bag.add_item('Pen')

print(my_bag.items)
print(your_bag.items)
print(her_bag .items)
