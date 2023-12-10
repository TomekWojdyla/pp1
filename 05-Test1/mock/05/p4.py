def f(card_no):
    card_str = str(card_no)
    lent = len(card_str)
    disp = ""
    selection = [0,1,lent-4,lent-3,lent-2,lent-1]
    for i in range(0,lent):
        if i in selection:
            disp += card_str[i]
        else:
            disp += "*"
    return disp

#g = f(1234567890123456)
#print(g)