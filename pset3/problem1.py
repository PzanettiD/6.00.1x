def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    aDict = {}
    for char in secretWord:
        aDict[char] = False
    for i in lettersGuessed:
        if i in aDict:
            aDict[i] = True
    for obj in aDict:
        if aDict[obj] == False:
            return False
    return True
     
print(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))