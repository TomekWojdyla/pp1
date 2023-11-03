# 35.	A tree may be cut down if its diameter is at least 50 cm. Write a program that, based on the circumference of the tree entered from the keyboard, calculates and displays the value True if the tree can be cut down, or display the value False otherwise. Sample result:
#Enter tree circumference: …
#Tree can be cut down: …

import math

circ_str = input("Enter the tree circumference in cm: ")
circ = float(circ_str)
diam = circ/math.pi
#print("PI: ", math.pi)
print("Tree diamater in cm: ", round(diam,2))
print("Tree is big enough to be cut down: ", diam>=50)
