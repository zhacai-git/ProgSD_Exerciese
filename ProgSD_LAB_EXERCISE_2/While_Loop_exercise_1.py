total = 0

while True:
    number = float(input("Enter a number: "))
    total += number

    choice = input("Do you want to add another number? (y/n): ").strip().lower()
    if choice != 'y':
        break

print(f"The total is: {total}")
