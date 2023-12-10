#36.	Write a program that counts the number of occurrences of any value from a tuple. Sample result:
#Tuple: 50,20,40,50,30,50
#Value: 50
#Number of occurrences: 3

tuple1 = (50,30,40,50,30,50,70,70,50,30,50)
rep = []
for i in range(len(tuple1)-1):
    multi = 1
    if tuple1[i] not in rep:
        for j in range(i,len(tuple1)-1):
            if i==j:
                pass
            else:
                if tuple1[i] == tuple1[j]:
                    multi +=1
                    rep.append(tuple1[i])
                else:
                    pass
    else:
        pass
    if multi>1:
        print(f"replicated number {tuple1[i]}")
        print(f"Number of repetitions {multi}")
    else:
        pass
