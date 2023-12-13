#20.	Using any text editor, create the following two text files:
#MeatAndFish.txt
#Skinless white meat
#Tuna fish
#Luncheon meat
#Lean cuts of red meat
#GrainsAndBread.txt
#Bread
#Rice
#All purpose flour
#Breakfast cereal
#Pasta 
#Then, write a program that creates the allproducts.txt file, in which save the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.

f1 = open("MeatAndFish.txt")
f1_content = f1.read()
f2 = open("GrainsAndBread.txt")
f2_content = f2.read()
f3 = open("AllProducts.txt", "a")
f3.write(f1_content)
f3.write(f2_content)

f1.close()
f2.close()
f3.close()

