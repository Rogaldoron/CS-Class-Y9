def OutputPoints(TeamName,Wins,Draws,Losses, NumberOfGames):
    TotalPoints = (Wins*3)+Draws
    print(TeamName,"achieved a total score from all games of",TotalPoints)
    print("\n",TeamName,"has an average point score of",(Tot-alPoints/NumberOfGames))

TeamName=input("What is the Team called? ")
NumberOfGames = int(input("How many games did they play? "))
Wins=int(input("How many games did they win? "))
Draws=int(input("How many games did they draw in? "))
Losses=int(input("How many games did they lose? "))
OutputPoints(TeamName,Wins,Draws,Losses, NumberOfGames)
