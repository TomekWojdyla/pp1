#(p4.py) The dictionary contains the names of subjects and the grades obtained. Create a function f(subjects) that, for the given subjects and their grades, returns the name of the subject for which the average grade is the highest. Example:
#f({"math":[5,5,4],"geo":[5,4,4,4],"comp":[5,4]})  "comp"

def f(subjects):
    avg = 0
    for key, value in subjects.items():
        lent = len(value)
        sum = 0
        for i in range(lent):
            sum+=value[i]
        new_avg = sum/lent
        if new_avg>avg:
            avg = new_avg
            max = key
    return max

a = f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})
print(a)
a = f({"math":[5,5,4],"geo":[5,4,4,4],"comp":[5,4]})
print(a)