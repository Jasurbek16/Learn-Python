#1 – “Old Style” String Formatting
>>> 'Hello, %s' % name
'Hello, Bob'

>>> '%x' % errno
'badc0ffee'

>>> 'Hey %s, there is a 0x%x error!' % (name, errno)
'Hey Bob, there is a 0xbadc0ffee error!'

>>> 'Hey %(name)s, there is a 0x%(errno)x error!' % {
... "name": name, "errno": errno }
'Hey Bob, there is a 0xbadc0ffee error!'

#2 – “New Style” String Formatting
>>> 'Hey {name}, there is a 0x{errno:x} error!'.format(
... name=name, errno=errno)
'Hey Bob, there is a 0xbadc0ffee error!'

#3 – Literal String Interpolation (Python 3.6+)
>>> f"Hey {name}, there's a {errno:#x} error!"
"Hey Bob, there's a 0xbadc0ffee error!"

#4 – Template Strings
>>> from string import Template
>>> t = Template('Hey, $name!')
>>> t.substitute(name=name)
'Hey, Bob!'

>>> templ_string = 'Hey $name, there is a $error error!'
>>> Template(templ_string).substitute(
... name=name, error=hex(errno))
'Hey Bob, there is a 0xbadc0ffee error!'
# Template Strings close an attack vector, and this makes
# them a safer choice if you’re handling format strings generated from
# user input

# Dan’s Python String Formatting Rule of Thumb:
    
    # If your format strings are user-supplied, use Template
    # Strings to avoid security issues. Otherwise, use Literal
    # String Interpolation if you’re on Python 3.6+, and “New
    # Style” String Formatting if you’re not.