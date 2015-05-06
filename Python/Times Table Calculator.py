import time

def Printy():
    print("\n"*100)

def TimesTables():
    print("Hello! I'm Jeeves, the Times Table Bot!")
    time.sleep(2)
    print("LOOK AT ME!")
    time.sleep(1)
    print("""      /:""|
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
    time.sleep(2)
    num1=int(input("Give me your first number to multiply, please:"))
    num2=int(input("Give me your second number to multiply, please:"))

    for x in range(1,num2):
        print(x*num1)

Printy()
TimesTables()
