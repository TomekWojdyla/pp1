#18.	Write a program that calculates values for the following fractions: 1/2, 1/3, ..., 1/10. First, Use the "while" statement, then, the "for" statement. Sample result:

i=1
while i<=10:
    print(f"1/{i} = {1/i}")
    i=i+1

print("Break")
# to samo ale for

for j in range(1,11):
    print(f"1/{j} = {1/j}")