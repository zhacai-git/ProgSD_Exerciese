def main():
    first_name = input("Please enter your first name: ")
    if len(first_name) >= 5:
        print(first_name.lower())
    else:
        surname = input("Please enter your surname: ")
        print((first_name + surname).upper())

if __name__ == "__main__":
    main()