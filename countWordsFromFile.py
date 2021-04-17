def countWordsFromFile():
    fileName = input("Enter the name of the file: ")
    f = open(fileName, "r")
    wordLength = 0

    for line in f:
        words = line.split()
        wordLength = wordLength + len(words)

    print("The number of words in this file is", wordLength)

countWordsFromFile()