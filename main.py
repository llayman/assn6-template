from string_stuff import reverse_words, count_vowels


def main():
    while True:
        print("Select an option:")
        print("1. Reverse sentence")
        print("2. Count vowels")
        print("3. Exit")

        option = input("Options: ")
        if option in ["1", "2"]:
            text = input("Enter text: ")
            if option == "1":
                print(reverse_words(text))
            else:
                print(count_vowels(text))
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()