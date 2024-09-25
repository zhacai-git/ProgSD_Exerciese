def main():
    direction = input("Which direction to you want to count (up/down): ")
    if direction == "up":
        top_number = int(input("Please input the top number: "))
        for i in range(top_number):
            print(i+1)
    elif direction == "down":
        bottom_number = int(input("Please input the bottom number that below 20: "))
        if bottom_number < 20:
            for i in range(20, bottom_number - 1, -1):
                print(i)
    else:
        print("I don't understand")

if __name__ == "__main__":
    main()