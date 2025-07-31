def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    """Main function to handle temperature conversion."""
    print("Temperature Converter")
    print("---------------------")

    while True:
        choice = input("Convert from (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (Enter 'C' or 'F', or 'Q' to quit): ").upper()

        if choice == 'Q':
            print("Exiting temperature converter.")
            break
        elif choice == 'C':
            try:
                temp_c = float(input("Enter temperature in Celsius: "))
                temp_f = celsius_to_fahrenheit(temp_c)
                print(f"{temp_c}°C is equal to {temp_f:.2f}°F")
            except ValueError:
                print("Invalid input. Please enter a numerical value for temperature.")
        elif choice == 'F':
            try:
                temp_f = float(input("Enter temperature in Fahrenheit: "))
                temp_c = fahrenheit_to_celsius(temp_f)
                print(f"{temp_f}°F is equal to {temp_c:.2f}°C")
            except ValueError:
                print("Invalid input. Please enter a numerical value for temperature.")
        else:
            print("Invalid choice. Please enter 'C', 'F', or 'Q'.")

if __name__ == "__main__":
    main()
