def main():
    while True:
        word = input("Enter a word (type 'quit' to exit): ")

        if word.lower() == 'quit':
            break

        length = len(word)
        print(f"The length of the word '{word}' is: {length}")

    print("Program terminated.")


if __name__ == '__main__':
    main()
