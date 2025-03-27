# Function to allow the user to buy fruits and calculate the total cost
def buy_fruits():
    # Dictionary containing fruit names as keys and their prices as values
    fruits = {'Mango': 1.5, 'Apple': 50, 'Jackfruit': 80, 'Kiwi': 1, 'Strawberry': 1.5, 'Banana': 5, "Litchi": 21}
    
    total_cost = 0  # Variable to store the total cost

    # Loop through each fruit in the dictionary
    for name in fruits:
        price = fruits[name]  # Get the price of the current fruit

        while True:
            try:
                # Ask the user how many of the current fruit they want to buy
                fruit_bought = int(input(f"How many {name} do you want to buy? "))  
                break  # Exit loop if input is valid
            except ValueError:
                print("Enter a valid number.")  # Handle non-integer inputs
            
        total_cost += (price * fruit_bought)  # Calculate and add the cost to total

    # Display the total cost of all fruits purchased
    print(f"Your total cost is ${total_cost}")

# Call the function to execute the fruit-buying process
buy_fruits()
