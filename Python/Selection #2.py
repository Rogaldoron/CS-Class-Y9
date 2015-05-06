from random import randint
num=randint(1,5)
def Program(num):
    guess=int(input("Think of a number between 1 and 5: "))
    if guess==num:
        print("Well done")
    elif guess<num:
        print("Too low\n")
        Program(num)
    elif guess>num:
        print("Too high\n")
        Program(num)
Program(num)
        
