def Area():
    print("\n"*50)
    print("""     ______
    |      |
    |      |  x
    |______|

       y
    """)
    width=int(input("Please state the width, which is displayed as y in the diagram above, of your rectangle: "))
    height=int(input("Please state the height, which is displayed as x in the diagram above, of your rectangle: "))
    print("The area of your rectangle is x multiplied by y which is: ",width*height)
    enter=input("\n\n\nPress enter to continue")
    Area()
Area()
