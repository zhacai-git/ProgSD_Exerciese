VOWEL = ['a', 'e', 'i', 'o', 'u']
def main():

    original_word = input("Please input a word: ")
    lower_word = original_word.lower()

    if lower_word[0] in VOWEL:
        lower_word += 'way'
    else:
        lower_word = lower_word[1:] + lower_word[0] + 'ay'
    print(lower_word)

if __name__ == "__main__":
    main()