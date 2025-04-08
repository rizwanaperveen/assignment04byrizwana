import colorama
temperature_farhenheit = input("give the temperature in farenheit:")

temperature_farhenheit = int(temperature_farhenheit)

temperature_celcius = (temperature_farhenheit - 32) * 5.0/9.0

print(f"The temperature in celcius is  {temperature_farhenheit} =", colorama.Style.BRIGHT + str(temperature_celcius))