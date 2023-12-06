#29.	The vending machine accepts 1, 2 and 5 PLN coins. Define a function f(amount_to_pay) that returns the minimum number of coins that can be used to pay for the purchased product. Sample result:
#f(23) returns 6
#f(8) returns 3
#f(2) returns 1
#f(0) returns 0


def min_coins(x):
    five = x//5
    two = (x-5*five)//2
    one = x-5*five -2*two
    minimum = five+two+one
    return minimum

price = int(input("Provide price: "))

coins = min_coins(price)

print(f"your minimum count of coins is: {coins}")

    