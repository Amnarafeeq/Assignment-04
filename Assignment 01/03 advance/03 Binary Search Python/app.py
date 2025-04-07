def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr_input = input("Enter a sorted list of numbers (comma-separated): ")
    arr = list(map(int, arr_input.split(',')))  # String → int list
    arr.sort()
    print(f"Sorted Array: {arr}")
    
    target = int(input("Enter the number you want to search for: "))
    
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Number {target} found at index {result}")
    else:
        print(f"Number {target} not found in the list")
