def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ""
    for char in secretWord:
        if not char in lettersGuessed:
            result += "_ "
        else:
            result += char
    return result
        
print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))