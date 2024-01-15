#(p3.py) The uid array contains user IDs in one of the popular websites. Identifiers should be unique. Create a function f(uid) that returns true if all ids are unique. Otherwise, the function returns false. Example:
#f(["john5","ann123","JOHN5","xxx","abc333","a10"])  True
#f(["abc123","ann","abc123","a10"])  False
#f(["bob2","bob2"])  False
#f(["bob2","BOB2"])  True

def f(uid):
    lent = len(uid)
    check = True
    for i in range(lent):
        for j in range (lent):
            if i==j:
                pass
            elif uid[i]==uid[j]:
                check = False
                break
    return check

a = f(["john5","ann123","JOHN5","xxx","abc333","a10"])
print(a)
a=f(["abc123","ann","abc123","a10"])
print(a)
a = f(["bob2","bob2"]) 
print(a)
a = f(["bob2","BOB2"])
print(a)