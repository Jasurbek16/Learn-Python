'''Namedtuples are a memoryefficient
shortcut to defining an immutable class in Python 
manually.'''

from collections import namedtuple
from random import randint

# Color = namedtuple('Color', 'red green blue')
# a name of the namedtuple^('typename') and the val.s ^ it has

# typename -- the name of the new class that’s being created 
# by calling the namedtuple function.

# we can also use a string with the delimeter of ''
# that takes in several different methods 
# ,automatically splits, and passes as a list like above

# the 2nd arg -- field names for the class created by the namedtuple()

# The class name is used in the docstring and 
# the __repr__ implementation that namedtuple automatically
# generates for us.

# color = Color(55, 155, 255)

########################################################################
#### _asdict() ####
# Making a dictinary of the contents of the tuple
# print(color._asdict())

########################################################################
#### _replace() ####
# Making a shallow copy when replacing some of that's fields
# new_color = color._replace(red=100)
# print(new_color.red)

########################################################################
# we can specify red = blue = and green = as well, but that's optional
# print(color[0]) and print(color.red) <- these are equal
# it is more readible than the regular tuple
########################################################################
# white = Color(255, 255, 255)

# print(white.blue)
########################################################################
# Tuple unpacking and the *-operator for function argument unpacking
# also work as expected:
#
# >>> red, green, blue = color
# >>> print(red, green, blue)
# 55 155 255
# >>> print(*color)
# 55 155 255
########################################################################
# You’ll even get a nice string representation 
# for your namedtuple object
# for free, which saves some typing and verbosity:
#
# >>> color
# Color(red=55, green=155, blue=255)
########################################################################
# Subclassing Namedtuples
# class CoolColor(Color):
#     def tell_cool_color(self):
#         if self.red == 46 and self.green == 140 and self.blue == 206:
#             print('Nice choice!')

# new_obj = CoolColor(46, 140, 206)
# print('Color [R, G, B]:', new_obj.red, new_obj.green, new_obj.blue)
# new_obj.tell_cool_color()

########################################################################
# Adding a new immutable field; Creating hierarchies of namedtuples
# Color = namedtuple('Color', 'red green blue')
# Color_Transparency = namedtuple('Color_Transparency', Color._fields + ('alpha',))

# rgba_added = Color_Transparency(10, 40, 30, 0.5)
# print(rgba_added)

########################################################################
# Using a _make() classmethod for creating new instances of a namedtuple
# from a sequence or iterable
# created_obj = Color._make([101, 101, 101])
# print(created_obj)

########################################################################

##### Takeaways #####
# • collection.namedtuple is a memory-efficient shortcut to
# manually define an immutable class in Python.

# • Namedtuples can help clean up your code by enforcing an
# easier-to-understand structure on your data.

# • Namedtuples provide a few useful helper methods that all start
# with a single underscore, but are part of the public interface.
# It’s okay to use them.

########################################################################
# from typing import NamedTuple

# class Car(NamedTuple):
#     color: str
#     mileage: float
#     automatic: bool

# car1 = Car('red', 3812.4, True)
# # Instances have a nice repr:
# car1
# # Accessing fields:
# car1.mileage
# # Fields are immutable:

# car1.mileage = 12
# AttributeError: "can't set attribute"

# car1.windshield = 'broken'
# AttributeError:
# "'Car' object has no attribute 'windshield'"

# # Type annotations are not enforced without
# # a separate type checking tool like mypy:
# Car('red', 'NOT_A_FLOAT', 99)
# Car(color='red', mileage='NOT_A_FLOAT', automatic=99)
########################################################################