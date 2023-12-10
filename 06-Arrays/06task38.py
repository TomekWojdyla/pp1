# 38.	Write a program that, for the given array of real numbers, displays the number of elements that are greater than the given value entered from the keyboard.

n = float(input("Enter min number: "))
arr = []
a =0
while a != "end":
    a = (input("Enter array element or type end to finish: "))
    if a == "end":
        break
    else:
        b = str(a)
        arr.append(b)

lent = len(arr)
disp = ""
for i in range(lent):
    if float(arr[i])>n:
        disp += str(arr[i]) + " "
    else:
        pass
print(disp)

    