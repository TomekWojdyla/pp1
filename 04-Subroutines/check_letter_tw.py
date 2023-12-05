def check_letter(let, text):
    text_length=len(text)
    total_let_count = 0
    i=0
    sum=0
    while i<text_length:
        if text[i]==let:
            sum += 1
            i += 1
        else:
            i +=1
    return sum

test = "miala baba koguta "
letter = " "

count = check_letter(letter, test)
print(count)