def cal_temp():
    # Ask the user to enter the temperature in Fahrenheit
    temp = float(input("Enter temperature in Fahrenheit: "))  
    
    # Convert Fahrenheit to Celsius using the formula
    celsius: float = (temp - 32) * 5.0 / 9.0  
    
    # Print the converted temperature in bold and italic using ANSI escape codes
    print(f"{temp}°F in Celsius is: \033[1m\033[3m{celsius}°C\033[0m")  

# Run the function if the script is executed directly
if __name__ == "__main__":
    cal_temp()
