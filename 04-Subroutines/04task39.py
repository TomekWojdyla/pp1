# 39.	A sentence is an ordered group of words separated by spaces (spaces). Define a function f(sentence) that returns a sentence with spaces removed. Sample result:
#f("integrated development environment") returns "integrateddevelopmentenvironment"
#f("A programming language is a system of notation for writing computer programs") returns "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms" 


def no_spaces(x):
    sent_len = len(x)
    disp = ""
    for i in range (0,sent_len):
        if x[i] == " ":
            pass
        else:
            disp += x[i]
    return disp

g = no_spaces("integrated development environment")
print(g)