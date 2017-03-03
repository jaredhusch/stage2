#stage 2 project: Quiz on space

#These are the blanks that will have to be replaced

blanks = ["__1__", "__2__", "__3__", "__4__"]

easy_questions = "What planet has the nickname, the Red Planet __1__? What is the biggest planet in our solar system __2__? What is the name of the galaxy Earth resides in __3__? What is the smallest planet in our solar system __4__?"
easy_answers = ["Mars", "Jupiter", "Milky Way", "Mercury"]

medium_questions = "What is the name of the next closest galaxy to Earth __1__? The explosion of a star is called __2__? How many planets are in the Solar System __3__? What has a gravitational pull so strong that even light cannot escape it __4__?"
medium_answers = ["Andromeda", "Supernova", "8", "Black Hole"]

hard_questions = "What type of galaxy is the most common in the Universe __1__? What is the closest star to the Sun __2__? How many billions of years old is the Universe __3__? What is the name of the brightest star in the night sky __4__?"
hard_answers = ["Elliptical", "Alpha Centauri", "13.7", "Sirius"]

#Ask for user's name
user_name = raw_input('What is your name?')

#Greet the user
print ("Hello and welcome to my Space Fill in the Blanks Quiz!!!" + user_name + "!")

def get_level():
  level = raw_input('Please choose a level between easy, medium and hard')
  if level == "easy" or level == "medium" or level == "hard":
    return level

#getting the quiz  
def get_questions(game_level):
  if game_level == "easy":
      print "You chose level Easy."
      return easy_questions
      
  elif game_level == "medium":
      print "You chose level Medium."
      return medium_questions
      
  elif game_level == "hard":
      print "You chose level Hard."
      return hard_questions
      
#getting quiz answers      
def get_answers(game_level):
  
  if game_level == "easy":
      return easy_answers
      
  elif game_level == "medium":
      return medium_answers
      
  elif game_level == "hard":
      return hard_answers

def blank_in_blanks(word, blanks):
    for blank in blanks:
        if blank in word:
            return blank
    return None

def play_game():
	game_level= get_level()
	questions= get_questions(game_level)
	answers= get_answers(game_level)
	replaced = []
	count_answers=0
	print questions
	questions = questions.split()
	for word in questions:
		replacement = blank_in_blanks(word, blanks)
		if replacement != None:
			user_input = raw_input("What is the answer for blank: " + replacement+ " ")
			while user_input != answers[count_answers]:
				print "Your answer was wrong. Please enter a new answer: "
				user_input== raw_input()
			word= word.replace(replacement, user_input)
			replaced.append(word)
			count_answers= count_answers+1
			print " ".join(replaced)
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	print "Congratulations, you have found all the answers!"

print play_game()