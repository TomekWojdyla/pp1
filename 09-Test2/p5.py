def f(first_letter, last_letter):
    import re
    handler = open("data.txt", encoding="UTF-8")
#    text = "To jest przykladowy teast Tomka Totomka tost"
    text = handler.read()
    arr = text.split()
    print(arr)
    lent = len(arr)
#    print(lent)
    counter  = 0
    for i in range(lent):
        word = arr[i]
        lent2 = len(word)
        if word[0] == first_letter and word[-1] == last_letter:
            counter +=1
        else:
            pass
    
#    disp = ""
#    for items in arr:
#    search_fun = str("\b")+ "["+str(first_letter)+"][a-zA-Z]["+str(last_letter)+"]"+str("\b")
#    print(search_fun)
#    arr = re.findall(r"\b{first_letter}[a-zA-Z]+\b",text)
#    print(arr)
#    lent = len(arr)
#    handler.close()



    return counter




if __name__ == "__main__":
    # function calls
    print(f("T","e"))
   # print(f("t","t"))
   # print(f("j","t"))


