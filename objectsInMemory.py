class Backpack:
    def __init__(self):
        self._items = []

@property
def items(self):
    return self._items

my_bag = Backpack()
your_bag = Backpack()

print(id(my_bag))
print(id(your_bag))