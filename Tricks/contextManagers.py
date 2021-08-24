# Class based context managers

class ManagedFile:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')

######################################################################

class Indent:
    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('\t' * self.level + text)


with Indent() as indent:
    indent.print('Hello')
    with indent:
        indent.print('Hola')
        with indent:
            indent.print('Wow')
    indent.print('end')


######################################################################
# Function based

from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')