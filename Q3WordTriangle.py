def main():
    while True:
        word = input("Enter a word (type 'quit' to exit): ")

        if word.lower() == 'quit':
            break

        for i in range(len(word)):
            print(word[:i+1])

    print("Program terminated.")


if __name__ == '__main__':
    main()
