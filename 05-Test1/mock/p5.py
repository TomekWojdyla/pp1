#The binary system uses two symbols to represent a number: 0 and 1. Define a function f(binary_number) that returns True if the given notation is a valid binary number, or false otherwise. 

def f(binary_number):
    lenght = len(binary_number)
    for i in range (0,lenght):
        check = binary_number[i]=="0" or binary_number[i]=="1"
        if check==False:
            break
        else:
            pass
    return check

if __name__ == '__main__':
    #check your program in this place
    print(f(9))
    print(f(10))
    print(f(16))