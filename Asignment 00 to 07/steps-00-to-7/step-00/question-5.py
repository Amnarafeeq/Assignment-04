def perimeter_of_triangle():
    # Ask the user to enter the lengths of the three sides of the triangle
    a = float(input("Enter the first side of the triangle: "))
    b = float(input("Enter the second side of the triangle: "))
    c = float(input("Enter the third side of the triangle: "))

    # Calculate the perimeter by adding all three sides
    perimeter: float = a + b + c

    # Display the calculated perimeter
    print(f"The perimeter of the triangle is {perimeter}")

# Run the function if the script is executed directly
if __name__ == "__main__":
    perimeter_of_triangle()
