# Define the minimum age for adulthood
adult_age = 18  

def is_adult(age: int):
    """
    Function to check if a person is an adult based on the given age.
    """
    if age >= adult_age:
        return True  # Returns True if the age is 18 or above
    return False  # Returns False if the age is below 18

# Take user input and convert it to an integer
age = int(input("Enter your age: "))

# Print whether the user is an adult or not
print(is_adult(age))
