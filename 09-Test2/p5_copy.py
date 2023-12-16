def f(first_letter,last_letter):

    file_handler = open("data.txt", encoding="UTF-8")
    file_content = file_handler.read()
    words = file_content.split()
    lent = len(words)
    count = 0   
    for i in range(lent):
        a = words[i]
        if a[0] ==first_letter and a[-1]==last_letter:
            count +=1
        else:
            pass
    return count


g = f("a","d")
print(g)