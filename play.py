"""The user is asked to enter the word the word_length (max_word length is 15) and No. of guesses.
   Then the user starts to make guess on every wrong score and no. of guesses are decreased by 1.
   If the entered letter matches with the word retrieved then based on position of entered letter 
   in word the spaces are filled. """
   
   






import random
import os
max_length,word=0,'' 
length=list_word=already_guessed=0

Hangmanpics = ['''
  
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']


print( """
		  |       |   |-----| |\    |  |-------  |\    /|  |------| |\    |          
		  |       |   |     | | \   |  |         | \  / |  |      | | \   |                    
		  |-------|   |-----| |  \  |  |         |  \/  |  |------| |  \  |                    
		  |       |   |     | |   \ |  |   ----| |      |  |      | |   \ |                    
		  |       |   |     | |    \|  |_______| |      |  |      | |    \|                    
		  """)
		

def takeInput():
	
		c=input("enter max word length(max word_length is 15):    \n")
		return c

def takeInput1():
	
		c=input("Enter already guessed words:   \n")
		return c	


#findword() selects a random word of length specified by the user from the dataset 
def findword():
	max_length=takeInput()
	global length
	length=int(max_length)

	file_name=str(max_length)+".txt"
	fp=open(file_name,"r")
	no_line=0
	for line in fp:
		no_line+=1
	pon=random.randrange(0,no_line)	#pon contains a number in range(0,filesize)
	print(pon)
	fileinfo=os.stat(file_name)
	size_file=fileinfo.st_size
	print(size_file,no_line)
	k=size_file/no_line
	print(k)
	if pon!=0 :
		fp.seek((k*(pon-1)))
		
	else :
		fp.seek(0)
	global word
	word =fp.readline()	#read the randomly generated word from the position where fp points
	print(word)
	return 


#This function asks for number of already guessed words and places those words at random positions 
'''def takehints():
	global already_guessed
	already_guessed=int(takeInput1())	#user inputs number of already guessed words
	global list_word
	list_word=[]
	for i in range(length):
		list_word.append(word[i])	
	
	list1=[]
	try:
		list1=random.sample(range(0,length), already_guessed) #gives a list some(no of already guessed) random number 
	except ValueError:
		print("enter again as word length = ",length)	#if already guessed words > word length
		takehints()

	for i in range(length):
		if i not in list1:
			list_word[i]='_'	#fill the positions(i) that is not in list1 with _
	print("The word to be guessed is:")
	for i in list_word:
		print(i,end="")

	print("\n")
	return
'''
#after the word is retrieved from the file playgame functions asks the user to enter a letter and checks wheather it matches with word retrieved
'''def playgame():
	guess=7
	score=7
	
	
	letters_used=[]  #empty list in order to append and the letters that are wrong
	print ("You only have "+str(guess)+" chances")
	current_length=already_guessed #No of letters guessed goes in the current_length
	while(current_length!=(len(word)-1) and guess!=0):
		alphabet_enter=input("Enter a letter:   ")
		alphabet_enter=alphabet_enter.upper()  #if user enters a letter in lower case this function converts it into upper case then checks
		found=0
		if (word.count(alphabet_enter)==list_word.count(alphabet_enter)!=0):
			print("This word is already guessed. Guess again :)")
			print("Current status of word  ")
			for i in list_word:
				print(i,end="")
			print("\n")
				
		else:		
			for i in range(0,length):
				if(word[i]==alphabet_enter and (alphabet_enter!=list_word[i])):  
					list_word[i]=alphabet_enter   #if letter entered by the user is present in word then in list_word letter is added on its position
					current_length+=1
					found=1
	
			if(found==1):
				print("Right:       ")
				for i in list_word:
					print(i,end="")
				print("\n")
			else:           #The letter entered by the user is not present in the word    
				print("Letters that you have already used are:      ")
				letters_used.append(alphabet_enter)   # letter that is not present in the word gets added in letters_used list
				print(letters_used)
				guess-=1
				score-=1
				print("Your Score is :    ")
				print(score)
				print(Hangmanpics[6-guess])   #With every wrong guess hangmanpic is displayed from the list
				print("wrong guess. You only have "+str(guess)+" guess left")
				for i in list_word:
					print(i,end="")
				print("\n")
			
			
	
	if((current_length == len(word)-1)):
		print("YES! YOU WON!!!!!!!!!")
		used_guess=7-guess
		print("Guesses used: "+str(used_guess)+ " out of 7")
	else:
		print("Sorry you could not guess the word")
		print("The correct answer is :    ")
		print(word)
'''
  

		
findword()
#takehints()
#playgame()
#print(list_word)
