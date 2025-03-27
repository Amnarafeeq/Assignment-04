def fav_animal():
    # Ask the user for their favorite animal
    animal_name = input("Enter your favorite animal: ")  
    
    # Print the favorite animal in bold and italic using ANSI escape codes
    print(f"My favorite animal is \033[1m\033[3m{animal_name}\033[0m.")  

# Run the function if the script is executed directly
if __name__ == "__main__":
    fav_animal()
