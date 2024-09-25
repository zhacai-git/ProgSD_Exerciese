def main():
    age = int(input("How old are you: "))

    if age >= 18:
        print("You can vote.")
    elif age == 17:
        print("You can learn how to drive.")
    elif age == 16:
        print("You can buy a lottery ticket.")
    elif age < 16:
        print("You can go Trick-or-Treating.")

if __name__ == '__main__':
    main()