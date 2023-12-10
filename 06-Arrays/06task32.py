# 32.	Define a function occurs(number, array) that returns True if a given number is present in an array. Then create a program that checks whether the number entered from the keyboard is present in the array [15, 38, 7, 23, 14]. Sample result:
#Number: 23
#Array: 15 38 7 23 14
#Result: number 23 appears in the array


def occurs(num, arr):
    n = len(arr)
    check = False
    for i in range(n):
        if num == arr[i]:
            check = True
            break
        else:
            pass
    return check

number = int(input("Enetr number: "))
array = [15, 38, 7, 23, 14]
g = occurs(number,array)
if g == False:
    print(f"number{number} is NOT present in array.")
else:
    print(f"Number {number} IS PRESENT in array.")