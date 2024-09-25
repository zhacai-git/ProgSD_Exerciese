def main():
    total = 0

    for i in range(5):
        temp = int(input("Please enter a number (" + str(i+1) + "/5): "))
        confirm = input("Do you want that number to be included? (y/n): ")
        if confirm == "y":
            total += temp

    print("The total is", total)

if __name__ == "__main__":
    main()