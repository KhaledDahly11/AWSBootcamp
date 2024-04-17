import random

#----------------Array printing----------------
def printarray():
    InstructionArray=['0','1','2','3','4','5','6','7','8']
    print ("\nGrid0")
    print (GridArray[0][0:3],"\t",InstructionArray[0:3])
    print (GridArray[0][3:6]," Index->",InstructionArray[3:6])
    print (GridArray[0][6:],"\t",InstructionArray[6:])
    print ("\nGrid1")
    print (GridArray[1][0:3],"\t",InstructionArray[0:3])
    print (GridArray[1][3:6]," Index->",InstructionArray[3:6])
    print (GridArray[1][6:],"\t",InstructionArray[6:])
    print ("\nGrid2")
    print (GridArray[2][0:3],"\t",InstructionArray[0:3])
    print (GridArray[2][3:6]," Index->",InstructionArray[3:6])
    print (GridArray[2][6:],"\t",InstructionArray[6:])
    print ()

#-----------------Main Function----------------
print ()
print("Welcome to the 3D tic tac toe game!")
while(1):
    print ("1.Start game\n2.Exit")
    option=input("Please enter an option: ")
    if option=='2':
          print ("Goodbye!")
          exit ()
    elif option=='1':
        GridArray=[]
        GridArray.append([' ',' ',' ',' ',' ',' ',' ',' ',' '])
        GridArray.append([' ',' ',' ',' ',' ',' ',' ',' ',' '])
        GridArray.append([' ',' ',' ',' ',' ',' ',' ',' ',' '])
        #instructions
        print ("The game rules:\n*You can enter a grid number between 0-2\n*You can enter a square number between 0-8\nHere is the grids numbered printed")
        printinstructions()
        #Players initilaization
        P1=input("Please enter the first player name who will use 'X': ")
        P2=input("Please enter the second player name who will use 'O': ")
        P1symbol='X'
        P2symbol='O'
        #Game starting
        currentplayer=random.randint(1,2)
        print (f"The Player who starts is {P1}") if currentplayer==1 else print (f"The Player who starts is {P2}")
        printarray()
        while(1):
            print (f"{P1}'s turn!") if currentplayer==1 else print (f"{P2}'s turn!")
            Gridnum=int(input("Please enter a grid number: "))
            Squarenum=int(input("Please enter a square number: "))
            if (Gridnum<0 or Gridnum>2 or Squarenum<0 or Squarenum>8):
                print ("You entered a grid number or square number that is out of the game limits. here is the grid and squares numbering.")
                printarray()
                print ("Please enter a grid and square numbers again!\n")
                continue
            if GridArray[Gridnum][Squarenum] != ' ':
                print (f"Square:{Squarenum} in grid:{Gridnum} is already used.\nPlease choose another one.")
                continue
            if(currentplayer==1):
                GridArray[Gridnum][Squarenum] = 'X'
                currentplayer=2
            else:
                GridArray[Gridnum][Squarenum] = 'O'
                currentplayer=1
            #winningoptions
            Hhelper=int(Squarenum/3)*3
            Vhelper=int(Squarenum%3)
            #vertical
            op1 = (GridArray[0][Squarenum] == GridArray[1][Squarenum] == GridArray[2][Squarenum] != ' ')
            #horizinal
            op2 = (GridArray[Gridnum][Hhelper] == GridArray[Gridnum][Hhelper+1] == GridArray[Gridnum][Hhelper+2] != ' ')
            op3 = (GridArray[0][Hhelper] == GridArray[1][Hhelper+1] == GridArray[2][Hhelper+2] != ' ')
            op6 = (GridArray[2][Hhelper] == GridArray[1][Hhelper+1] == GridArray[0][Hhelper+2] != ' ')
            #verticaldifferentgrid
            op4 = (GridArray[Gridnum][Vhelper] == GridArray[Gridnum][Vhelper+3] == GridArray[Gridnum][Vhelper+6] != ' ')
            op5 = (GridArray[0][Vhelper] == GridArray[1][Vhelper+3] == GridArray[2][Vhelper+6] != ' ')
            op7 = (GridArray[2][Vhelper] == GridArray[1][Vhelper+3] == GridArray[0][Vhelper+6] != ' ')
            #diagonal
            #op8 = (GridArray[0][Vhelper] == GridArray[1][Vhelper+3] == GridArray[2][Vhelper+6] != ' ')
            printarray()
            if(op1 or op2 or op3 or op4 or op5 or op6 or op7):
                    print ("The game has ended!")
                    print (f"{P1} has won!") if currentplayer==2 else print (f"{P2} has won!")
                    print ("\nWhat would you like to do next?")
                    break
    else:
         print ("This is not a valid option.\nPlease choose the number 1 or 2\n")