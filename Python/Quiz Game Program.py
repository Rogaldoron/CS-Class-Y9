def CheckAnswer(answer1,question,correct_answer1,answer2,correct_answer2):
    if question==1:
        if answer1==correct_answer1:
            message1="\n\nD, Millenium Edition, is the correct answer! Well done!"
            return message1
        else:
            message1="\n\nYour answer is incorrect! Jeeves is disappointed!\nThe Correct answer was D, Millenium Edition!\nJeeves commands you to do better next time!"
            return message1
    if question==2:
        if answer2==correct_answer2:
            message1="\n\nB, Random Access Memory, is the correct answer! Well done!"
            return message1
        else:
            message1="\n\nYour answer is incorrect! Jeeves is disappointed!\nThe Correct answer was B, Random Access Memory!\nJeeves commands you to do better next time!"
            return message1

def PractiseQuestion():
    print("\nWhat does the ME in Windows ME stand for?")
    time.sleep(3)
    print("Option A: Microsoft Edition")
    time.sleep(2)
    print("Option B: Mainframe Edition")
    time.sleep(2)
    print("Option C: Mavericks Edition")
    time.sleep(2)
    print("Option D: Millennium Edition")
    time.sleep(2)
    question=1
    correct_answer1="D"
    answer1=input("Your answer is: ").upper()
    if answer1=="A" or answer1=="D" or answer1=="C" or answer1=="B":
        print(CheckAnswer(answer1,question,correct_answer1))
        a=input("\nPress enter to continue!")
        Question1()
    else:
        print('Jeeves does not understand your answer. Please state your answer as an "A", "B", "C" or "D"!')
        time.sleep(5)
        print("Let's try the question again")
        PractiseQuestion()

def Question2():
    print("\n"*100)
    print("Now you've got the hang of it, let's start our quiz!")
    time.sleep(5)
    print("\n\nQuestion 1: What does RAM stand for?")
    time.sleep(3)
    print("Option A: Random Allocated Memory")
    time.sleep(2)
    print("Option B: Random Access Memory")
    time.sleep(2)
    print("Option C: Raw Accessed Memory")
    time.sleep(2)
    print("Option D: Recursive Analog Markup")
    time.sleep(2)
    question=2
    correct_answer2="B"
    answer2=input("Your answer is: ").upper()
    if answer2=="A" or answer1=="D" or answer1=="C" or answer1=="B":
        print(CheckAnswer(answer1,question,correct_answer1))
        b=input("\nPress enter to continue!")
        Question3()
    else:
        print('Jeeves does not understand your answer. Please state your answer as an "A", "B", "C" or "D"!')
        time.sleep(5)
        print("Let's try the question again")
        Question2()

def Question3():
    print("\n"*100)
    print("Question 2: What does CPU stand for?")
    time.sleep(3)
    print("Option A: Central Processing Unit")
    time.sleep(2)
    print("Option B: Central Processing Utility")
    time.sleep(2)
    print("Option C: Central Processor Unicode")
    time.sleep(2)
    print("Option D: Central Processing Unix")
    time.sleep(2)
    question=3
    correct_answer3="A"
    answer3=input("Your answer is: ").upper()
    if answer3=="A" or answer1=="D" or answer1=="C" or answer1=="B":
        print(CheckAnswer(answer1,question,correct_answer1))
        c=input("\nPress enter to continue!")
        Question4()
    else:
        print('Jeeves does not understand your answer. Please state your answer as an "A", "B", "C" or "D"!')
        time.sleep(5)
        print("Let's try the question again")
        Question3()

def Question4():
    
    
    

import time

print("\n"*100)
goto=input("DEV TOOL! WOULD YOU LIKE TO GO ANYWHERE!")
if goto=="PractiseQuestion":
    PractiseQuestion()
else:
    print("")
print("Hello and Welcome to the National Computing Quiz!")
time.sleep(3)
print("\nAnd now welcome your favourite quiz show host...")
time.sleep(3)
print("\nJeeves!")
time.sleep(1)
print("""\n          /:""|
         |: 66|_     
         C     _)    
          \ ._|      
           ) /       
          /`\\        
         || |Y|      
         || |#|     
         || |#|      
         || |#|     
         :| |=:   
         ||_|,|    
         \)))||   
      |~~~`-`~~~| 
      |         |  
      |_________|     
      |_________|   
          | ||      
          |_||__   
          (____))
    """)



name=input("Please tell us your name contestant!\n")
print("\nWelcome to the game show",name,"!")
time.sleep(4)
print("\nWe will be asking you,",name,", five multiple choice questions related to computing!")
time.sleep(6)
print('\nYou simply need to answer "A" if you think the answer is option A, "B" if you think the answer is option B, and so on, so forth')
time.sleep(6)
print("\nLet me give you an example:")
time.sleep(5)
print("\nThe questions will be displayed in the following format:")
time.sleep(5)
PractiseQuestion()





