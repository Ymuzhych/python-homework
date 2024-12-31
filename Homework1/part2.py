def main():
    # Welcome message
    print("Temperature Converter: Celsius to Fahrenheit")
    
    # Ask the user for the temperature in Celsius
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        
        # Convert Celsius to Fahrenheit
        fahrenheit = celsius * 9/5 + 32
        
        # Display the result
        print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
