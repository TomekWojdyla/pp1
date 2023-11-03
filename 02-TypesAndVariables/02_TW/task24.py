#check car registration plates from entry if from Krk
reg_no = input("Enter vehicle registration number: ")
reg_no_city = reg_no[0:2]
reg_check = reg_no_city=="KK" or reg_no_city=="KR"
print(f"Car is registered in Krakow: {reg_check}")