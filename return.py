def fahrenheit(T_in_celsius):
    """ returns the temperature in degrees Fahrenheit """
    return (T_in_celsius * 9 / 5) + 32
cv1=int(input("Enter a celcius value from 0 to 30:"))
cv2=int(input("Enter a celcius value from 0 to 30:"))
cv3=int(input("Enter a celcius value from 0 to 30:"))
cv4=int(input("Enter a celcius value from 0 to 30:"))
cvalues = []
cvalues.append(cv1)
cvalues.append(cv2)
cvalues.append(cv3)
cvalues.append(cv4)
for i in cvalues:
    print(i, ": ",fahrenheit(i))