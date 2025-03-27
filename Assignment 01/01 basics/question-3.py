def liftoff():
    """
    Counts down from 10 to 1 and then prints 'liftoff!'.
    """
    for i in range(10, 0, -1):  # Loop from 10 down to 1
        print(i)  # Print the current countdown number

    print("liftoff!")  # Print the final message after countdown is complete

# Call the function to execute the countdown
liftoff()
