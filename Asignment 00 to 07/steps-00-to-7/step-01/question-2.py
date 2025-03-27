def cal_energy():
    speed_of_light = 299792458  # Speed of light in meters per second (m/s)
    
    mass: float = float(input("Enter kilos of mass: "))  # Take mass input from the user in kg
    
    energy = mass * speed_of_light ** 2  # Calculate energy using Einstein's formula: E = mc²
    
    print("\ne = m * C**2...")  # Display the formula
    print(f"m = {mass} kg")  # Display the entered mass
    print(f"C = {speed_of_light} m/s")  # Display the speed of light
    
    print(f"\n\033[1;3m{energy}\033[0m joules of energy!")  # Print the calculated energy in a bold & italic format

# Run the function if the script is executed directly
if __name__ == "__main__":
    cal_energy()
