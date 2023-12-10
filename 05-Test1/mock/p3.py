def acronym(text):
    lent = len(text)
    disp = text[0]
    for i in range(1,lent):
        if text[i-1] == " ":
            disp += text[i]
        else:
            pass
    return disp

#g = acronym("Internet of Things")
#print(g)
#h = acronym("For Your Information")
#print(h)
#k = acronym("Python")
#print(k)