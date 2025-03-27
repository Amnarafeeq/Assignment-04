def access_list(lst, index):
    """
    Function to access an element from a list at a given index.
    Returns the element if index exists, otherwise returns an error message.
    """
    try:
        return lst[index]
    except IndexError:
        return "No index found."

def modify_list(lst, index, add_value):
    """
    Function to modify a list by replacing an element at a given index.
    Returns the updated list or an error message if the index is out of range.
    """
    try:
        lst[index] = add_value
        return lst
    except IndexError:
        return "No index found."

def slice_list(lst, start, end):
    """
    Function to return a slice of the list from start to end index.
    """
    try:
        return lst[start:end]
    except IndexError:
        return "No index found."

def index_game():
    """
    Function to allow the user to access, modify, or slice a list interactively.
    """
    lst = ["apple", "mango", "banana", "orange", "grapes"]
    print("Current List: ", lst)
    
    # Ask the user which operation they want to perform
    operation = input("Do you want to 'access', 'modify', or 'slice' the list? ").strip().lower()

    # Handling "access" operation
    if operation == "access":
        try:
            index = int(input("Enter index number: "))
            print(access_list(lst, index))
        except ValueError:
            print("Invalid input! Please enter a valid index number.")

    # Handling "modify" operation
    elif operation == "modify":
        try:
            index = int(input("Enter index: "))
            add_value = input("Enter the new value: ")
            print(modify_list(lst, index, add_value))
        except ValueError:
            print("Invalid input! Please enter a valid index number.")

    # Handling "slice" operation
    elif operation == "slice":
        try:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(lst, start, end))
        except ValueError:
            print("Invalid input! Please enter valid index numbers.")

    else:
        print("Invalid operation! Please choose 'access', 'modify', or 'slice'.")

# Call the function to execute the program
index_game()
