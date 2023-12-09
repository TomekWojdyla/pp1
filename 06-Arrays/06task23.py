# 23.	An array contains numbers: -15, 8, -31, 47, -2, 19. Create a program that finds and displays the maximum and minimum number. Do not use available functions.

array = [-15,8,-31,47,-2,19]
maximum = array[0]
for i in range(1,len(array)):
    if array[i]>array[i-1] and array[i]>=maximum:
        maximum = array[i]
    else:
        pass
print(maximum)

minimum = array[0]
for i in range(1,len(array)):
    if array[i]<array[i-1] and array[i]<=minimum:
        minimum = array[i]
    else:
        pass
print(minimum)