from random import randint                                                            #Import the random function, used to determine question asked and the answer order
import time                                                                           #Allows time.sleep to be used in the 3-second countdown
                                                                                   #Converts keywords.txt into a list format for easy use later
question = 0                                                                        #Sets the question number as a global variable. As the quiz loops, this number grows.
choiceorder = randint(1,3)                                                         #Sets the order in which answers will appear as a global variable.
x = 0                                                                               #Sets the question displayed as a global variable.
wrong = 0                                                                           #Sets the amount of incorrect answers as a global variable.
right = 0                                                                           #Sets the amount of correct answers as a global variable
start = time.time()                                                             #Sets the time as a global variable. This doesn't start the timer until it's called in def Mainmenu() below.


def Mainmenu():
    #This section is a three-second countdown.                                                                     #Sets every value in the list points to zero. This is used especially when restarting the quiz. 
    global question                                                                                                                                                 #Gives permission for the global variable question to be used
    question = 0                                                                                                                                                    #Restarts the question counter, again used when the quiz is restarted
    print("Welcome to the Flash Card Quiz!")
    time.sleep(2)                                                                                                                                                   #Stops all actions for 2 seconds.
    print("3!")                                                                                                                                                         #Prints "3!", etc.
    time.sleep(1)                                                                                                                                                   #Stops all actions for 1 second.
    print("2!")
    time.sleep(1)
    print("1!")
    time.sleep(1)
    print("Go!")
    time.sleep(0.3)
    global start                                                                                                                                                       #Gives permission for the global variable start to be used 
    start = time.time()                                                                                                                                             #Starts the timer for the quiz.
    Quiz()                                                                                                                                                              #Begins the loop that provides questions.

def Quiz():                                                                                                                                                           #Defines the below code as part of the module Quiz()
    global question                                                                                                                                                #Permits usage of the global variable question.
    question = question + 1;                                                                                                                                  #Increases question number by 1, to help track progress in the quiz.
    print(("Question"), str(question) + ("!"))                                                                                                              #Prints "Question (x)!" where x is the amount of questions cleared plus 1.
    global x                                                                                                                                                            #Permits usage of the global variable x.
    x = randint(2,absolution)                                                                                                                                                #Sets the variable for the correct answer.           \
    secchoice = randint(2, absolution)                                                                                                                                  #Decides what incorrect answer will be printed    |----Chosen at random from the list of keywords.
    thirdchoice = randint(2, absolution)
    while x==absolution or x==absolution+1:
        x=randint(2,absolution)
    if x%2==0:
        print(defs[x])                                                                                                                                            #Print the entry after it in the list. Even-numbered list entries are the answers, and the entries following
        print("Choose your answer from the following:")                                                                                             #Prints the command to the user.
        global choiceorder                                                                                                                                      #Permits usage of the global variable choiceorder.
        choiceorder = randint(1, 3)                                                                                                                         #Sets the location of the correct answer in the multiple-choice block.
        while secchoice == thirdchoice or secchoice == thirdchoice - 1 or secchoice == x - 1 or secchoice == x:      #This line runs a series of checks on the first wrong answer to see if it is equal to the right, or other wrong, answer.
            secchoice = randint(2, absolution)                                                                                                                    #Redefines the variable if it fits this criteria. As this is a while loop, if the redefine again fits the criteria it redefines the variable again.
        while secchoice == thirdchoice or secchoice == thirdchoice - 1 or thirdchoice == x - 1 or thirdchoice == x:   #This line runs a series of checks on the second wrong answer to see if it is equal to the right, or other wrong, answer.
            thirdchoice = randint(2, absolution)                                                                                                                    #Redefines the variable if it fits this criteria. As this is a while loop, if the redefine again fits the criteria it redefines the variable again.
        if secchoice%2!=0 and thirdchoice%2!=0:                                                                                             #Checks that both of the other possible choices are even.
            if choiceorder == 1:                                                                                                                            #If the choice order states that the correct answer comes first...
                print(("1."), (defs[x-1]), ("\n2."), (defs[secchoice]), ("\n3."), (defs[thirdchoice]))                                            #...display it like that, then...
                Check()                                                                                                                                                 #run the answer input and checking function detailed under def Check():.
            elif choiceorder == 2:                                                                                                                               #Or if the choice order varies, do the same things.
                print(("1."), (defs[secchoice]), ("\n2."), (defs[x-1]), ("\n3."), (defs[thirdchoice]))                                            #
                Check()                                                                                                                                             #
            elif choiceorder == 3:                                                                                                                              #
                print(("1."), (defs[secchoice]), ("\n2."), (defs[thirdchoice]), ("\n3."), (defs[x-1]))                                            #
                Check()                                                                                                                                             #
        elif secchoice%2==0 and thirdchoice%2!=0:                                                                                               #If the first alternate choice isn't even...
            if choiceorder == 1:                                                                                                                                #
                print(("1."), (defs[x-1]), ("\n2."), (defs[secchoice-1]), ("\n3."), (defs[thirdchoice]))                                         #...rectify that by adding 1 to it and doing the same things as above.
                Check()                                                                                                                                             #
            elif choiceorder == 2:                                                                                                                              #
                print(("1."), (defs[secchoice-1]), ("\n2."), (defs[x-1]), ("\n3."), (defs[thirdchoice]))                                          #
                Check()                                                                                                                                             #
            elif choiceorder == 3:                                                                                                                              #
                print(("1."), (defs[secchoice-1]), ("\n2."), (defs[thirdchoice]), ("\n3."), (defs[x-1]))                                        #
                Check()                                                                                                                                             #
        elif secchoice%2!=0 and thirdchoice%2==0:                                                                                                #If the second alternate choice isn't even...
            if choiceorder == 1:                                                                                                                                #
                print(("1."), (defs[x-1]), ("\n2."), (defs[secchoice]), ("\n3."), (defs[thirdchoice-1]))                                          #...again, rectify it by adding 1.
                Check()                                                                                                                                             #
            elif choiceorder == 2:                                                                                                                              #
                print(("1."), (defs[secchoice]), ("\n2."), (defs[x-1]), ("\n3."), (defs[thirdchoice-1]))                                          #
                Check()                                                                                                                                             #
            elif choiceorder == 3:                                                                                                                              #
                print(("1."), (defs[secchoice]), ("\n2."), (defs[thirdchoice-1]), ("\n3."), (defs[x-1]))                                          #
                Check()                                                                                                                                               #
        elif secchoice%2==0 and thirdchoice%2==0:                                                                                                    #If both alternate choices aren't even...
            if choiceorder == 1:                                                                                                                                    #
                print(("1."), (defs[x-1]), ("\n2."), (defs[secchoice-1]), ("\n3."), (defs[thirdchoice-1]))                                        #...again, rectify them both by adding 1.
                Check()                                                                                                                                                 #
            elif choiceorder == 2:                                                                                                                                  #
                print(("1."), (defs[secchoice-1]), ("\n2."), (defs[x-1]), ("\n3."), (defs[thirdchoice-1]))                                        #
                Check()                                                                                                                                                 #
            elif choiceorder == 3:                                                                                                                                  #
                print(("1."), (defs[secchoice-1]), ("\n2."), (defs[thirdchoice-1]), ("\n3."), (defs[x-1]))                                        #
                Check()                                                                                                                                                 #
    elif x%2!=0:                                                                                                                                                       #And if the right answer variable is odd...
        print(defs[x+1])                                                                                                                                                  #...go through exactly the same process, but don't add 1 to x.
        print("Choose your answer from the following:")                                                                                                 #Everything below this will not be annotated unless there is a real difference to what's above.
        global choiceorder                                                                                                                                          #
        choiceorder = randint(1, 3)                                                                                                                               #
        secchoice = randint(2, absolution)                                                                                                                               #
        thirdchoice = randint(2, absolution)                                                                                                                              #
        while secchoice == thirdchoice or secchoice == x or secchoice == x + 1 or secchoice == thirdchoice - 1:                                                 #Runs the check that the first alternate answer isn't equal to the other alternate answer or the correct answer.
            secchoice = randint(2, absolution)                                                                                                                           #Redefines the variable if it fits the criteria.
        while thirdchoice == secchoice or thirdchoice == x or thirdchoice == x + 1 or thirdchoice == secchoice - 1:       #Does the same for the other alternate choice.
            thirdchoice = randint(2, absolution)                                                                                             #
        if secchoice%2!=0 and thirdchoice%2!=0:                                                                         #
            if choiceorder == 1:                                                                                                        #
                print(("1."), (defs[x]), ("\n2."), (defs[secchoice]), ("\n3."), (defs[thirdchoice]))                #
                Check()                                                                                                                     #
            elif choiceorder == 2:                                                                                                      #
                print(("1."), (defs[secchoice]), ("\n2."), (defs[x]), ("\n3."), (defs[thirdchoice]))                #
                Check()                                                                                                                     #
            elif choiceorder == 3:                                                                                                      #
                print(("1."), (defs[secchoice]), ("\n2."), (defs[thirdchoice]), ("\n3."), (defs[x]))                #
                Check()                                                                                                                     #
        elif secchoice%2!=0 and thirdchoice%2==0:                                                                         #
            if choiceorder == 1:                                                                                                         #
                print(("1."), (defs[x]), ("\n2."), (defs[secchoice-1]), ("\n3."), (defs[thirdchoice-1]))            #
                Check()                                                                                                                     #
            elif choiceorder == 2:                                                                                                      #
                print(("1."), (defs[secchoice]), ("\n2."), (defs[x]), ("\n3."), (defs[thirdchoice-1]))            #
                Check()                                                                                                                     #
            elif choiceorder == 3:                                                                                                      #
                print(("1."), (defs[secchoice]), ("\n2."), (defs[thirdchoice-1]), ("\n3."), (defs[x]))            #
                Check()                                                                                                                     #
        elif secchoice%2==0 and thirdchoice%2!=0:                                                                         #
            if choiceorder == 1:                                                                                                        #
                print(("1."), (defs[x]), ("\n2."), (defs[secchoice-1]), ("\n3."), (defs[thirdchoice]))            #
                Check()                                                                                                                     #
            elif choiceorder == 2:                                                                                                      #
                print(("1."), (defs[secchoice-1]), ("\n2."), (defs[x]), ("\n3."), (defs[thirdchoice]))            #
                Check()                                                                                                                     #
            elif choiceorder == 3:                                                                                                      #
                print(("1."), (defs[secchoice-1]), ("\n2."), (defs[thirdchoice]), ("\n3."), (defs[x]))            #
                Check()                                                                                                                     #
        elif secchoice%2==0 and thirdchoice%2==0:                                                                          #
            if choiceorder == 1:                                                                                                        #
                print(("1."), (defs[x]), ("\n2."), (defs[secchoice-1]), ("\n3."), (defs[thirdchoice-1]))        #
                Check()                                                                                                                     #
            elif choiceorder == 2:                                                                                                      #
                print(("1."), (defs[secchoice-1]), ("\n2."), (defs[x]), ("\n3."), (defs[thirdchoice-1]))        #
                Check()                                                                                                                     #
            elif choiceorder == 3:                                                                                                      #
                print(("1."), (defs[secchoice-1]), ("\n2."), (defs[thirdchoice-1]), ("\n3."), (defs[x]))        #
                Check()

def Check():                                                                                                                                #
    ans = choiceorder                                                                                                                   #Allows the user to input an answer
    if ans == choiceorder:                                                                                                           #If the answer the user enters corresponds to the location of the correct answer in the order of the list...
            print("Correct!")                                                                                                           #...show them that they got it right.
            global points
            points[x] = int(points[x]) + 1                                                                                          #This changes the value in the list according to the number of the question.
            global right                                                                                                                #Permits the changing of the variable right.
            right = right + 1
            Breaktime()#Adds to the variable.                                                                                                    #Goes back to the starting countdown, where all variables needed to be reset will be reset.                                                                                                       #...the shutting down of the code.                                                                                                      #...this restarts the cycle of giving a question, after checking that the user hasn't hit a 15-question milestone.
    else:                                                                                                                            #And if the answer they've picked is wrong...
            print("Incorrect.")                                                                                             #This prints to the interpreter that theuser has got the question wrong, as they haven't fit the above criteria.
            global wrong                                                                                                    #Permits the changing of the variable wrong.
            wrong = wrong + 1                                                                                           #Appends another point to the total of wrong answers.
            Breaktime()                                                                                                     #...and asks another question, after checking that the user hasn't hit a 15-question milestone.

def Breaktime():
    if question%15==0:                                                                                                      #If the number of the question the user just cleared is divisible by 15...
        print("Guess it's time you took a break...How long do you want (in minutes)?")              #...a question is printed to the interpreter asking how long a break the user would like.
        meeh = int(input())                                                                                                     #Allows the user to input a number.
        time.sleep(meeh*60)                                                                                                 #Pauses the code for as many minutes as the user asked for.
        Quiz()
    elif question%100==0:
        print("Looks like it's time you stopped. This thing's being going for a while...Bye!")
        import sys
        sys.exit()
    else:                                                                                                                           #And if they have't hit a 15-question milestone...
        Quiz()                                                                                                                      #...another question is fired as normal.

title = input("Which quiz do you want to take?")
meh = "Z:/Documents/Quizzes/" + str(title)    #CHANGE THIS FOR THE DIRECTORY IN WHICH YOU KEEP YOUR QUIZZES MADE IN QUIZ_CONFIG
file = open(meh + ".txt", "r")
defs = list(file)
absolution = len(defs) - 1
variabool = 0
points = []
while variabool < absolution + 2:
    points.append(0)
    variabool = variabool + 1
print(defs)
Mainmenu()                                         #This starts the code as a whole, as the chunks above only define what needs to happen.
