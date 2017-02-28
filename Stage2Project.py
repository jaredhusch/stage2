#stage 2 project: Quiz on space
blanks = ["__1__", "__2__", "__3__", "__4__"]

easy_questions = "What planet has the nickname, the Red Planet __1__? What is the biggest planet in our solar system __2__? What is the name of the galaxy Earth resides in __3__? What is the smallest planet in our solar system __4__?"
medium_questions = "What is the name of the next closest galaxy to Earth __1__? The explosion of a star is called __2__? How many planets are in the Solar System __3__? What has a gravitational pull so strong that even light cannot escape it __4__?"
hard_questions = "What type of galaxy is the most common in the Universe __1__? What is the closest star to the Sun __2__? How many billions of years old is the Universe __3__? What is the name of the brightest star in the night sky __4__?"

easy_answers = ["Mars", "Jupiter", "Milky Way", "Mercury"]
medium = ["Andromedia", "Supernova", "8", "Black Hole"]
hard_answers = ["Elliptical", "Alpha Centauri", "13.7", "Sirius"]

print ("Welcome to my Space Fill in the Blanks Quiz!!!")
user_input = input("Please choose a difficulty level: easy, medium, or hard.")

#Takes user input to determine the level and prints out that level
def level(user_input):
    if user_input.lower() == "easy":
        print("You've chosen easy.")
        return easy_questions
    elif user_input.lower() == "medium":
        print("You've chosen medium.")
        return medium_questions
    elif user_input.lower() == "hard":
        print("You've chosen hard.")
        return hard_questions
print(level(user_input))


