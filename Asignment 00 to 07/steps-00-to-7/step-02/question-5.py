def get_first_element(lst):  
    # Function to print the first element of the list
    if len(lst) == 0:  # Check if the list is empty
        print("The list is empty. You must enter at least one element.")  
    else:  
        print(lst[0])  # Print the first element of the list

def get_lst():  
    # Function to take user input and create a list
    lst = []  # Initialize an empty list
    elem: str = input("Please enter an element of the list or press enter to stop: ")  
    
    while elem != "":  # Keep taking input until the user presses enter
        lst.append(elem)  # Add the entered element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")  
    
    return lst  # Return the final list

if __name__ == '__main__':  
    lst = get_lst()  # Get the list from user input
    get_first_element(lst)  # Print the first element of the list
