def repeat_message(msg: str, repeat: int):
    """
    Function to repeat a given message a specified number of times.
    """
    return (msg + " ") * repeat  # Repeat the message with a space in between

def main():
    """
    Main function to get user input and print the repeated message.
    """
    msg = input("Type a message: ")  # Get message input from the user
    repeat = int(input("Enter the number of times to repeat your message: "))  # Get repetition count
    print(repeat_message(msg, repeat))  # Call function and print repeated message

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
