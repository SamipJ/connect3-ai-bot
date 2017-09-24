import copy

class mystate:
    def __init__(self,board,action,player):
        self.player=player
        self.action=action
        self.board=board

    def changeplayer(self):
        if self.player == 1:
            return 2
        else:
            return 1

    def __str__(self):
        return self.action
    def __repr__(self):
        return str(self.action)

    def succesor_function(self):
        succesorlist=[]
        for i in range(4):
            for j in range(4):
                if self.board[i][j]==0:
                    newboard=copy.deepcopy(self.board)
                    newboard[i][j]=self.player
                    succesorlist.append(mystate(newboard,i+1,self.changeplayer()))
                    break
        # print succesorlist
        return succesorlist
                
def terminal_test(state,bot):
    full = True
    player=bot
    other=1 if player==2 else 2
    for i in range(4):
        for j in range(4):
            #to check each tile vertically upwards
            try:
                # print "upwards"   
                player1 = 0
                player2 = 0
                for k in range(3):
                    space = state.board[i][j+k]
                    if space == player:
                        player1 += 1
                    if space == other:
                        player2 += 1
                if player1 == 3:
                    return True,1
                elif player2 == 3:
                    return True,-1
            except:
                pass

            #to check each tile horizontally to the right
            try:
                # print "right"
                player1 = 0
                player2 = 0
                for k in range(3):
                    space = state.board[i+k][j]
                    if space == player:
                        player1 += 1
                    if space == other:
                        player2 += 1
                if player1 == 3:
                    return True, 1
                elif player2 == 3:
                    return True,-1
            except:
                pass

            #to check each tile diagonally up to the right
            try:
                # print "diag right"
                player1 = 0
                player2 = 0
                for k in range(3):
                    space = state.board[i+k][j+k]
                    if space == player:
                        player1 += 1
                    if space == other:
                        player2 += 1
                if player1 == 3:
                    return True,1
                elif player2 == 3:
                    return True ,-1
            except:
                pass

            #to check each tile diagonally up to the left
            try:
                # print "diag left"
                player1 = 0
                player2 = 0
                for k in range(3):
                    if i-k>=0:
                        space = state.board[i-k][j+k]
                        # print space,i-k,j+k
                        if space == player:
                            player1 += 1
                        if space == other:
                            player2 += 1
                if player1 == 3:
                    return True, 1
                if player2 == 3:
                    return True,-1
            except:
                pass
            
            if state.board[i][j]==0:
                    full = False
    
    if full == True:
            return True,0
    
    else:
        return False,0


def minimax(state,bot):
    print state.board,"max"
    maximumvalue=-2
    action="No move possible"
    next1=None
    isterminal,utilityvalue = terminal_test(state,bot) 
    if isterminal:
        print ("utilityvalue",utilityvalue)
        return utilityvalue
    for succesor in state.succesor_function():
        value=min_value(succesor,bot)
        # print ("value",value)
        if maximumvalue < value:
            maximumvalue=value
            action=succesor.action
            next1=succesor
    print action,state.player
    return action,next1

def max_value(state,bot):
    print state.board,"max"
    isterminal,utilityvalue = terminal_test(state,bot) 
    if isterminal: return utilityvalue
    maximumvalue=-2
    for succesor in state.succesor_function():
        maximumvalue=max(maximumvalue,min_value(succesor,bot))
    return maximumvalue

def min_value(state,bot):
    print state.board,"min"
    isterminal,utilityvalue = terminal_test(state,bot) 
    if isterminal: return utilityvalue
    minimumvalue=2
    for succesor in state.succesor_function():
        minimumvalue=min(minimumvalue,max_value(succesor,bot))
    return minimumvalue

if __name__=="__main__":
    board=[[1,2,1,0],[2,2,1,0],[1,1,2,0],[2,1,2,0]]
    initialstate=mystate(board,None,2)
    curstate=initialstate
    # while(curstate!=None):
    a,curstate=minimax(curstate,2)
        # if curstate==None: break
        # a,curstate=minimax(curstate,2)