def f(arr):
    lent = len(arr)
    valid_pass = 0
    for i in range(lent):
        check = True
        password = arr[i]
        if len(arr[i])>=4 and len(arr[i])<=12:
            lent2 = len(password)
            passcheck = []
            for j in range(lent2):
                b = password[j]
                if b in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","x","y","z","0","1","2","3","4","5","6","7","8","9","_"]:
                    check = True
                else:
                    check = False
                    break
        else:
            check = False
        if check == True:
            valid_pass +=1
        else:
            pass
    return valid_pass
    
    
    

if __name__ == "__main__":
    # function calls
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
#   print(f(1,"programming"))