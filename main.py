from string_stuff import reverse_words, count_vowels, is_palindrome


def main():
    while True:
        print("Select an option:")
        print("1. Reverse sentence")
        print("2. Count vowels")
        print("3. Palindrome check")
        print("4. Exit")

        option = input("Option: ")
        match option:
            case "1":
                print(reverse_words(input("Enter text: ")))
            case "2":
                print(count_vowels(input("Enter text: ")))
            case "3":
                print(is_palindrome(input("Enter text: ")))
            case  "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid option")

if __name__ == '__main__':
    main()
