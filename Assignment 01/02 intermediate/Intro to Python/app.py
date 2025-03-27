# Dictionary containing planet names and their gravity multipliers relative to Earth
planets_weights = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.360,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.140
}

def weight_on_planets():
    """
    This function calculates a user's weight on different planets based on Earth's weight.
    """
    
    # Get user input for weight on Earth
    weight_on_earth = float(input("Enter your weight on Earth: "))
    
    # Get user input for planet name (title() ensures first letter is uppercase)
    planet_name = input("Enter planet name: ").title()
    
    # Check if the planet is in the dictionary
    if planet_name in planets_weights:
        weight_on_planet = weight_on_earth * planets_weights[planet_name]  # Calculate weight on selected planet
        print(f"Your weight on {planet_name} is {round(weight_on_planet, 2)} kg")  # Print result with rounded value
    else:
        print("Invalid planet name. Please enter a correct planet name.")  # Error message for invalid input

# Call the function to execute
weight_on_planets()
