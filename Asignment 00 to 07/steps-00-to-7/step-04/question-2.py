# Function to save numbers in a phone book
def save_num_in_phone_book():
    phone_book = {}  # Dictionary to store names and numbers
    while True:
        enter_name = input("Enter name: ")  # Prompt user to enter a name

        if enter_name == "":  # If input is empty, exit the loop
            break

        enter_num = int(input("Enter number: "))  # Prompt user to enter a phone number
        phone_book[enter_name] = enter_num  # Store the name and number in the dictionary
        return phone_book  # Return the dictionary (but it exits after the first entry)

# Function to print all contacts in the phone book
def print_phone_book(phone_book):
    for name in phone_book:
        print(f"This is the name {name} with this Phone number: {phone_book[name]} ")

# Function to find a number by name in the phone book
def get_number(phone_book):
    while True:
        name = input("Enter Name to find Number: ")  # Ask for a name to search
        if name == "":  # Exit loop if input is empty
            break
        if name in phone_book:  # Check if name exists in the dictionary
            print(phone_book[name])        
        else: 
            print(f"{name} is not in the phone book.")  

# Main function to manage the phone book operations
def main():
    phone_book = save_num_in_phone_book()  # Call function to save numbers
    print_phone_book(phone_book)  # Display saved contacts
    get_number(phone_book)  # Allow user to search for a contact

# Run the program when executed
if __name__ == "__main__":
    main()
