#17.	Define the function different(n1,n2,n3), which returns True if all three numbers n1,n2,n3 are different or False otherwise. Then, write a program that reads three integers from the keyboard. Checks whether the numbers are different. Sample result:
#Enter first number: …
#Enter second number: …
#Enter third number: …
#Numbers …, …, and … are different

#def different(n1,n2,n3):
#    if n1==n2 :
#        if n2==n3 :
#            a = True
#        else:
#            a = False
#    else:
#        a = False
#    return a

def different(n1,n2,n3):
    if n1!=n2 and n2!=n3 and n1!=n3:
        a=False
    else:
        a=True
    return a

no1 = float(input("Enter first number: "))
no2 = float(input("Enter second number: "))
no3 = float(input("Enter third number: ")) 

comp = different(no1, no2, no3)
if comp==True:
    print(f"Numbers {no1}, {no2} and {no3} are equal. Boolean: ", comp)
else:
    print(f"Numbers {no1}, {no2} and {no3} are different. Boolean: ", comp)      