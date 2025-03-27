def feet_to_inches():
    feet = float(input("Enter the length in feet: "))  # Take length input from the user in feet
    
    inches = feet * 12  # Convert feet to inches (1 foot = 12 inches)
    
    print(f"\033[1;3m{feet}\033[0m feet is equal to \033[1;3m{round(inches,2)}\033[0m inches")  
    # Print the result in bold & italic format with two decimal places

# Run the function if the script is executed directly
if __name__ == "__main__":
    feet_to_inches()
