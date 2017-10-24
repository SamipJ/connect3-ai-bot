#SAMIP JASANI 2015A7PS0127P
from finalgui import *
exit=False
while not exit:
    inp=raw_input("Enter one of the options:\n\
    1. Display Empty board\n\
    2. Play Game using Minimax Algorithm\n\
    3. Play using Alpha-Beta Pruning\n\
    4. Show all results R1-R12\n\
    5. Play using my depth-using minimax\n\
    0 . EXIT\n\
    >> ")
    opt=int(inp)
    if opt==1:
        play = ConnectThree("blank")
        turtle.done()
    elif opt==2:
        print "2"
        play = ConnectThree("minimax")
        turtle.done()
    elif opt==3:
        print "3"
        play = ConnectThree("alphabeta")
        turtle.done()
    elif opt==4:
        results()
        turtle.done()
    elif opt==5:
        play = ConnectThree("myminimax")
        turtle.done()
    elif opt==0:
        exit=True