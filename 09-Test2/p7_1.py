def f(arr):
    lent = len(arr)
    import re
    count = 0
    for i in range(lent):
        a = (re.findall(r"\b[a-z0-9_]{4,12}\b",arr[i]))
        b = str(a)
        print(b)
        print(arr[i])
        if b==str(arr[i]):
            count +=1
        else:
            pass
    return count
    
    
if __name__ == "__main__":
    # function calls
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
