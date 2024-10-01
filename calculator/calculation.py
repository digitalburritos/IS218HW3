'''
Primitive way to have a history of calculations - commented out
'''

'''
# History to store calculations
history = []

# Function to perform calculation
def calculate(num1, num2, operation):
    # Perform the selected operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero")
            return None
        result = num1 / num2
    else:
        print("Error: Invalid operation. Please use +, -, *, or /.")
        return None
    
    # Save to history
    history.append(f"{num1} {operation} {num2} = {result}")
    return result

# Function to show last calculation
def show_last():
    if history:
        return history[-1]
    else:
        return "No calculations yet."

# Function to clear history
def clear_history():
    history.clear()

# Main loop to run the calculator
def main():
    while True:
        try:
            # Get user input
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            
            # Perform the calculation
            result = calculate(num1, num2, operation)
            if result is not None:
                print(f"Result: {result}")
                print(f"Last calculation: {show_last()}")
        
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
        
        # Ask the user if they want to continue
        cont = input("Do you want to perform another calculation? (yes/no): ").lower()
        if cont != 'yes':
            break
    
    # Show full history and clear
    print("Calculation History:")
    for calc in history:
        print(calc)
    clear_history()
    print("History cleared.")

# Run the calculator
if __name__ == "__main__":
    main()

'''