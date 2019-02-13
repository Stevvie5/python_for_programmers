def wordFreq(fileName):
    fileInput = open(fileName)
    fileText = fileInput.read()
    fileInput.close()

    words = fileText.split()
    processedWords = {}
    for word in words:
        processedWord = ''
        for character in word:
            character = character.lower()
            if character in ['?','!',',','.',';',':']:
                character = ''
            processedWord += character
        processedWords[processedWord] = processedWords.get(processedWord, 0) +1

    for (key, value) in processedWords.items():
        print(key, value)
wordFreq('sample.txt')
