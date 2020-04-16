# Multiplication Table
num1 = int(input("Enter multiplier: ")) #Enter multiplier.
for num in range(1, num1+1): #This is to loop through the num1 variable.
    print("This is a {} times table!".format(num)) #This is to print the looped items in num1 variable.
    for item in range(1, 13): #This is to loop through the num2 variable.
        print("{} X {} = {}".format(num, item, num * item)) #This is to print the looped items in the num2 variable.