def get_list():  
    # Function to take user input and create a list
    lst = []  # Create an empty list
    elem = input("Please enter an element of the list: ")  
    
    while elem:  # Keep taking input until the user presses enter
        lst.append(elem)  # Add the element to the list
        elem = input("Please enter an element of the list: ")  
    
    return lst  # Return the final list

def get_list_elements(lst):  
    # Function to print the list elements
    if len(lst) == 0:  # Check if the list is empty
        print("The list is empty. You must enter at least one element.")  
    else:  
        print("Here is a list:", lst)  # Print the full list

if __name__ == '__main__':  
    lst = get_list()  # Get the list from user input
    get_list_elements(lst)  # Display the list
