def stringCount(fileName, text):
    fileInput = open(fileName, 'r')
    fileText = fileInput.read()
    fileInput.close()

    return fileText.count(text)