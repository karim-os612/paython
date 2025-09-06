number1 = int(input("Enter your number:"))
number2 = int(input("Enter your second number:"))
print("1:plural")
print("2:minus")
print("3:multiplication")
print("4:division")
choice = int(input("select your choice"))
if(choice == 1):
   final = number1 + number2
   print(final)
elif(choice == 2):
   final = number1 - number2
   print(final)
elif(choice == 3):
   final = number1 * number2
   print(final)
elif(choice == 4):
   final = number1 / number2
   print(final)
else:
   print("you dont select")
input("please press Enter key to close program:)")
