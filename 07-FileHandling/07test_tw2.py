import re
x = 'Uzyskalismy $10.00 za ciasteczka.'
y = re. findall('\$[0-9.]+', x)
print(y)