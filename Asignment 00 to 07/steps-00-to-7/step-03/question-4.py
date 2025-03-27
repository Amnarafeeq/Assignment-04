# Minimum height required to be eligible for the ride
min_height = 50

# Function to check if a person meets the height requirement
def check_height():
    while True:  # Infinite loop to repeatedly ask for input
        # Prompt user to enter their height
        entered_height = input("\nHow tall are you? (Enter to exit): ")

        # Check if the user wants to exit
        if entered_height == "":
            print("\nExiting program... Have a great day!")
            break  # Exit the loop if no input is given

        # Convert the input to float for comparison
        entered_height = float(entered_height) 

        # Check if the height meets the requirement
        if entered_height >= min_height:
            print(f"\nGreat! You're {entered_height} tall, so you're tall enough to ride!")
        else:
            print(f"\nOops! You're {entered_height} tall, which is below the required {min_height}. Maybe next year!")

# Call the function to start the height check process
check_height()
