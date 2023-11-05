no = input ("wprowadz liczbe x: ")
try :
    x=int(no)
    if x>5 :
        print("x>5 jest prawdziwe")
    else :   
        print("x>5 jest nieprawdziwe")
    print("to wydrukuj tak czy inaczej: x = ",x)
except :
    print("Liczbe podaj! zacznij jeszcze raz")
i=7
print("aliczba jego to ",i)

print(type(i))
print(type(no))

#petle
tot = 0
for number in range(1,21):
    if number % 2 == 0:
       tot = tot + 1
       print(number)
print(f"We have {tot} even numbers in {range(1,20)}") 
