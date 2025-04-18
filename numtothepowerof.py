def calculate_power(base, exponent):
  return base ** exponent

def main():
  base = float(input("Enter a number: "))
  exponent = int(input("Enter the amount of times you want to multiply it(power): "))

  result = calculate_power(base, exponent)
  print(f"{base} raised to the power of {exponent} is: {result}")

if __name__ == "__main__":
  main()