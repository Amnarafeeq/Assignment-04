# Function to check the stock of a given fruit
def num_in_stock(fruit):
    """
    Returns the number of fruits in stock based on the given fruit name.
    """
    if fruit == "mango":
        return 560  # Stock for mango
    elif fruit == "apple":
        return 891  # Stock for apple
    elif fruit == "kiwi":
        return 20   # Stock for kiwi
    else:
        return 0    # If the fruit is not found, return 0

# Main function to take user input and check stock
def main():
    """
    Prompts the user to enter a fruit name and checks its stock.
    """
    fruit = input("Enter a fruit: ").lower()  # Convert input to lowercase for consistency
    stock = num_in_stock(fruit)  # Get stock count

    if stock == 0:
        print("This fruit is not in stock.")  # Output if the fruit is unavailable
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)  # Print available stock

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
