#18.	Define a function numbers(n) that returns a string containing integer numbers from 1 to n, separated by a single space character. Then, call the function and display numbers from 1 to 15 and from 1 to 7. Sample result:
#Numbers <1,15>: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#Numbers <1,7>: 1 2 3 4 5 6 7

#????

#def numbers(n):
#       i=1
#        while i < n:
#                print(i, end=" ")
#                i=i+1
#        return a

#prov=int(input("Provide max element in range: "))        
#print(f"Numbers <1,{prov}>: ", numbers(prov))

def numbers(n):
        a=""
        for i in range(1,n+1):
                b=str(i)
                a=a+" "+b
        return a

#print(numbers(5))

prov=int(input("Provide max element in range: "))        
print(f"Numbers <1,{prov}>: ", numbers(prov))