#40.	The array contains integer 8 numbers in the range 1 to 999. Write a program that displays elements of the array formatted as below.
#-----------------------------------------
#|   1|  23|   5| 382|   1|  17|   4| 906|
#-----------------------------------------

arr = [1,23,5,382,1,17,4,906]
spacer = "-----------------------------------------"
len_spacer = len(spacer)
print(spacer)
disp="|"
for i in range(8):
    if len(str(arr[i])) == 1:
        disp += "   "+str(arr[i])+"|"
    elif len(str(arr[i])) == 2:
        disp += "  "+str(arr[i])+"|"
    elif len(str(arr[i])) == 3:
        disp += " "+str(arr[i])+"|"
    else:
        disp += " "+str(arr[i])+"|"
print(disp)
print(spacer)
        

