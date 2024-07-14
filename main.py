#Welcome to my Guessing Game! To play, you must enter the row and column of your choice twice. If the two characters that are guessed are the same, they stay flipped over. If not, you must continue guessing until each duo of characters is guessed. You also have the option to use a hint which shows the location of one character
#Importing different functions to access randomizers, color changers, and timers.
import random
import os
import time
from termcolor import colored
import colorama
from termcolor import colored
from colorama import Fore, Back, Style
import termcolor 
import colored, cprint


#The variables function is used every time the user decides to start a new game. It creates a new grid based on their input and resets most repeated variables back to their neutral value.
def variables():
	#Globaling different variables so they can be used in different functions
	global wrongGuesses
	global rightGuesses
	global characterList
	global xList
	global guessedRows
	global guessedColumns
	global twoGuessesRows
	global twoGuessesCols
	global correctGuessedRows
	global correctGuessedCols
	global mainList
	global middleOfGrid
	characterList = []
	alreadyInList = ''
	#Depending on if the user's entered grid size is even or odd the program creates a different list of characters
	if gridSize % 2 == 0:
		lengthOfList = (gridSize * gridSize)/2
	else: lengthOfList = ((gridSize * gridSize) - 1)/2
	lengthOfList = int(lengthOfList)
	#This group of code creates a list of random characters based on the size of the grid
	while len(characterList) < lengthOfList:
		alreadyInList = ''
		randomLetterAscii = random.randint(65,122) 
		#This prevents the characters from being "x" or "X" which are used in the empty grid
		if randomLetterAscii != 120 and randomLetterAscii != 88:
			randomLetter = chr(randomLetterAscii)
			for num in range(len(characterList)):			
				if characterList[num] == randomLetter:
					alreadyInList = "yes"
			if alreadyInList != "yes":
				characterList.insert(0,randomLetter)
	#This doubles each character in the list so that each character has a pair to be used in the game
	for num in range(lengthOfList):
		characterList.append(characterList[num])
	#If the grid size is odd an X is added to the end of the list
	if gridSize % 2 != 0:
		characterList.append("X")
	mainList = []
	tempList = []
	#This creates the top list which shows the column numbers
	for num in range(gridSize + 1):
		tempList.insert(0,(gridSize - num))
	mainList.insert([0][0],tempList)
	tempList = []
	#This group of code creates the main list by randomizing the characters in each row
	for num in range(gridSize):
		tempList = []
		for num2 in range(gridSize):
			tempChoice = random.randint(0,(len(characterList))-1)
			tempList.append(*characterList[tempChoice])
			characterList.pop(tempChoice)
		#This adds in the row numbers to the left of the rows.
		tempList.insert(0,(num+1))
		mainList.append(tempList)
	xList = []
	#This group of code creates a new list where each value of the main list is instead "x"
	for num in range(len(mainList)):
		tempList = []
		for num2 in range(len(mainList[num])):
			tempList.insert(0,"x")
		xList.append(tempList)
	#This loop adds in the row and column numbers to the "x" list
	for num in range(gridSize + 1):
		xList[0][num] = num
		xList[num][0] = num
	#This if statement creates variables if the grid size is odd so that the middle value can be replaced by "X"
	if gridSize % 2 != 0:
		for num in range(gridSize+1):
			for num2 in range(gridSize+1):
				if mainList[num][num2] == "X":
					tempXRow = num
					tempXCol = num2		
					break
	#Using the variables established in the last if statement, this statement swaps the capital X with the middle character
	if gridSize % 2 != 0:
		middleOfGrid = int((gridSize + 1)/2)
		replacementCharacter = mainList[middleOfGrid][middleOfGrid]
		mainList[tempXRow][tempXCol] = replacementCharacter
		XVariable = "X"
		colorMagenta = colored.fg('magenta')
		colorWhite = colored.fg('white')
		mainList[middleOfGrid][middleOfGrid] = (colorMagenta + XVariable + colorWhite)
		xList[middleOfGrid][middleOfGrid] = (colorMagenta + XVariable + colorWhite)
	#These reset the variables used each game
	guessedRows = []
	guessedColumns = []
	twoGuessesRows = []
	twoGuessesCols = []
	correctGuessedRows = []
	correctGuessedCols = []
	wrongGuesses = 0
	rightGuesses = 0

#The instructions function displays instructions to the user
def instructions():
	print("Welcome to my Guessing Game! To play, you must enter the row and column of your choice twice. If the two characters that are guessed are the same, they stay flipped over. If not, you must continue guessing until each duo of characters is guessed. You also have the option to use a hint which shows the location of one character.\n")

#The mainCode function is used each turn the player takes. It takes two inputs from the user and compares them to the grid established in the variables function
def mainCode():
	global wrongGuesses
	global rightGuesses
	global middleOfGrid
	os.system('clear')
	#Prints the "x" list
	for num in range(len(xList)):
		print(*xList[num])
	twoGuessesRows = []
	twoGuessesCols = []
	guessedRows = []
	guessedColumns = []
	#This loop asks the user if they would like a hint
	while True:
		hintInput = (input("Would you like a hint? y/n : "))
		if hintInput == "y":
			#This calculates a position that hasn't already been answered
			while True:
				randomColumn = random.randint(1,gridSize)
				randomRow = random.randint(1,gridSize)
				if xList[randomRow][randomColumn] == "x":
					break
			#This colors the text to make it easier to read
			colorCyan = colored.fg('cyan')
			colorWhite = colored.fg("white")
			hintGrid = mainList[randomRow][randomColumn]
			hintGridColored = (colorCyan + hintGrid + colorWhite)
			xList[randomRow][randomColumn] = hintGridColored
			os.system('clear')
			for num in range(len(xList)):
				print(*xList[num])
			xList[randomRow][randomColumn] = "x"
			break
		elif hintInput == "n":
			break
		else: print("Please enter a valid option")
	#This loop gets two row and column values from the user to be used in the guessing game
	while len(twoGuessesRows) < 2:
		while True:
			alreadyGuessed = "no"
			while True:
				col = input("Please enter a column: ")
				if col.isdigit():
					col = int(col)
					if col > 0 and col <= gridSize:
						break
					else: print("Please enter a valid input")
				else: print("Please enter a valid input")
			while True:
				row = input("Please enter a row: ")
				if row.isdigit():
					row = int(row)
					if row > 0 and row <= gridSize:
						break
					else: print("Please enter a valid input")
				else: print("Please enter a valid input")
			#If the user guesses the same combination twice in a row it gives them an error message
			for num in range(len(guessedRows)):
				if guessedRows[num] == row and guessedColumns[num] == col:
					alreadyGuessed = "yes"
					print("You cannot guess the same row and column twice in one turn!")
			#If the user has already correctly guessed at least one of the values it gives them an error message
			for num in range(len(correctGuessedRows)):
				if correctGuessedRows[num] == row and correctGuessedCols[num] == col:
					alreadyGuessed = "yes"
					print("You have already guessed this correctly!")
			#If the user guesses the middle value they receive an error message
			if gridSize % 2 != 0:
				if col == middleOfGrid and row == middleOfGrid:
					alreadyGuessed = "yes"
					print("You cannot guess the middle value!")
			if alreadyGuessed == "yes":
				print("")
			else: 
				#adds the values to a list
				guessedRows.insert(0,row)
				guessedColumns.insert(0,col)
				twoGuessesRows.append(row)
				twoGuessesCols.append(col)
				break
	guess1Row = twoGuessesRows[0]
	guess1Col = twoGuessesCols[0]
	guess2Row = twoGuessesRows[1]
	guess2Col = twoGuessesCols[1]
	os.system('clear')
	#checks to see if the user guessed correctly or not
	if mainList[guess1Row][guess1Col] == mainList[guess2Row][guess2Col]:
		color = colored.fg("green")
		color2 = colored.fg("white")
		right1 = mainList[guess1Row][guess1Col]
		right1color = (color + right1 + color2)
		right2 = mainList[guess2Row][guess2Col]
		right2color = (color + right2 + color2)
		xList[guess1Row][guess1Col] = right1color
		xList[guess2Row][guess2Col] = right2color
		#adds correct guesses to a list to make sure they don't get guessed again
		correctGuessedRows.insert(0,twoGuessesRows[0])
		correctGuessedCols.insert(0,twoGuessesCols[0])
		correctGuessedRows.insert(1,twoGuessesRows[1])
		correctGuessedCols.insert(1,twoGuessesCols[1])
		for num in range(len(xList)):
			print(*xList[num])
		xList[guess1Row][guess1Col] = right1
		xList[guess2Row][guess2Col] = right2
		print("Well Done! You guessed correctly")
		rightGuesses += 1
		time.sleep(1.5)
	else: 
		print("Incorrect, here is what you guessed")
		wrongGuesses += 1
		wrong1 = mainList[guess1Row][guess1Col]
		color = colored.fg("red")
		color2 = colored.fg("white")
		wrong1 = (color + wrong1 + color2)
		wrong2 = mainList[guess2Row][guess2Col]
		wrong2 = (color + wrong2 + color2)
		#shows the user a red x to show that they got it wrong
		xList[guess1Row][guess1Col] = wrong1
		xList[guess2Row][guess2Col] = wrong2
		for num in range(len(xList)):
			print(*xList[num])
		time.sleep(1.5)
		xList[guess1Row][guess1Col] = "x"
		xList[guess2Row][guess2Col] = "x"
		
#the menu function is where all the other functions are used. It is also where the user decides the grid size and if they would like to play again or quit
def menu():
	turns = 0
	global gridSize
	instructions()
	#This loop is where the user inputs the grid size they would like
	while True:
		while True:
			gridSize = (input("Please enter what you would like the length and height of the grid to be: "))
			if gridSize.isdigit():
				gridSize = int(gridSize)
				if gridSize < 11 and gridSize > 1:
					break
				else: print("Please enter a valid number")
			else: print("Please enter a valid number")
		variables()
		#This loop is where the main game function is used
		while True:
			print("1. Guess\n2. Quit")
			choice = input("Choice: ")
			if choice == "1":
				mainCode()
				time.sleep(2)
				turns += 1
				os.system('clear')
				#This prints out how many right and wrong guesses the user made
				if mainList == xList:
					print("You won! It took you", turns, "turns!\nYou made", rightGuesses,"right guesses and", wrongGuesses, "wrong guesses")
					break
			#Quit option
			elif choice == "2":
				break
				print("Thank you for playing!")
				print("You made", rightGuesses, "right guesses and", wrongGuesses, "wrong guesses")
			else: print("Please input a valid option")		
		restart = input("Would you like to play again? y/n : ")
		if restart == "n":
			print("See you next time!")
			break
menu()
