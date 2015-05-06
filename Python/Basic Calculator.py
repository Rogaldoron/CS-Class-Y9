#Seen below is a function
#This specific function is executed on line 25

def Start():
    a1=input("\nWhat would you like to do? Addition (A), subtraction (S), division (D) or multiplication (M)?\nPlease remember that you cannot divide by 0!\n").lower()
    if a1=="a":
        Addition()
    elif a1=="s":
        Subtraction()
    elif a1=="d":
        Division()
    elif a1=="m":
        Multiplication()
    elif a1=="exit":
        Exit()
    else:
        print ("What the heck are you talking about\n")
        Start()

#Seen below is another function
#This specific function is executed on line 6

def Addition():
    numberOfGames=input("How many games did they play? ")
    a3=input("\nSecond Number: ")
    print("\n",a2,"+",a3,"=",int(a2)+int(a3))
    Start()

#Seen below is another function
#This specific function is executed on line 8

def Subtraction():
    a4=input("\nFirst Number: ")
    a5=input("\nSecond Number: ")
    print("\n",a4,"-",a5,"=",int(a4)-int(a5))
    Start()

def Division():
    a6=input("\nFirst Number: ")
    a7=input("\nSecond Number: ")
    print("\n",a6,"/",a7,"=",int(a6)/int(a7))
    Start()

def Multiplication():
    a8=input("\nFirst Number: ")
    a9=input("\nSecond Number: ")
    print("\n",a8,"*",a9,"=",int(a8)*int(a9))
    Start()

def Exit():
    print("")
    
#When defining a function you must add brackets next to the name of said function.
#These are the functions parameters should you want to use variables from other parts of your program in your function.

Start()

#You execute (or call) a function by typing its name with the parameters, in brackets, next to it
