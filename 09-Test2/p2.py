def f(arr):
    lent = len(arr)
    check = []
    for i in range(lent-1):
        if arr[i] == arr[i+1]:
            check.append(True)
        else:
            check.append(False)
    if check[0] == False:
        val = arr[0]
    else:
        for i in range(lent-1):
            if check[i] == False:
                val = arr[i+1]
                break
    return val



if __name__ == "__main__":
    # function calls
    print(f([5,5,5,5,7,5,5]))
    print(f([1,5,5,5,5,5,5]))
    print(f([5,5,5,5,5,5,2]))