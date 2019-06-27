choice = input('type \'f\' to convert from farenheit to celsius or type \'c\' to convert celsius to farenheit\n')
convertedTemp = 2
temp = float(input('Enter a temp: '))

if choice == 'f':
    convertedTemp = (temp - 32) * 5/9
    print(round(convertedTemp,2), "°c")
elif choice == 'c':
    convertedTemp = (temp * 9/5) + 32 
    print(round(convertedTemp,2), "°f")
else:
    print("cannot convert\n")
    

