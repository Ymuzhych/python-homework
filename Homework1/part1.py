def main():
    # Ask the user for input
    print("Welcome to the Calculator Program!")
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        # Perform calculations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        if num2 != 0:
            division = num1 / num2
        else:
            division = "Undefined (division by zero)"
        
        # Display results
        print("\nResults:")
        print(f"Addition: {num1} + {num2} = {addition}")
        print(f"Subtraction: {num1} - {num2} = {subtraction}")
        print(f"Multiplication: {num1} * {num2} = {multiplication}")
        print(f"Division: {num1} / {num2} = {division}")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()