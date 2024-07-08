def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    print("Welcome to the Python Calculator!")
    
    while True:
        print("\nSelect operation:")
        print(add)
        print(subtract)
        print(multiply)
        print(divide)
        print(exit)
        
        choice = input("Enter choice (add/subtract/multiply/divide/exit): ").strip()
        print(f"User choice: {choice}")  # Debugging print
        
        if choice in ['add', 'subtract', 'multiply', 'divide', 'exit']:
            if choice == 'exit':
                print("Exiting the calculator. Goodbye!")
                break

            try:
                num1 = float(input("Enter first number: ").strip())
                print(f"First number: {num1}")  # Debugging print
                num2 = float(input("Enter second number: ").strip())
                print(f"Second number: {num2}")  # Debugging print
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if choice == 'add':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == 'subtract':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 'multiply':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 'divide':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    main()
