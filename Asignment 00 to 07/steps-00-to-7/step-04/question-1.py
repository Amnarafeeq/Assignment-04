def count_num():
    numbers_count = {}  # Dictionary to store counts

    while True:
        get_nums = input("Enter number (or press enter to stop): ")
        if get_nums == "":  # Stop if user enters nothing
            print("Exiting program...")
            break
        
        get_nums = int(get_nums)  # Convert input to integer

        # Update count in dictionary
        if get_nums in numbers_count:
            numbers_count[get_nums] += 1
        else:
            numbers_count[get_nums] = 1

    # Print the counts after exiting loop
    for num, count in numbers_count.items():
        print(f"{num} appears {count} times.")

count_num()
