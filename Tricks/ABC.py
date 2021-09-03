'''ABC - Abstract Base Class'''

'''Using just a python idiom'''

# class Base:
#     def foo(self):
#         raise NotImplementedError()

#     def bar(self):
#         raise NotImplementedError()

# class Concrete(Base):
#     def foo(self):
#         return 'foo() called'
# Oh no, we forgot to override bar()...
# def bar(self):
# return "bar() called"

# b = Base() 
# print(b.foo())
# c = Concrete()
# print(c.foo())
# print(c.bar())

# Furthermore, instantiating and using Concrete 
# works as expected.
# And, if we call an unimplemented method 
# like bar() on it, this also
# raises an exception

################################################

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    
    @abstractmethod
    def foo(self):      
        pass
    
    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    
    def foo(self):
        pass

# We forget to declare bar() again  ...
c = Concrete()

# • Abstract Base Classes (ABCs) ensure that derived classes implement
# particular methods from the base class at instantiation
# time.
# • Using ABCs can help avoid bugs and make class hierarchies easier
# to maintain