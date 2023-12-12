def f(first_letter, last_letter):
    handler = open("data.txt", encoding="UTF-8")
    text = handler.read()
    
    disp = ""
    for line in text:
        for word in line:
            print(word)
            if word[0]==first_letter and word[-1]==last_letter:
                disp +=word +" "
            else:
                pass
    handler.close()
    return disp


g = f("a","z")
print(g)



#handler = open("data.txt", encoding="UTF-8")
#text = handler.read()
#print(text)