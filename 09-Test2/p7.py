def f(arr):
    lent = len(arr)
    dict = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,r,s,t,u,v,x,y,x,z,1,2,3,4,5,6,7,8,9,0,_]
    lent_dict = len(dict)
    for i in range(lent):
        trypass = arr[i]
        lenttry = len(trypass)
        if lenttry>=4 and lenttry<=12:
            check = False
            for k in range(lenttry):
                for j in range(lent_dict):
                    if trypass[k] == dict[j]:
                        check = True
                        break
                    else:
                        pass
            