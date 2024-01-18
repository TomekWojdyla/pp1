#(p3.py) A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words). Sample result:
#f("Internet of Things") returns "IoT"
#f("For Your Information") returns "FYI"
#("Python") returns "P"

def f(name):
    words = name.split()
    outp=""
    for i in range(len(words)):
            outp+=words[i][0]
    return outp

a = f("Internet of Things")
print(a)

a = f("For Your Information")
print(a)

a = f("Python")
print(a)

a = f("")
print(a)