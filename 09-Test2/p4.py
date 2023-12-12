def f(subjects):
    lent = len(subjects)
    sol = {}
    for key, value in subjects:
        notes = value
        lentv = len(value)
        sum = 0
        for i in range(lentv):
            sum += notes[i]
        avg = sum/lentv
        sol.update({key:avg})
        a = 0
    for key, value in sol:
        if value>a:
            a == value:
        else:
            

if __name__ == "__main__":
    # function calls
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))
    
    
    nie wiem
    
    
    