import re as red

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = red.findall("\d{2}",message)
# red.findall - szuka wszystkich dwucyfrowych liczb znajdujących sie w 'message'
print(temperatures)

suma = 0
for i in range(len( temperatures)):
    suma += int (temperatures[i])
print(suma)

srednia = suma / len(temperatures)

print(f"Srednia temperatura z tych dni wynosi: {srednia}")