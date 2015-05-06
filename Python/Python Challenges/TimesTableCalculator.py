def TimesTableCalculator():
    print("\n"*100)
    print("Hello! I'm Jeeves, the Times Table Bot!")
    print("""          /:""|
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
    num1=int(input("Please enter the times table you wish to know: "))
    num2=int(input("Please enter the number up to which you want to know your times table: "))
    num3=1
    while num3<=num2:
        print(num3," X ",num1,"=",num3*num1)
        num3=num3+1
    print("\nDONE!")
    loop=input("Press enter to continue")
    TimesTableCalculator()

TimesTableCalculator()
    
