#43.	A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words). Sample result:
#f("Internet of Things") returns "IoT"
#f("For Your Information") returns "FYI"
#f("Python") returns "P"


def f(x):
    y = len(x)
    acr = x[0]
    for i in range (1,y):
        if x[i] == " ":
            acr += x[i+1]
        else:
            pass
    return acr

g = f("Internet of Things")
print(g)
g = f("For Your Information")
print(g)
g = f("Python")
print(g)