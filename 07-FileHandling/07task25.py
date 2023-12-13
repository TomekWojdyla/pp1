# 25.	The announcement regarding the temperature forecast in degrees Celsius for the next three days was published on the Internet:
#"Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
#Create a program that calculates the average temperature. Use regular expressions to extract the values of temperatures from the message.
#import re

#message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
#temperatures = re.findall("\d{2}",message)
# complete the program code
# ...


import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temp = re.findall("\d{2}",message)
print(temp)

sum = 0
for i in range(len(temp)):
    sum += int(temp[i])

avg = sum/len(temp)
print(avg)