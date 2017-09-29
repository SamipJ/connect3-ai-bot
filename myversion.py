import copy
import random
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
    
        
    def __eq__(self,other):
        return self.__dict__==other.__dict__

    def __ne__(self, other):
        return (not self.__eq__(other))
    
    def __hash__(self):
        return hash(self.__repr__())

    def __str__(self):
        return str(self.board)+" "+str(self.player)
    def __repr__(self):
        return str(self.board)+" "+str(self.player)

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


def myminimax(state,bot,seen):
    maximumvalue=-2
    action="No move possible"
    nextsuccesor=None
    for succesor in state.succesor_function():
        value,depth=min_value(succesor,bot,seen)
        # print "action: ",succesor.action,"value: ",value,"depth: ",depth
        if maximumvalue < value:
            maximumvalue=value
            nextsuccesor=[]
            nextsuccesor.append((depth,succesor.action))
        elif maximumvalue==value:
            nextsuccesor.append((depth,succesor.action))
    # print nextsuccesor
    if maximumvalue==-1:
        nextsuccesor.sort(reverse=True)
        depth,action=nextsuccesor[0]
    elif maximumvalue==1:
        nextsuccesor.sort()
        depth,action=nextsuccesor[0]
    else:
        depth,action=random.choice(nextsuccesor)
    # print action,state.player
    return action#,next1.board

def max_value(state,bot,seen):
    # print state.board,"max"
    isterminal,utilityvalue = terminal_test(state,bot) 
    if isterminal:
        # print state , utilityvalue
        return utilityvalue,0
    maximumvalue=-2
    for succesor in state.succesor_function():
        if seen.has_key(succesor):
            # print "yeh2"
            value,depth=seen[succesor]
        else:
            # print str(succesor.board)+" "+str(succesor.player)
            value,depth=min_value(succesor,bot,seen)
            seen[succesor]=(value,depth)
            # print str(succesor.board)+" "+str(succesor.player)
            # print seen
        # maximumvalue=max(maximumvalue,value)
        if maximumvalue<value:
            maximumvalue=value
            nextsuccesor=[]
            nextsuccesor.append(depth)
        elif maximumvalue==value:
            nextsuccesor.append(depth)
    # if maximumvalue==1:
    nextsuccesor.sort()
    depth=nextsuccesor[0]+1
    # else:
    #     nextsuccesor.sort(reverse=True)
    #     depth=nextsuccesor[0]+1
    return maximumvalue,depth

def min_value(state,bot,seen):
    # print state.board,"min"
    isterminal,utilityvalue = terminal_test(state,bot) 
    if isterminal:
        # print state , utilityvalue
        return utilityvalue,0
    minimumvalue=2
    for succesor in state.succesor_function():
        if seen.has_key(succesor):
            # print "yeh"
            value,depth=seen[succesor]
        else:
            value,depth=max_value(succesor,bot,seen)
            seen[succesor]=(value,depth)
        # minimumvalue=min(minimumvalue,value)
        if minimumvalue>value:
            minimumvalue=value
            nextsuccesor=[]
            nextsuccesor.append(depth)
        elif minimumvalue==value:
            nextsuccesor.append(depth)
    # if minimumvalue==1:
    nextsuccesor.sort()
    depth=nextsuccesor[0]+1
    # else:
    #     nextsuccesor.sort(reverse=True)
    #     depth=nextsuccesor[0]+1
    return minimumvalue,depth

if __name__=="__main__":
    print "Use finalgui.py"
    # board=[[1,2,1,0],[2,2,1,0],[1,1,2,0],[2,1,2,0]]
    # initialstate=mystate(board,None,2)
    # curstate=initialstate
    # # while(curstate!=None):
    # a,curstate=minimax(curstate,2)
        # if curstate==None: break
        # a,curstate=minimax(curstate,2)