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


def alphabeta(state,bot):
    value,action=max_value(state,bot,-2,2)
    return action

def max_value(state,bot,alpha,beta):
    isterminal,utilityvalue = terminal_test(state,bot) 
    if isterminal:
        return utilityvalue,None
    action=None
    value=-2
    for succesor in state.succesor_function():
        temp,_=min_value(succesor,bot,alpha,beta)
        if temp>value:
            value=temp
            action=succesor.action
        if value>=beta:
            return value,action
        alpha=max(alpha,value)
    return value,action

def min_value(state,bot,alpha,beta):
    isterminal,utilityvalue = terminal_test(state,bot) 
    if isterminal:
        return utilityvalue,None
    value=2
    action=None
    for succesor in state.succesor_function():
        temp,_=max_value(succesor,bot,alpha,beta)
        if temp<value:
            value=temp
            action=succesor.action
        if value<=alpha:
            return value,action
        beta=min(beta,value)
    return value,action

if __name__=="__main__":
    print "Use finalgui.py"
    