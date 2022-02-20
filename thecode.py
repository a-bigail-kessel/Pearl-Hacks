"""docstring """

import numpy as np
import pandas as pd

import webbrowser
# webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSfXbjS8lE9yYYeECOAGNeHHjUnyP_Mt3iJGxzN-F_bYjwWnuA/viewform')



%matplotlib inline
import 

pearl = Table.read_table("Navigating UNC Susan Director.csv")




def initial_greeting():
 """Initial Greeting."""
    print("Welcome! I'm Rameses, and I was designed help women and nonbinary people at UNC navigate STEM fields! We accept and offer advice about classes, clubs, and professors.")
    giveorreceive = input("Would you like to give advice or receive advice?")
    if "give" in giveorreceive:
        give()
    elif "receive" in giveorreceive:
        receive()
    else:
        print("Sorry, I don’t understand.")
    


def give():
	"""Give function."""
	print("Please fill out this google form")
    webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSfXbjS8lE9yYYeECOAGNeHHjUnyP_Mt3iJGxzN-F_bYjwWnuA/viewform')

def receive():
    """ receive """
    profclassclub= input("Would you like to receive advice on professors, classes, or clubs?")
    if "professors" or "professor" in profclassclub:
        professor()
   elif "club" or "clubs" in profclassclub:
       club()
     print("Here are some of our club recommendations!")
       # list of clubs and descriptions and links to websites
   elif "class" or "classes" in profclassclub:
       classes()

def professor():
    choose_or_top = input("Do you want to CHOOSE a specific professor or just hear about the TOP ones")
    while choose_or_top != "CHOOSE" or choose_or_top != "TOP":
        leave = input("Do you want to hear about profs? YES or NO")
        if leave == "NO":
            leave()
        else:
            choose_or_top = input("Say CHOOSE or TOP")
    if choose_or_top == "CHOOSE":
        prof_choose()
    elif choose_or_top == "TOP":
        prof_top()
 
def prof_choose():
    print("Here are all the professors you can ask about")
    professor_column = pearl.select('Professor')
    print(professor_column)
    choosenprof = input("What professor do you want to hear about?")
    Reviews = pearl.where("Professor", are.equal_to(choosenprof)).column("Why Professor")
	for review in reviews:
		print(review)
    leave()

def prof_top():
    print("Here are some of the most recommended professors:")
    professor_column = pearl.group('Professor').sort('count', descending = True)
    top_five_professors = professor_column.take(np.arange(0,5))
    print("Would you like to see more professors? Enter 'YES' or 'NO'")
    moreprofs: str = input()
    if moreprofs == "YES":
        number_profs = input('How many professors would you like to see? Input a number between 1 and', professor.column.num_rows, ".")
	    print(professor_column.show(number_profs))
    leave()

def classes():
    choose_or_top = input("Do you want to CHOOSE a specific class or just hear about the TOP ones")
    while choose_or_top != "CHOOSE" or choose_or_top != "TOP":
        leave = input("Do you want to hear about classes? YES or NO")
        if leave == "NO":
            leave()
        else:
            choose_or_top = input("Say CHOOSE or TOP")
    if choose_or_top == "CHOOSE":
        classes_choose()
    elif choose_or_top == "TOP":
        classes_top()


def classes_choose():
    print("Here are all the classes you can ask about")
    classes_column = pearl.select('Class')
    print(class_column)
    choosenpclass = input("What class do you want to hear about?")
    reviews = pearl.where("Class", are.equal_to(choosenclass)).column("Why Class")
	for review in reviews:
		print(review)
    leave()

def classes_top():
    print("Here are some of the most recommended classes:")
    class_column = pearl.select('Class').group('Class').sort('count', descending = True)
 	print(class_column)
    top_five = class_column.take(np.arange(0,5))
    print("Would you like to see more classes? Enter 'Yes' or 'No'")
    moreclasses: str = input()
    if moreclasses == "Yes":
        print('How many classes would you like to see? Input a number between 1 and', class.column.num_rows, ".")
        number_classes = str = input()
	    print(class_column.show(number_classes))
    leave()



def club():
    choose_or_top = input("Do you want to CHOOSE a specific club or just hear about the TOP ones")
    while choose_or_top != "CHOOSE" or choose_or_top != "TOP":
        leave = input("Do you want to hear about clubs? YES or NO")
        if leave == "NO":
            leave()
        else:
            choose_or_top = input("Say CHOOSE or TOP")
    if choose_or_top == "CHOOSE":
        classes_choose()
    elif choose_or_top == "TOP":
        classes_top()

def leave():
    leave = input("Do you want to go back to 'PROFESSORS', 'CLUBS', 'CLASSES' or 'EXIT'"):
    while leave != "PROFESSORS" or leave != "CLUBS" or leave != "CLASSES" or leave != "EXIT":
        leave = ("Ask one of the following; 'PROFESSORS', 'CLUBS', 'CLASSES' or 'EXIT'")
        if leave == "PROFESSORS":
            professor()
        elif leave == "CLUBS":
            club()
        elif leave == "CLASSES":
            classes()
        elif leave == "EXIT":
            initial_greeting()

initial_greeting()