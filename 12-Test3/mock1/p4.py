#(p4.py) The prods array contains the names of the products in stock. Create a function f(fnc,prods) that maps product names to their IDs, according to the fnc function. The f function returns a comma-separated list of product IDs, with no spaces. Example:
#prods = ["water","cheese","tomato"] 
#fnc1 = lambda x: "id:"+x[:2] 
#f(fnc1,prods)  " id:wa,id:ch,id:to"
#fnc2 = lambda x: (x[0]+x[-1]).upper() 
#f(fnc2,prods)  "WR,CE,TO"


def f(fnc,prods):
    lent = len(prods)
    outp = ""
    ans = list(map(fnc,prods))
    for i in range(lent):
        outp +=ans[i]+","
    lent2 = len(outp)
    outp = outp[0:lent2-1]
    return outp

prods = ["water","cheese","tomato"] 
fnc1 = lambda x: "id:"+x[:2] 
fnc2 = lambda x: (x[0]+x[-1]).upper() 
a = f(fnc1,prods) 
print(a)
a = f(fnc2,prods) 
print(a)