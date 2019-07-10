#Exercise 5

def fahrenheit_to_celsius(): #Converts a user temperature from Fahrenheit to Celsius.
    print('Please enter a temperature in Fahrenheit:')
    temp_f = int(input())
    temp_c = round(((temp_f - 32) * 5 / 9),4)
    print('The temperature {}°F is {}°C.'.format(temp_f, temp_c))

fahrenheit_to_celsius()

#Test Cases
#Input: 82      Output: 27.778
#Input: 32      Output: 0.0
#Input: 0       Output: -17.7778