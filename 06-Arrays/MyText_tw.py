#a.	A function that returns the number of words in the text

def word_count(x):
    #count = 0
    #for word in x:
    #    count += 1
    arr=x.split()
    count = len(arr)
    return count


#b.	A function that returns an ordered array of words, from longest to shortest
def word_ordered(x):
    arr = x.split()
    sort = sorted(arr,key=len,reverse=True)
    return sort


#c.	A function that returns an alphabetically ordered array of words
def word_alpha(x):
    arr = x.split()
    sort = sorted(arr)
    return sort
