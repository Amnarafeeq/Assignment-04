# Define the minimum voting ages for three different locations
Peturksbouipo_voting_age = 16
Stanlau_voting_age = 25
Mayengua_voting_age = 48

def check_voting_age():
    # Take user input for age
    user_age:int = int(input("Enter age to check that you can vote or not:"))

    # Check voting eligibility for Peturksbouipo
    if user_age >= Peturksbouipo_voting_age:
        print("\nYou can vote in Peturksbouipo where the voting age is " + str(Peturksbouipo_voting_age) + ".")
    else:
        print("You can't vote in Peturksbouipo where the voting age is " + str(Peturksbouipo_voting_age) + ".")
    
    # Check voting eligibility for Stanlau
    if user_age >= Stanlau_voting_age:
        print("You can vote in Stanlau where the voting age is " + str(Stanlau_voting_age) + ".")
    else:
        print("You can't vote in Stanlau where the voting age is " + str(Stanlau_voting_age) + ".")

    # Check voting eligibility for Mayengua
    if user_age >= Mayengua_voting_age:
        print("You can vote in Mayengua where the voting age is " + str(Mayengua_voting_age) + ".")
    else:
        print("You can't vote in Mayengua where the voting age is " + str(Mayengua_voting_age) + ".")    

# Call the function to execute the program
check_voting_age()  
