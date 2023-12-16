def f(cell):
    import re
    a = re.findall(r'[a-zA-Z]{1,2}[0-9]{1,4}',cell)
    if a==[]:
        ans = False
    for item in a:
        if item == cell:
            ans = True
        else:
            ans = False
    return ans

g = f("Az")
print(g)