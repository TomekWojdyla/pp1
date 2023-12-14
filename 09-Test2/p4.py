def f(subjects):
    lent = len(subjects)
    sol = {}
    for key, value in subjects.items():
        notes = value
        lentv = len(value)
        sum = 0
        for i in range(lentv):
            sum += notes[i]
        avg = sum/lentv
        sol.update({key:avg})
        top_subject = ""
    max_grade = 0
    for key, value in sol.items():
        if value>=max_grade:
            max_grade = value
            top_subject = key
        else:
            pass
    return top_subject


            

if __name__ == "__main__":
    # function calls
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))
    print(f({"math":[5,5,5],"geo":[5,4,4,4],"comp":[5,4]}))
    
    
    
    
    