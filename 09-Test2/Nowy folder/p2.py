def f(d):
    lent=len(d)
    ppl=0
    for i in range(lent):
        if d[i]=="+":
            ppl+=1
        else:
            ppl = ppl -1
    return ppl


