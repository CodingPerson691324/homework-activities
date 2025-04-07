checker = input('Enter a character: ')

if checker.isalpha():
    print(f"{checker} is an alphabet character")
elif checker.isnumeric():
    print(f"{checker} is a number")
else:
    print(f"{checker} is neither an alphabet character nor a number")