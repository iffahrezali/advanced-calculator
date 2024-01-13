def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Select an operation: \n 1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division")

while True:
    choice = input("Enter your choice 1-4: ")
    if choice in ('1', '2', '3', '4'):
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("The input is invalid. Please enter a number.")
        
        if choice == '1':
            print(number1, "+" , number2, "=", add(number1,number2))
        elif choice == '2':
            print(number1, "-", number2, "=",substract(number1,number2))
        elif choice == '3':
            print(number1,"x", number2,"=",multiply(number1,number2))
        elif choice == '4':
            print(number1,"/", number2,"=",divide(number1,number2))

        next_calculation = input("Would you like to calculate another? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("The input is invalid.")

