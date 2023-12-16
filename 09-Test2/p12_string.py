def f(dictio,val):
#dictio = {"ddvf":126,"ccc":175, "ddx5":100}
#val = "ddxgx8"
    lent = len(val)
    count = 0
    for key in dictio:
        a = key
        for i in range(lent):
            if a[i] == val[i]:
                check = True
            else:
                check  = False
                break
        if check == True:
            count +=1
        else:
            pass
    return count


g = f({"ddvf":126,"ccc":175, "ddx5":100},"ccc")
print(g)
        