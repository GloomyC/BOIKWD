# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:02:28 2019

@author: Gloomy
"""


class Gamestate:
    def __init__(self,P1,P2,turn,lastTaken,P1touched,P2touched,coins,parent):
        #P1: current score of P1
        #P2: current score of P2
        #lastTaken: amount of coins taken during last move
        #P1touched: boolean list, which stacks has P1 interacted with
        #P2touched: boolean list, which stacks has P2 interacted with
        #coins: integer list of coins left on stacks
        #turn: either "P1" or "P2"
        #next: list of Gamestates
        #parent: parent, only used for getTrace
        self.P1 = P1
        self.P2 = P2
        self.lastTaken = lastTaken
        self.P1touched = P1touched 
        self.P2touched = P2touched
        self.coins = coins
        self.turn = turn
        self.next = [] 
        self.parent = parent
        
    def nextTurn(self):
        if self.turn == "P1":
            return "P2"
        else:
            return "P1"
    
    #return list with possible amounts of coins to take from given stack
    def possibleTakes(self,stack_num):
        if self.coins[stack_num] == 0:
            return []
        if self.lastTaken == 0 and self.coins[stack_num] >=1:
            return [1]
        result = []
        j= 1
        while j <= self.coins[stack_num] and j <= self.lastTaken*2:
            result.append(j)
            j+=1
        return result
    
    def addSubstates(self,substates):
        self.next = self.next + substates
    
    #creates all valid moves
    def genPossibleSubstates(self):
        result = []
        n = len(self.coins)
        currMove = self.turn
        nextMove = self.nextTurn()
        
        #consider which stacks can current player interact with
        if currMove == "P1":
            consideredTouches = self.P1touched
        else:
            consideredTouches = self.P2touched
        
        madeMove = False
        for i in range(n):
            #if stack touched, skip
            if consideredTouches[i] == True:
                continue
            
            takes = self.possibleTakes(i)
            
            #for each stack player can interact with, generate branch for each possible amount taken
            for takevalue in takes:
                if currMove == "P1":
                    newTouchP1 = self.P1touched.copy()
                    newTouchP1[i] = True
                    
                    newTouchP2 = self.P2touched.copy()
                    
                    newCoin = self.coins.copy()
                    newCoin[i] -= takevalue
                    
                    newP1 = self.P1+takevalue
                    
                    result.append(Gamestate(newP1,self.P2,nextMove,takevalue,newTouchP1,newTouchP2,newCoin,self))
                    madeMove = True
                else:
                    newTouchP1 = self.P1touched.copy()
                    
                    newTouchP2 = self.P2touched.copy()
                    newTouchP2[i] = True
                    
                    newCoin = self.coins.copy()
                    newCoin[i] -= takevalue
                    
                    newP2 = self.P2+takevalue
                    
                    result.append(Gamestate(self.P1,newP2,nextMove,takevalue,newTouchP1,newTouchP2,newCoin,self))
                    madeMove = True
                    
        #if moves couldn't be generated for current player, check if there exist any valid moves
        if not madeMove:
            
            gameOver = True
            
            for i in range(len(self.coins)):
                if self.coins[i] != 0 and (self.P1touched[i] == False or self.P2touched[i] == False):
                    gameOver = False
                    break
            if not gameOver:
                result.append(Gamestate(self.P1,self.P2,nextMove,self.lastTaken,self.P1touched.copy(),self.P2touched.copy(),self.coins.copy(),self))
        self.addSubstates(result)
                
    def makeTree(self):
        self.genPossibleSubstates()
        for state in self.next:
            state.makeTree()
            
    def __repr__(self):
        return "P1:{0}, P2:{1}, coins{2}".format(self.P1,self.P2,self.coins)
    
    def getTrace(self):
        x = self
        while x != None:
            print(str(x))
            x = x.parent
        

#creates initial game start node
def makeInitState(coins):
    P1touched = []
    P2touched = []
    for i in range(len(coins)):
        P1touched.append(False)
        P2touched.append(False)
    return Gamestate(0,0,"P1",0,P1touched,P2touched,coins,None)


def minmaxTree(tree : Gamestate):
    #if leaf, return self
    if len(tree.next) == 0:
        return tree
    #if not leaf, agregate minmaxTree results from all possible moves
    choices = []
    for move in tree.next:
        choices = choices + [minmaxTree(move)]
    
    #if P1 choose best minmax for P1 from choices
    if tree.turn == "P1":
        result = max(choices,key= (lambda x : x.P1-x.P2))
    #if P2 choose worst minmax for P1 from choices
    else:
        result = min(choices,key= (lambda x : x.P1-x.P2))
        
    return result

#turns whole tree into string with indents
def strFromTree(tree: Gamestate,depth):
    s = ""
    for i in range(depth):
        s = s+" "
    s = s+ str(tree) + "\n"
    for subtree in tree.next:
        s = s+ strFromTree(subtree,depth+1)
    
    return s


#========================
coins = [2,2,2]
gameTree = makeInitState(coins)
gameTree.makeTree()

result = minmaxTree(gameTree)

#print(strFromTree(gameTree,0))

print("===========")
print("game: {0}".format(coins))
print("minmax game outcome:")
print(str(result))
print("----------")
print("minmax game trace:")
result.getTrace()
print("===========")

#========================
coins = [3,3,3]
gameTree = makeInitState(coins)
gameTree.makeTree()

result = minmaxTree(gameTree)

print("===========")
print("game: {0}".format(coins))
print("minmax game outcome:")
print(str(result))
print("----------")
print("minmax game trace:")
result.getTrace()
print("===========")

#========================
coins = [1,2,6]
gameTree = makeInitState(coins)
gameTree.makeTree()

result = minmaxTree(gameTree)

print("===========")
print("game: {0}".format(coins))
print("minmax game outcome:")
print(str(result))
print("----------")
print("minmax game trace:")
result.getTrace()
print("===========")
