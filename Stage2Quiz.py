#Stage 2 project. 

#Easy questions. Easy answers. Easy sentences that contain the easy answers. 
easy_questions = ["What planet has the nickname, the Red Planet ____?\n", 
"What is the biggest planet in our solar system ____?\n",
"What is the name of the galaxy Earth resides in ____?\n",
"What is the smallest planet in our solar system ____?\n",]
easy_answers = ["mars", "jupiter", "milky way", "mercury"]
easy_sentence = ["Mars has the nicknam the Red Planet.", 
"Jupiter is the largest planet in the solar system.", 
"Earth resides in the Milky Way galaxy.", 
"Mercury is the smallest planet in th solar system."]

#Medium questions. Medium anwsers. Medium setences that contain the medium answers.
medium_questions = ["What is the name of the next closest galaxy to Earth ____?\n",
"The explosion of a star is called __2__?\n",
"How many planets are in the Solar System __3__?\n",
"What has a gravitational pull so strong that even light cannot escape it __4__?\n",]
medium_answers = ["andromeda", "supernova", "8", "black hole"]
medium_sentence = ["Andromeda is the next closest galaxy to Earth.", 
"The explosion of a start is called a supernova.", 
"There are currenlty eight planets in the solar system.", 
"A black hole has a gravitational plull so strong that light cannot escape it."]

#Hard questions. Hard answes. Hard sentences that contain the hard answers.
hard_questions = ["What type of galaxy is the most common in the Universe ____?",
"What is the closest star to the Sun ____?",
"How many billions of years old is the Universe ____?",
"What is the name of the brightest star in the night sky ____?"]
hard_answers = ["elliptical", "alpha Centauri", "13.7", "sirius"]
hard_sentence = ["Elliptical galaxies are the most common in the Universe.", 
"Alpha Centauri is the closest star to the Sun.", 
"The universe is 13.7 years old", 
"Sirius is the brightest star in the night sky."]

#Ask user for name and prints welcome message
user_name = raw_input("What is your name?")
print ("Hello " + user_name + " and welcome to my Space fll-in-the-blanks-quiz!")

#Asks user to select a level for the game
def getlevel():
	level = raw_input("What level would you like to play? Please type 'easy', 'medium', or 'hard':\n")
	level = level.lower()
	if level == "easy" or level == "medium" or level == "hard":
		print "You chose level " + level
		return level
	else:
		print level + " is not a valid entry"
		return getlevel()


userlevel = getlevel()
print userlevel

#Get questions and answers and sentences for selected level 
def getquestionanswer(userlevel):
	if userlevel == "easy":
		return [easy_questions, easy_answers, easy_sentence]
	elif userlevel == "medium":
		return [medium_questions, medium_answers, medium_sentence]
	elif userlevel == "hard":
		return [hard_questions, hard_answers, hard_sentence]

#Variables use to play th egame
userquestions = getquestionanswer(userlevel)
questions = userquestions[0]
answers =  userquestions[1]
sentence = userquestions[2]
question_counter = 0

#Retrieves the question and checks user input with answer key list
def answerquestion(questions, answers, sentence, question_counter):
	user_answer = raw_input(questions[question_counter])
	if user_answer.lower() == answers[question_counter].lower():
		print sentence[question_counter]
		question_counter = question_counter+1
		if question_counter < len(questions):
			answerquestion(questions, answers, sentence, question_counter)
		else: 
			print "Congrats!"
			for correct_answers in sentence:
				print correct_answers
	else:
		print "Incorrect"
		answerquestion(questions, answers, sentence, question_counter)

#Plays the game 
answerquestion(questions, answers, sentence, question_counter)

