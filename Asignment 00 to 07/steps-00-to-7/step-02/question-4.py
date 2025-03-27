def add_three_copies(lst, data):  
    # Function to add three copies of 'data' to the given list 'lst'
    lst.append(data)  
    lst.append(data)  
    lst.append(data)  

lst = []  # Initialize an empty list

add_data = input("Enter the data to be added: ")  # Take user input for data to be added

if __name__ == '__main__':  
    print(f"Before: {lst}")  # Print list before adding data
    add_three_copies(lst, add_data)  # Call the function to add three copies of input data
    print(f"After: {lst}")  # Print list after adding data
