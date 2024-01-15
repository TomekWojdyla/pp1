#(p6.py) Assume that a valid variable name in a computer program consists of one to five characters. The first character of a variable name must be a lowercase or uppercase letter or an underscore. The remaining characters in the variable name can be uppercase or lowercase letters, digits or the underscore character. Create a function f(vname) that returns true if the variable name vname is valid. Otherwise, the function returns false. Example:
#f("abc")  True
#f("Abc")  True
#f("aBC")  True
#f("_ab_c")  True
#f("abcdef")  False
#f("8abc")  False
#f("_aB8_")  True
#f("_4x")  True

import re

def f(vname):
    check = True
    arr = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]{0,4}\b',vname)
    if arr ==[]:
        check = False
    return check

a = f("abc")
print(a)
a = f("Abc")
print(a)
a = f("aBC")
print(a)
a = f("_ab_c")
print(a)
a = f("abcdef")
print(a)
a = f("8abc")
print(a)
a = f("_aB8_")
print(a)
a = f("_4x")
print(a)