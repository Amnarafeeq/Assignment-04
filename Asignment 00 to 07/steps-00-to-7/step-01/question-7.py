# Define constants for time calculations
days_in_year = 366  # Assuming a leap year with 366 days
hours_in_day = 24  # Number of hours in a day
minutes_in_hour = 60  # Number of minutes in an hour
seconds_in_minute = 60  # Number of seconds in a minute

def cal_sec_in_year():
    # Calculate total seconds in a year by multiplying all time units
    return days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
      
# Execute the function and print the result when the script runs
if __name__ == '__main__':
    print(f"Number of seconds in a year: {cal_sec_in_year()}")
