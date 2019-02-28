# Introduction
In this problem set, you'll implement two versions of a wordgame!

### Rules:
#### Dealing:
	- A player is dealt a hand of n letters chosen at random.

	- The player arranges the hand into as many words as they want out of the letters, using each letter at most once.

	- Some letters may remain unused (these won't be scored).

#### Scoring:
	- The score for the hand is the sum of the scores for each word formed.

	- The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.

	- Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary "SCRABBLE_LETTER_VALUES" that maps each lowercase letter to its Scrabble letter value.

	- For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

	- As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters) 

## Problem 1 - Word Scores:
The first step is to implement some code that allows us to calculate the score for a single word. The function getWordScore should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.

## Problem 2 - Dealing with Hands:
Your task is to implement the function updateHand, which takes in two inputs - a hand and a word (string). updateHand uses letters from the hand to spell the word, and then returns a copy of the hand, containing only the letters remaining.

## Problem 3 - Valid Words:
Write a function to verify that a word given by a player obeys the rules of the game. A valid word is in the word list; and it is composed entirely of letters from the current hand.

## Problem 4 - Hand Length:
You'll need to implement the helper calculateHandlen function, which takes a hand as input and returns the length of the hand.

## Problem 5 - Playing a Hand:
Implement a function that allows the user to play one hand, as follows:

	- The hand is displayed.
	- The user may input a word or a single period (the string ".") to indicate they're done playing.
	- Invalid words are rejected, and a message is displayed asking the user to choose another word until they enter a valid word or "."
	- When a valid word is entered, it uses up letters from the hand.
	- After every valid word: the score for that word is displayed, the remaining letters in the hand are displayed, and the user is asked to input another word.
	- The sum of the word scores is displayed when the hand finishes.
	- The hand finishes when there are no more unused letters or the user inputs a ".".

## Problem 6 - Playing a Game:
A game consists of playing multiple hands. We need to implement one final function to complete our word-game program. Write the code that implements the playGame function. 
	
	- Asks the user to input 'n' or 'r' or 'e'.
	- If the user inputs 'n', let the user play a new (random) hand.
	- If the user inputs 'r', let the user play the last hand again.
	- If the user inputs 'e', exit the game.
	- If the user inputs anything else, tell them their input was invalid.

## Problem 7 - You and your Computer:
Write a function that re-implements that of the Problem 6,but adding the capability to allow the computer to play

## Certificate:

![Certificate](https://i.imgur.com/DJtSNHO.jpg)



.   
