#29.	Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. Create a program that displays the numbers from the first array that do not appear in the second array.

array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]

diff = []
final_diff = ""
for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i] == array2[j]:
            pass
        else:
            diff.append(array1[i])
for i in range(0,len(diff)-2):
    if diff[i] == diff[i+1] == diff[i+2]:
        final_diff += str(diff[i]) + ", "
    else:
        pass
print(diff)
print(final_diff)

