#(p1.py) The playing cards have the following values: Ace (A), King (K), Queen (Q), Jack (J) and 10 (T) have a value of 10 each. The other cards have the value indicated by the card number. Create a function f(player1,player2) that returns true if the first player has cards of the same or higher value, and false otherwise. Example:
#f("AJ972","AQT72")  False
#f("9532","K8")  True

def f(player1,player2):
    sum1 = 0
    sum2 = 0
    fig = ["A","K","Q","J","T"]
    for i in range(len(player1)):
        if player1[i] in fig:
            sum1+=10
        else:
            sum1+=int(player1[i])
    for i in range(len(player2)):
        if player2[i] in fig:
            sum2+=10
        else:
            sum2+=int(player2[i])
    if sum1>=sum2:
        return True
    else:
        return False
    
a = f("AJ972","AQT72")
print(a)
a = f("9532","K8")
print(a)