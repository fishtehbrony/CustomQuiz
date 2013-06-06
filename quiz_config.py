print("Welcome to quiz_config")
print("You can exit the config AS LONG AS THE REQUEST IS 'Please enter the question you'd like to ask:' with Alt+F4.")
title = input("Please enter the subject:")
meh = "Z:/Documents/Quizzes/" + str(title)
print(meh)          #Change 'meh' according to where you want to put your quizzes
f = open(meh + ".txt", "a")
f.write(str(title) + ("\n"))
f.close
while True:
    f = open(meh + ".txt", "a")
    question = str(input("Please enter the question you'd like to ask:"))
    answer = str(input("Please enter the correct answer to that question:"))
    f.write(str(answer) + ("\n"))
    f.write(str(question) + ("\n"))
    f.close()
