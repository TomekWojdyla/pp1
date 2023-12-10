def f(text):
    lent = len(text)
    disp = text[0]
    for i in range(1,lent):
        if text[i-1] == " ":
            disp += text[i]
        else:
            pass
    return disp

#g = f("Internet of Things")
#print(g)
#h = f("For Your Information")
#print(h)
#k = f("Python")
#print(k)