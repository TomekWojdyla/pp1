def f(dic,let):
#dic = {"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4],"music":[5,2]}
#let = "m"
    lent = len(dic)
    count = 0
    for key,value in dic.items():
        a = key
        if a[0]==let:
            count +=1
        else:
            pass
    return count
    



if __name__ == "__main__":
    # function calls
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]},"s"))
#    print(f({"math":[5,5,5],"geo":[5,4,4,4],"comp":[5,4]}))