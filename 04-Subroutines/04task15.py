#15.	Define a function phone_keyboard() that displays numbers in the layout as below (like on a phone keypad). Apply a loop statement. Then, call the function. Sample result:
#1 2 3
#4 5 6
#7 8 9

def phone_keyboard():
    for i in range(1,10,3):
        a=i
        b=i+1
        c=i+2
        print(f"{a} {b} {c}")
        
phone_keyboard()

print("Second solution")

def phone_keyboard(n):
    print(f"{n} {n+1} {n+2}")

for i in range(1,10,3):
    if i%3==1:
        phone_keyboard(i)
    else: 
        pass

print("Third solution")

def phone_keyboard(n): # ??????
    row =""
    for i in range(0,3):
        row=row+" "+str(i)
    return row

for i in range(1,10,3):
    if i%3==1:
        print=(phone_keyboard(i))
    else: 
        pass