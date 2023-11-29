# 35.	Write a program that displays numbers from 1 to 30. If the number is divisible by 3 then the program displays the word 'THREE'. Next, if the number is divisible by 5 then the program displays the word 'FIVE'. Finally, if the number is divisible by both 3 and 5 then the program displays the word 'BINGO'. Sample result:
# 1 2 THREE 4 FIVE THREE 7 ...

b=""
for i in range(1,31):
    if i%3 == 0 and i%5 != 0:
        a= "THREE"
        b=b+a+" "
    elif i%3 != 0 and i%5 == 0:
        a="FIVE"
        b=b+a+" "
    elif i%3 == 0 and i%5 == 0:
        a="BINGO"
        b=b+a+" "
    else:
        a=str(i)
        b=b+a+" "
print(b)