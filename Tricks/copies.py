'''Copying mutable collections like lists, dicts, and sets'''

original_list = [1,2,3,4,5,[1,2,3]]
new_list = list(original_list)
# ^ However, this method won’t work for custom objects and, on top of
# that, it only creates shallow copies which means that both lists share
# the same child objects.
# copy.copy() <- is also possible to make a shallow copy
# Pythonic to simply use the list, dict, and set factory functions 
# to create
# shallow copies.

new_list[5][0]=2
original_list[5][0]=1

print(original_list)
print(new_list)

'''Instead we're gonna use a deepcopy()'''
import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''Using copies with arbitary objects'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'

a = Point(23, 42)
b = copy.copy(a)
print(a)

print(b)

print(a is b)

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright
    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
    f'{self.bottomright!r})')

rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)

print(rect)
print(srect)
print(rect is srect)

drect = copy.deepcopy(srect)
drect.topleft.x = 222
print(drect)
print(rect)
print(srect)