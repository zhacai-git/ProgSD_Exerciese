def main():
    user_name = input("Please input your name: ")
    repeat_number = int(input("Please input a number: "))

    if repeat_number < 10:
        for i in range(repeat_number):
            print(user_name)
    else:
        for i in range(3):
            print("Too high")

if __name__ == "__main__":
    main()
