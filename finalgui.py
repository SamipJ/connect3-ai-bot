from minimax import *
from alphabeta import *
from myversion import *
import random
import turtle
def color(x,y,player,screen):
    t = turtle.Turtle()
    screen.tracer(1)
    t.speed(0)
    t.ht()
    if player == 1:
        t.pen(fillcolor="light green",pencolor="green",pensize=4)
        # t.color("light green")
    if player == 2:
        t.pen(fillcolor="light blue",pencolor="blue",pensize=4)
        # t.color("pink")
    t.penup()
    t.goto(x+12.5,y)    
    t.begin_fill()
    t.pendown()
    t.circle(12.5)
    t.penup()
    t.end_fill()


class ConnectThree:

    def __init__(self):
        # self.player = 1 #BOT First
        self.player = 2 #Human First
        # changes player every time a successful move has been made
        
        self.board=[[0]*4 for _ in range(4)]
        self.seen={}
        self.screenSetup()

    def screenSetup(self):

        self.screen = turtle.Screen()
        self.screen.setup(width=875,height=600)
        # self.screen.reset()
        self.screen.setworldcoordinates(-90,-10,110,110)
        self.screen.bgcolor("white")
        self.screen.tracer(0)
        # self.startX = 
        self.drawer = turtle.Turtle()
        self.drawer.ht()
        self.drawer.setx(0)
        # self.startY = 
        self.drawer.sety(0)
        # self.drawer.ht()
        self.drawer.penup()
        self.drawer.pencolor("black")
        self.drawer.pensize(2)

        i = 0
        while i <= 100:
            self.drawer.setpos(i,0)
            self.drawer.pendown()
            self.drawer.setpos(i, 100)
            self.drawer.penup()
            i += 25

        j = 0
        while j <= 100:
            self.drawer.setpos(0,j)
            self.drawer.pendown()
            self.drawer.setpos(100, j)
            self.drawer.penup()
            j += 25
        # self.board=[[1,2,1,0],[1,2,1,0],[2,1,2,0],[2,1,2,0]]
        # z=random.randint(0,3)
        # self.board[z][0]=1
        # self.board[0][2]=2
        row_list=[0,25,50,75]
        col_list=[0,25,50,75][::-1]
        for i in range(4):
            for j in range(4):
                if self.board[i][j]==1:
                    color(row_list[i],col_list[j],1,self.screen)
                if self.board[i][j]==2:
                    color(row_list[i],col_list[j],2,self.screen)
        self.screen.onclick(self.clicked)
        self.screen.listen()


    def switchPlayer(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1


    # def checkForWinner(self):
    
    #     for i in range(4):
    #         for j in range(4):

    #             #to check each tile vertically upwards
    #             try:
    #                 player1 = 0
    #                 player2 = 0
    #                 for k in range(3):
    #                     space = self.grid[i][j+k]
    #                     if space.__repr__() == 1:
    #                         player1 += 1
    #                     if space.__repr__() == 2:
    #                         player2 += 1
    #                 if player1 == 3:
    #                     print("Congrats! Player 1 -green- won in column {} :)".format(i+1))
    #                     turtle.exitonclick()
    #                 elif player2 == 3:
    #                     print("Congrats! Player 2 -purple- won in column {}! :)".format(i+1))
    #                     turtle.exitonclick()
    #             except:
    #                 pass

    #             #to check each tile horizontally to the right
    #             try:
    #                 player1 = 0
    #                 player2 = 0
    #                 for k in range(3):
    #                     space = self.grid[i+k][j]
    #                     if space.__repr__() == 1:
    #                         player1 += 1
    #                     if space.__repr__() == 2:
    #                         player2 += 1
    #                 if player1 == 3:
    #                     print("Congrats! Player 1 -green- won in row {}! :)".format(j+1))
    #                     turtle.exitonclick()
    #                 elif player2 == 3:
    #                     print("Congrats! Player 2 -purple- won in row {}! :)".format(j+1))
    #                     turtle.exitonclick()
    #             except:
    #                 pass

    #             #to check each tile diagonally up to the right
    #             try:
    #                 player1 = 0
    #                 player2 = 0
    #                 for k in range(3):
    #                     space = self.grid[i+k][j+k]
    #                     if space.__repr__() == 1:
    #                         player1 += 1
    #                     if space.__repr__() == 2:
    #                         player2 += 1
    #                 if player1 == 3:
    #                     print("Congrats! Player 1 -green- won with a diagonal! :)")
    #                     turtle.exitonclick()
    #                 elif player2 == 3:
    #                     print("Congrats! Player 2 -purple- won with a diagonal! :)")
    #                     turtle.exitonclick()
    #             except:
    #                 pass

    #             #to check each tile diagonally up to the left
    #             try:
    #                 player1 = 0
    #                 player2 = 0
    #                 for k in range(3):
    #                     space = self.grid[i-k][j+k]
    #                     if space.__repr__() == 1:
    #                         player1 += 1
    #                     if space.__repr__() == 2:
    #                         player2 += 1
    #                 if player1 == 3:
    #                     print("Congrats! Player 1 -green- won with a diagonal! :)")
    #                     turtle.exitonclick()
    #                 if player2 == 3:
    #                     print("Congrats! Player 2 -purple- won with a diagonal! :)")
    #                     turtle.exitonclick()
    #             except:
    #                 pass


    # def checkIfFull(self):
    #     full = True
    #     for colnum in range(4):
    #         for rownum in range(4):
    #             if isinstance(self.grid[colnum][rownum], EmptySpace):
    #                 full = False
    #     if full == True:
    #         print("Board is full - no winner! You should play again :)")
                

    def clicked(self, x, y):
        # print self.seen
        # print self.player
        if self.player==2:
            self.x = x
            self.y = y
            if int(self.y) in range(0,100):
                if int(self.x) in range(0,25):
                    self.column = 1
                    self.spacex = 0
                elif int(self.x) in range(25, 50):
                    self.column = 2
                    self.spacex = 25
                elif int(self.x) in range(50, 75):
                    self.column = 3
                    self.spacex = 50
                elif int(self.x) in range(75,100):
                    self.column = 4
                    self.spacex = 75
                else:
                    return
            columnlist = self.board[self.column-1]
            spaceylist = [75, 50, 25, 0]#, 100, 125, 150, 175, 200, 225]
            notplaced = True
            i = 0
        
            while notplaced and i<=3:
                if columnlist[i]== 0:
                    self.spacey = spaceylist[i]
                    columnlist[i] = self.player
                    color(self.spacex,self.spacey,2,self.screen)
                    # print "colored"
                    # columnlist[i] = FullSpace(self.spacex, self.spacey, self.player)
                    notplaced = False
                else:
                    i += 1
            if notplaced == False:
                self.switchPlayer()
            if notplaced == True:
                print("Column full - try another column.")
                return
            isterminal,value=terminal_test(mystate(self.board,None,1),1)
            if isterminal:
                if value== 1:
                    print "Winner Bot"
                    print "GAMEOVER"
                    self.screen.onclick(None)
                    return
                elif value==-1:
                    print "Winner Human"
                    print "GAMEOVER"
                    self.screen.onclick(None)
                    return
                elif value==0:
                    print "DRAW"
                    print "GAMEOVER"
                    self.screen.onclick(None)
                    return
            else:
                pass
                # print "Game ON"

        # elif self.player==1:
        
        print "bot's turn"
        # self.column=minimax(mystate(self.board,None,1),1,self.seen)
        # self.column=alphabeta(mystate(self.board,None,1),1)
        self.column=myminimax(mystate(self.board,None,1),1,self.seen)
        self.spacex=(25*(self.column-1))
        columnlist = self.board[self.column-1]
        spaceylist = [75, 50, 25, 0]#, 100, 125, 150, 175, 200, 225]
        notplaced = True
        i = 0
    
        while notplaced and i<=3:
            if columnlist[i]== 0:
                self.spacey = spaceylist[i]
                columnlist[i] = self.player
                color(self.spacex,self.spacey,1,self.screen)
                # columnlist[i] = FullSpace(self.spacex, self.spacey, self.player)
                notplaced = False
            else:
                i += 1
        if notplaced == False:
            self.switchPlayer()
        if notplaced == True:
            print("Column full - try another column.")

        isterminal,value=terminal_test(mystate(self.board,None,1),1)
        if isterminal:
            if value== 1:
                print "Winner Bot"
                print "GAMEOVER"
                self.screen.onclick(None)
            elif value==2:
                print "Winner Human"
                print "GAMEOVER"
                self.screen.onclick(None)
            elif value==0:
                print "DRAW"
                print "GAMEOVER"
                self.screen.onclick(None)
        else:
            print "your turn"
                        # print "Game ON"
            # self.checkForWinner()
            # self.checkIfFull()

if __name__=="__main__":                
    play = ConnectThree()
    turtle.done()