
from colorama import Fore
print(Fore.BLUE)

print("Temperature Converter")
print("*******************************************************")
print(Fore.WHITE)


a = input("Hello, do you want to convert from Celsius(C), or Fahrenheit(F)? ")

if(a == "C"):
  aa = input("What temperature would you like to convert from? ")
  
  aaa = (9/5 * float(aa) + 32)
  print(aa, "degrees Celsius equals", aaa, "degrees Fahrenheit.")

elif(a == "F"):
  b = input("What temperature would you like to convert from? ")

  bb = (5/9*(float(b)-32))
  print( b, "degrees Fahrenheit equals",bb, "degrees Celsius.")

else:
  print("*************************************************")
  print("Run the program again and enter F or C.")
