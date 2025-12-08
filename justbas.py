# A simple function to greet the user
def greet(name):
    print(f"\nHello, {name}! Welcome to Python basics.\n")

# A function to add two numbers
def add_numbers(a, b):
    return a + b

# Program starts here
name = input("Enter your name: ")
greet(name)

while True:
    print("--- MENU ---")
    print("1. Add two numbers")
    print("2. Check if a number is even or odd")
    print("3. Say Hello")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = add_numbers(num1, num2)
        print(f"Result: {num1} + {num2} = {result}\n")

    elif choice == "2":
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print(f"{num} is EVEN\n")
        else:
            print(f"{num} is ODD\n")

    elif choice == "3":
        print(f"Hello, {name}! 👋\n")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        break

    else:
        print("Invalid option, please try again.\n")
