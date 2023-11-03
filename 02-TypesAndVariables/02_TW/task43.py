#43.	In computer science, every written (graphic) character of human language (letters, digits, symbols, etc.) is encoded by assigning it a number. This allows characters to be stored, transmitted, and transformed using digital computers. Write a program that displays a numerical representation of each letter of your name. To convert a character to its numerical representation, use the Python ord() function. Sample result:
#Name: John
#J(74) o(111) h(104) n(110)
name=input("Enter your name: ")
a=name[0]
ord_a=ord(a)
b=name[1]
ord_b=ord(b)
c=name[2]
ord_c=ord(c)
d=name[3]
ord_d=ord(d)
e=name[4]
ord_e=ord(e)
print(f"{a}({ord_a}) {b}({ord_b}) {c}({ord_c}) {d}({ord_d}) {e}({ord_e})")

