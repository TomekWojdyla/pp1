#(p7.py) A valid username consists of 4 to 12 characters: lowercase letters, numbers and the underscore character. Create a function f(arr) that, for a given array of usernames, returns the number of valid usernames in the array. Example:
#f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])  2

import re

def f(arr):
    pass_ok=0
    for i in range(len(arr)):
        a = re.findall(r'\b[a-z0-9_]{4,12}\b',arr[i])
        if a==[]:
            pass
        elif a[0]==arr[i]:
            pass_ok+=1
        else:
            pass
    return pass_ok

a = f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])
print(a)
        
