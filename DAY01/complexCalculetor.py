# SIMPLE CALCULETOR (MEMORY HANDALING/)
print('*** WELCOME TO SIMPLE COMPLEX CALCULETOR ***')
input1 = float(input("Enter the 1st value: "))
result = input1

while True:

    print("1. Addition(+): ")
    print("2. Subtraction(-): ")
    print("3. Multiplication(*): ")
    print("4. Divition(/): ")
    print("5. Do you want to exit the app: ")
    choice = input("Enter Your Choice!: ")

    if choice == "1":
        add_number = float(input("Enter the new number that you want to be added: "))
        result = result + add_number
        print(result)
    elif choice == "2":
        add_number = float(input("Enter the new number that you want to be Subtraction: "))
        result = result - add_number
        print(result)
    elif choice == "3":
        add_number = float(input("Enter the new number that you want to be Multiplication: "))
        result = result * add_number
        print(result)
    elif choice == "4":
        add_number = float(input("Enter the new number that you want to be Divition: "))
        result = result / add_number
        print(result)
    elif choice == '5':
        print("Thank you !!!")
        break




