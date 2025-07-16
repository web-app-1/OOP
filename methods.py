'''
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def find_diameter(self):
        print(f'DIameter {self.radius * 2}')

'''

class BackPack():

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
            print(f'{item} added to the bag')
        else:
            print('Please provide a valid item')

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            print(f'{item} removed from the bag')
        else:
            print('Item is not in the backpack')

    def has_item(self, item):
        return item in self._items

my_bag = BackPack()
my_bag.add_item('Pencil')
my_bag.add_item('Book')
my_bag.add_item('Laptop')
print(my_bag.items)
my_bag.remove_item('Pencil')
print(my_bag.items)
print(my_bag.has_item('Book'))