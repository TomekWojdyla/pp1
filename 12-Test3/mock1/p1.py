#(p1.py) Create a function f(word) that, for a given word, returns a string of characters in which the subsequent letters of the word form the so-called Mexican Wave. Initially, the first letter of the word is capitalized and the remaining letters are lowercase. Then, the second letter of the word is capitalized and the remaining letters are lowercase, etc. Separate words with a minus sign. Example:
#f("book")  "Book-bOok-boOk-booK"
#f("water")  "Water-wAter-waTer-watEr-wateR"
##f("ok")  "Ok-oK"
#f("a")  "A"
#f("")  ""


def f(word):
    lent = len(word)
    outp = ""
    for i in range(lent):
        for j in range(lent):
            if i==j:
                outp += word[j].upper()
            else:
                outp += word[j]
        if i<lent-1:
            outp+="-"
        else:
            pass
    return outp
    
a = f("book")
print(a)
a = f("water")
print(a)
a = f("ok")
print(a)
a = f("a")
print(a)
a = f("")
print(a)