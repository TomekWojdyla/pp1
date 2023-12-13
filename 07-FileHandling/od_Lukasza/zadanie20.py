f = open("allproducts2", "w")

w = open("MeatAndFish", "r")
content = w.read()
f.write(content)
z = open("GrainsAndBread","r")
content = z.read()
f.write(content)



f.close()
w.close()
z.close()
