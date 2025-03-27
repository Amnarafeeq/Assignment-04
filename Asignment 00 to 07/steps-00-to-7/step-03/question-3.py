# Function to check if a given year is a leap year using nested conditions
def is_leap_year():
    # Take user input for the year
    leap_year: int = int(input("Enter a year to check if it's a leap year or not: "))

    # Check if the year is divisible by 4
    if leap_year % 4 == 0:
        # Check if the year is divisible by 100
        if leap_year % 100 == 0:
            # Check if the year is divisible by 400
            if leap_year % 400 == 0:
                print(f"{leap_year} is a leap year.")
            else:
                print(f"{leap_year} is not a leap year.")    
        else:
            print(f"{leap_year} is a leap year.")    
    else:
        print(f"{leap_year} is not a leap year.")

# Call the function to execute the program
is_leap_year()

# ----------------------------------------

# Alternative way to check for a leap year using a simplified condition
def check_leap_year():
    # Take user input for the year
    leap_year: int = int(input("Enter a year to check if it's a leap year or not: "))

    # Check the leap year condition using logical operators
    if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0:
        print(f"{leap_year} is a leap year.")
    else:
        print(f"{leap_year} is not a leap year.")

# Call the function to execute the program
check_leap_year()
