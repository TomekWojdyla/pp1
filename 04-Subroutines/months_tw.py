
def months_name(n):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if n<=12 and n>=1:
        mname=months[n-1]
    else:
        mname ="Select a number between 1 and 12"
    return mname