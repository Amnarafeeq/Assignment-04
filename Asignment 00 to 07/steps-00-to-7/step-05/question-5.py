# Function to perform a countdown from 10 to 1
def liftoff():
    # Loop from 10 down to 1 in reverse order
    for i in range(10, 0, -1):
        print(i)  # Print the current countdown number

    # Print liftoff message after the countdown ends
    print("Liftoff!")    

# Call the function to execute the countdown
liftoff()
