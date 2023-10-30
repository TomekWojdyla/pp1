#Transformation of temperature provided in Celcius to Kelvin and Fahrenheit
#Entry of temperature in Celcius:
temp_input = input("Provide temperature in Celcuis: ")
temp_celcius = float(temp_input)
#transformation of temperature to Kelvin scale
temp_kelvin = 273.15 + temp_celcius
#here we could put a validation if temp_kelvin is >=0 to eliminate negative value in Kelvin scale that is out of range. This could also be enteren after input.
#transformation of temperature to Fahrenheit scale
temp_fahrenheit = (temp_celcius*9/5) + 32
#Output of results
print(f"Temperature {temp_celcius}deg in Celcius scale equals to {temp_kelvin}deg in Kelvin scale and {temp_fahrenheit}deg in Fahrenheit scale.")
