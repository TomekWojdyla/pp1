def f(player1, player2):
    cards = {
        "A":10,
        "K":10,
        "Q":10,
        "J":10,
        "T":10,
        "9":9,
        "8":8,
        "7":7,
        "6":6,
        "5":5,
        "4":4,
        "3":3,
        "2":2
    }

    val1 = 0
    val2 = 0
    lent1 = len(player1)
    lent2 = len(player2)
    
    for i in range(lent1):
        a = player1[i]
        b = cards[a]
        val1 += b
    
    for i in range(lent2):
        c = player2[i]
        d = cards[c]
        val2 += d
        
    if val1 >= val2:
        check = True
    else:
        check = False
    return check

if __name__ == "__main__":
    # function calls
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))
    
    