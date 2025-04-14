character = input("Enter a character: ")

if len(character) == 1:
    # Get ASCII value using ord() function
    ascii_value = ord(character)
    print(f"The ASCII value of '{character}' is {ascii_value}")
else:
    print("Please enter only a single character")