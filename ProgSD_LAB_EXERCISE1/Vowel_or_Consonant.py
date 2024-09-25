VOWEL = "aeiou"
def main():
    letter = input("Enter a letter: ")

    letter = letter.lower()[0]

    if letter in VOWEL:
        print("The letter you entered is a vowel")
    elif letter == 'y':
        print("Sometimes y is a vowel, and sometimes y is a consonant")
    else:
        print("The letter you entered is a consonant")

if __name__ == "__main__":
    main()