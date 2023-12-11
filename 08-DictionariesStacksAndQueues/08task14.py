# 14.	A dictionary contains course names along with the number of hours. Write a program that calculates and displays the total number of hours. Sample results:
#winter_semester = {
##    "math":60,
#    "programming":30,
#    "history":15
#}
#The total number of hours in the winter semester is …

winter_sem = {
    "math":50,
    "PP":15,
    "OiZ":30,
    "Ask":25
}

sum = 0
for key,value in winter_sem.items():
    sum += value
    
print(sum)