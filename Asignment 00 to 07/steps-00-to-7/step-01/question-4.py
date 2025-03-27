import math  # Import math module for square root function

def length_of_hypotenuse():
    AB = float(input("Enter the length of side AB: "))  # Take input for side AB
    AC = float(input("Enter the length of side AC: "))  # Take input for side AC
    
    BC = math.sqrt(AB**2 + AC**2)  # Calculate the hypotenuse using the Pythagorean theorem
    
    print(f"\033[1;3m{round(BC,2)}\033[0m is the length of the hypotenuse of the triangle")  
    # Display the result in bold & italic with two decimal places

# Run the function if the script is executed directly
if __name__ == "__main__":  
    length_of_hypotenuse()
