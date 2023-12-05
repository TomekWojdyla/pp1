def card_number(n):
    a=str(n)
    disp=""
    for i in range (1,len(a)):
        if i==1 or i==2 or i>=len(a)-4:
            disp += a[i]
        else:
            disp += "*"
    return disp

      
    