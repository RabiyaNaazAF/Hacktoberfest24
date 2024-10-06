def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    
    return list(duplicates)

# Get user input for the list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")

try:
    # Convert input into a list of integers
    numbers = list(map(int, user_input.split()))
    
    duplicates = find_duplicates(numbers)
    
    if duplicates:
        print(f"Duplicate numbers: {duplicates}")
    else:
        print("No duplicate numbers found.")
except ValueError:
    print("Please enter valid numbers.")
