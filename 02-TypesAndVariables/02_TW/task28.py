# 28.	Correct body weight has a significant impact on health. Write a program that calculates the Body Mass Index (BMI) based on your height in cm and weight in kg. A user enters data from the keyboard. Find the formula on the Internet for calculating the BMI. Then, using your program, check that you have the correct weight. Display the calculated BMI and display True if the weight is within the valid range, or display False otherwise. 
height_string = input("Enter your height in cm: ")
height = float(height_string)
weight_string = input("Enter your weight in kg: ")
weight = float(weight_string)
BMI = weight/(height/100)**2
print(f"Your BMI equals {BMI}")
print("Correct weight?", BMI>=18.5 and BMI<=24.9 )