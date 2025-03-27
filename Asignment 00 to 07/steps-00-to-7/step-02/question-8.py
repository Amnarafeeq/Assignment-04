max_length = 6  # Maximum allowed length of the list

def shorten_list(lst):
    # Function to remove extra elements if the list exceeds max_length
    while len(lst) > max_length:  # Keep removing elements until the list is within limit
       remove_last_elem = lst.pop()  # Remove the last element
       print(f"Removed {remove_last_elem} from the list.")  # Notify user

def get_list():
    # Function to get user input and create a list
    lst = []  # Initialize an empty list
    elem = input("Please enter an element of the list or press enter to stop. ")  
    while elem:  # Keep adding elements until the user presses enter
        lst.append(elem)  
        elem = input("Please enter an element of the list or press enter to stop. ")  
    return lst  # Return the final list

if __name__ == '__main__':
    lst = get_list()  # Get the user input list
    shorten_list(lst)  # Shorten it if needed
