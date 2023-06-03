def main():
    while True:
        word = input("Enter a word (type 'quit' to exit): ")

        if word.lower() == 'quit':
            break

        reversed_word = word[::-1]
        print(f"The word '{word}' in reverse is: {reversed_word}")

    print("Program terminated.")


if __name__ == '__main__':
    main()
