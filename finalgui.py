#SAMIP JASANI 2015A7PS0127P
from minimax import *
from alphabeta import *
from myversion import *
import random
import turtle
from time import time
import sys

def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

def color(x,y,player,screen):
    t = turtle.Turtle()
    # screen.tracer(1)
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

def erasableWrite(tortoise, name, font, reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.color("blue")
    eraser.write(name, font=font, align="left")
    return eraser

class ConnectThree:

    def __init__(self,algo):
        # changes player every time a successful move has been made
        if algo=="minimax":
            self.algo=minimax
        elif algo=="alphabeta":
            self.algo=alphabeta
        else:
            self.algo=myminimax
        self.screenSetup(algo)

    def screenSetup(self,algo):
        self.player = 1 #BOT First
        # self.player = 2 #Human First
        self.board=[[0]*4 for _ in range(4)]
        self.seen={}
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
        
        t = turtle.Turtle()
        t.hideturtle()
        t.up()
        t.goto(-80,85)
        t.write("Restart Using :", font=("Arial", 20, "normal"))
        t.goto(-70,70)
        t.write("Minimax Algorithm", font=("Arial", 16, "normal"))
        t.goto(-70,55)
        t.write("Alpha-Beta Pruning", font=("Arial", 16, "normal"))
        t.goto(-70,40)
        t.write("Minimax using Depth Heuristic", font=("Arial", 16, "normal"))
        t.goto(-80,25)
        t.write("Exit", font=("Arial", 20, "normal"))
        self.drawer.hideturtle()
        self.drawer.up()
        self.drawer.goto(-80,10)
        if algo != "blank":
            self.erasable = erasableWrite(self.drawer, "Click anywhere to start", font=("Arial", 20, "normal"))
            self.screen.onclick(self.clicked)
        else:
            self.erasable = erasableWrite(self.drawer, "No game selected", font=("Arial", 20, "normal"))
            self.screen.onclick(self.restart)
        self.screen.listen()


    def switchPlayer(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

                
    def restart(self,x,y):
        # print x,y
        if int(x) in range(-80,0):
            if int(y) in range(70,80):
                print "minmax"
                turtle.clearscreen()
                self.algo=minimax
                self.screenSetup(self.algo)
                return True
            elif int(y) in range(50,60):
                print "alphabeta"
                turtle.clearscreen()
                self.algo=alphabeta
                self.screenSetup(self.algo)
                return True
            elif int(y) in range(35,45):
                print "heuristic"
                turtle.clearscreen()
                self.algo=myminimax
                self.screenSetup(self.algo)
                return True
            elif int(y) in range(25,35):
                print "exit"
                turtle.bye()
                return True
        else :
            return False

    def resultofgame(self,value):
        if value== 1:
            self.erasable.clear()
            self.drawer.goto(-80,10)
            self.erasable = erasableWrite(self.drawer, "MACHINE WINS", font=("Arial", 20, "normal"), reuse=self.erasable)
            print "Winner Bot"
            print "GAMEOVER"
            self.screen.onclick(self.restart)
            return True
        elif value==-1:
            self.erasable.clear()
            self.drawer.goto(-80,10)
            self.erasable = erasableWrite(self.drawer, "HUMAN WINS", font=("Arial", 20, "normal"), reuse=self.erasable)
            print "Winner Human"
            print "GAMEOVER"
            self.screen.onclick(self.restart)
            return True
        elif value==0:
            self.erasable.clear()
            self.drawer.goto(-80,10)
            self.erasable = erasableWrite(self.drawer, "ITS DRAW", font=("Arial", 20, "normal"), reuse=self.erasable)
            print "DRAW"
            print "GAMEOVER"
            self.screen.onclick(self.restart)
            return True
        else: return False

    def clicked(self, x, y):
        # print self.seen
        # print self.player
        if self.restart(x,y):
            return
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
            # print get_size(mystate(self.board,None,1))
            if isterminal:
                if self.resultofgame(value):
                    return
            else:
                pass
                # print "Game ON"

        # elif self.player==1:
        print "bot's turn"
        self.erasable.clear()
        self.drawer.goto(-80,10)
        self.erasable = erasableWrite(self.drawer, "Wait!! Its BOT'S TURN", font=("Arial", 20, "normal"), reuse=self.erasable)
        # self.column=minimax(mystate(self.board,None,1),1,self.seen)
        # self.column=alphabeta(mystate(self.board,None,1),1)
        t1=time()
        self.column=self.algo(mystate(self.board,None,1),1,self.seen)
        print round(time()-t1,3)
        print len(self.seen)
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
            if self.resultofgame(value):
                return
        else:
            print "your turn"
            self.erasable.clear()
            self.drawer.goto(-80,10)
            self.erasable = erasableWrite(self.drawer, "YOUR TURN", font=("Arial", 20, "normal"), reuse=self.erasable)
                        # print "Game ON"
            # self.checkForWinner()
            # self.checkIfFull()

def results():
    screen = turtle.Screen()
    screen.setup(width=400,height=600)
    # self.screen.reset()
    screen.setworldcoordinates(-10,0,110,130)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    t.goto(0,120)
    t.write("R1  : 65752", font=("Arial", 16, "normal"))
    t.goto(0,110)
    t.write("R2  : 1088 Bytes", font=("Arial", 16, "normal"))
    t.goto(0,100)
    t.write("R3 : 16", font=("Arial", 16, "normal"))
    t.goto(0,90)
    t.write("R4 : 9.85 sec", font=("Arial", 16, "normal"))
    t.goto(0,80)
    t.write("R5 : 0.0067 nodes per microsec", font=("Arial", 16, "normal"))
    t.goto(0,70)
    t.write("R6 : 2733", font=("Arial", 16, "normal"))
    t.goto(0,60)
    t.write("R7 : 0.9585",font=("Arial", 16, "normal"))
    t.goto(0,50)
    t.write("R8 : 0.42 sec", font=("Arial", 16, "normal"))
    t.goto(0,40)
    t.write("R9 : 68MB vs 3MB", font=("Arial", 16, "normal"))
    t.goto(0,30)
    t.write("R10 : 9.94 sec vs 0.382 sec", font=("Arial", 16, "normal"))
    t.goto(0,20)
    t.write("R11 : 10 - M always wins", font=("Arial", 16, "normal"))
    t.goto(0,10)
    t.write("R12 : 10 - M always wins", font=("Arial", 16, "normal"))
    t.goto(0,0)
    t.write("R13 : 9.85 sec vs 0.42 sec", font=("Arial", 16, "normal"))
    
if __name__=="__main__":                
    # play = ConnectThree("myminimax")
    # turtle.done()
    # print"hey"
    results()
    turtle.done()
