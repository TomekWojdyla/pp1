#(p3.py) Flight numbers along with the number of passengers are stored in a dictionary d. Define a function f(d) that returns the number of flights in which the number of passengers is greater than the average number of passengers on all flights. Example:
#f({"LO231":150,"BA787":120,"NZ15":30})  2
#f({"LO231":150,"BA787":20,"NZ15":30})  1

def f(d):
    lent = len(d)
    sum_pass = 0
    counter = 0
    for key in d:
        sum_pass += d[key]
    avg = sum_pass/lent
    for key in d:
        if d[key]>avg:
            counter+=1
        else:
            pass
    return counter

a = f({"LO231":150,"BA787":120,"NZ15":30})
print(a)
a = f({"LO231":150,"BA787":20,"NZ15":30})
print(a)