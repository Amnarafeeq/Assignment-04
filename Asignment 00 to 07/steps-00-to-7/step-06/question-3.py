def count_even():
    lst = []  # List to store user input numbers
    count = 0  # Counter for even numbers

    while True:
        user_inp = input("Enter an integer or press Enter to stop: ")  # Prompt user for input

        if user_inp == "":  # Check if user wants to stop
            print(f"\nYour final list: {lst}")  
            print(f"Total even numbers in the list: {count}")  # Print final count of even numbers
            print("Thank you for using the program!")
            break  # Exit the loop
        
        user_inp = int(user_inp)  # Convert input to integer
        lst.append(user_inp)  # Add the number to the list

        count = 0  # Reset the even number counter
        for num in lst:  # Loop through the list
            if num % 2 == 0:  # Check if the number is even
                count += 1  # Increment the even number count

        print(f"Current list: {lst}")  # Display the updated list
        print(f"Even numbers so far: {count}\n")  # Show the current count of even numbers

# Run the function
count_even()
