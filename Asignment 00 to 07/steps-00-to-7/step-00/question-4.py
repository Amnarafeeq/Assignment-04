def age_riddle(age: int):
    # Assign the given age to Anton
    Anton: int = age  

    # Beth is 6 years older than Anton
    Beth: int = Anton + 6  

    # Chen is 20 years older than Beth
    Chen: int = Beth + 20  

    # Drew's age is the sum of Chen's and Anton's ages
    Drew: int = Chen + Anton  

    # Ethan's age is the same as Chen's age
    Ethan: int = Chen  

    # Print out the ages of each person
    print(f"Anton is {Anton}.")
    print(f"Beth is {Beth}.")
    print(f"Chen is {Chen}.")
    print(f"Drew is {Drew}.")
    print(f"Ethan is {Ethan}.")

# Run the function with an initial age of 21 if the script is executed directly
if __name__ == "__main__":
    age_riddle(21)
