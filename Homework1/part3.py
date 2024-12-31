def main():
    # Welcome message
    print("Number Converter Program")
    
    # Ask the user to input a number
    user_input = input("Enter a number: ")
    
    try:
        # Convert the input to different types
        as_int = int(float(user_input))  # Convert to float first to handle decimal inputs
        as_float = float(user_input)
        as_string = str(user_input)
        
        # Print the results
        print("\nConversions:")
        print(f"Integer: {as_int} type: {type(as_int)}")
        print(f"Float: {as_float} type: {type(as_float)}")
        print(f"String: '{as_string}' type: {type(as_string)}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
