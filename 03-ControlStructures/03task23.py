#23.	Write a program that calculates a dog's age in dog’s years. For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years. Sample result:

age = float(input("Enter the dog's age in human years: "))
if age<=2:
    age_dog = 5.25*age
else:
    age_dog = 10.5 + (age-2)*4
print(f"The dog's age {age} in human years equals to {age_dog} in dog's years.")