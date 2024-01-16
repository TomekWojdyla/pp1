#(p7.py) A computer system registers all entries into the car park ("in") and exits from the car park ("out"). Define a function f(d) that for the registered data d returns an array containing the registration numbers of vehicles that remain in the car park, in alphabetical order. Example:
#cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
#f(cars)  ["BA111","GX444","KR234"]
#cars1 = [["KR234","in"],["KR234","out"]]
#f(cars1)  []

def f(d):
    lent = len(d)
    outp=[]
    for i in range(lent):
        if d[i][1]=="in":
            outp.append(d[i][0])
        elif d[i][1]=="out":
            outp.remove(d[i][0])
    outp.sort()
    return outp

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
a = f(cars)
print(a)
cars1 = [["KR234","in"],["KR234","out"]]
b = f(cars1)
print(b)