
import sys
import math
import numpy as np
np.set_printoptions(threshold=np.nan)


prevBombTarget = -1

bombT1 =None
bombT2 = None
bombS1 =None
bombS2 = None
# send all bots to nearest factory that is neutral if all neutral attack nearest enemy
class Factory:
    "Class to store factory values"
    def __init__(self, i, owner, cyborgs, production, turns):
        self.i = i
        self.owner = owner
        self.cyborgs = cyborgs
        self.production = production
        self.turns = turns
    def __repr__(self):
        return 'i{},o{},c{},p{},t{}'.format(self.i,self.owner,self.cyborgs,self.production,self.turns)

class Troop:
    "Class to store troop values"
    def __init__(self, i, owner, source, target, amount, turns):
        self.i = i
        self.owner = owner
        self.source = source
        self.target = target
        self.amount = amount
        self.turns = turns
    def __repr__(self):
        return 'i{},o{},s{},t{},a{},turns{}'.format(self.i, self.owner, self.source, self.target, self.amount, self.turns)

def updateList():
       
    for i in range(len(factoryList)):
        if (factoryList[i].owner==1):
            ownedList.append(factoryList[i])
        elif (factoryList[i].owner==-1):
            enemyList.append(factoryList[i])
        elif (factoryList[i].owner==0):
            neutralList.append(factoryList[i])
    notOwnedList=[]
    notOwnedList=neutralList+enemyList


def findBombTargets():
    global prevBombTarget
    global enemyList
    global neutralList
    if (prevBombTarget!=-1):
        neutralList.append(factoryList[prevBombTarget])
    enemyList = list(set(enemyList)-set(neutralList))
    enemyList.sort(key=lambda fac: fac.cyborgs, reverse=True)
    print("bomb enemyList ",enemyList,file=sys.stderr)
    global bombT1
    bombT1 = enemyList[0].i
    '''
    global bombT2
    bombT2 = enemyList[1].i
    print("t1t2 ",bombT1,bombT2,file=sys.stderr)
    print("enemyList ",enemyList,file=sys.stderr)
    '''
    
    return 0
    
def findBombSource():
    initOwnedList.sort(key=lambda fac: fac.cyborgs,)
    global bombS1
    bombS1 = initOwnedList[0].i
    #global bombS2
    # = initOwnedList[1].i
    #print("s1s2 ",bombS1,bombS2,file=sys.stderr)
    #print("ownedList ",ownedList,file=sys.stderr)
    return 0
    
##################################################################################    
################################################################################## 

def mainSource():
    s = source()
    main = factoryInfo[s][2]
    mainId= s
    for i in range(factoryOwnedCount):
        if(factoryInfo[factoryOwned[i]][2]>main):
            main=factoryInfo[factoryOwned[i]][2]
            mainId=factoryInfo[factoryOwned[i]][0]
            
    print("main source ",mainId,file=sys.stderr)
    return mainId
    
##################################################################################    
##################################################################################  

def enemyMain(prevBombTarget): # fix by splitting notOwned into enemy and neutral or check it within this func
    main = 0
    mainId= 0
    if(prevBombTarget in factoryEnemy):
        factoryEnemy.remove(prevBombTarget)
    for i in range(len(factoryEnemy)):
        if(factoryInfo[factoryEnemy[i]][2]>main):
            main=factoryInfo[factoryEnemy[i]][2]
            mainId=factoryInfo[factoryEnemy[i]][0]
            #print("mainsource ,id, compare ",main,mainId,factoryInfo[factoryOwned[i]][2], file=sys.stderr)
    print("main enemy source ",mainId,file=sys.stderr)
    prevBombTarget = mainId
    return mainId


    for i in range(len(factoryEnemy)):
        if(factoryInfo[factoryEnemy[i]][2]>main):
            main=factoryInfo[factoryEnemy[i]][2]
            mainId=factoryInfo[factoryEnemy[i]][0]
            factoryInfo[factoryEnemy[i]][1]=1
    
    factoryEnemy.remove(mainId)
            #print("mainsource ,id, compare ",main,mainId,factoryInfo[factoryOwned[i]][2], file=sys.stderr)
    print("main enemy source ",mainId,file=sys.stderr)
    return mainId



##################################################################################    
##################################################################################


def lowSource():
    
    main = 9999
    mainId= 0
    for i in range(factoryOwnedCount):
        print("low source i ",i,file=sys.stderr)
        s = factoryOwned[i]
        if(factoryInfo[s][2]<main):
            main=factoryInfo[factoryOwned[i]][2]
            mainId=factoryInfo[factoryOwned[i]][0]
            #print("mainsource ,id, compare ",main,mainId,factoryInfo[factoryOwned[i]][2], file=sys.stderr)
    print("low source ",mainId,file=sys.stderr)
    return mainId


            
def dstn():
    if(len(factoryNotOwned)==0):
        return ((s+1)%len(factoryOwned))
    return factoryNotOwned[np.random.randint(0,len(factoryNotOwned))] 

def safe_div(x,y):
    if y == 0:
        return 0
    return x / y    
    
def amount(i):
    print("amount() ", math.floor(safe_div((factoryInfo[factoryOwned[i]][2]),2)), file=sys.stderr)   
   
    return  math.floor(safe_div((factoryInfo[factoryOwned[i]][2]),2))
    
def dist(s,d):
    dist = distInfo[s][d]
    distId = d
    for i in range(factoryNotOwnedCount):
        if(distInfo[s][factoryNotOwned[i]]<dist):
            dist = distInfo[s][factoryNotOwned[i]]
            distId=factoryNotOwned[i]
    print("dist() ",distId, file=sys.stderr)
    return distId

def checkDist(f1,f2):  
    
    return distInfo[f1][f2]
    

def target():
    for i in range(factoryNotOwnedCount):
        targetId = factoryNotOwned[i]
    return targetId
         
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
factoryOwned =[]
factoryNotOwned =[]
factoryEnemy=[]
factoryOwnedCount=0;
factoryNotOwnedCount=0;

#factoryInfo = np.zeros((15, 5))
factoryInfo = [[0 for i in range(5)] for j in range(15)]
print("factory ini \n",factoryInfo, file=sys.stderr)

bombInfo = [[0 for i in range(5)] for j in range(15)]
print("bomb ini \n",bombInfo, file=sys.stderr)

troopInfo = [[0 for i in range(6)] for j in range(1)]


factory_count = int(input())  # the number of factories

distInfo = [[99 for i in range(factory_count)] for j in range(factory_count)]
print("dist ini \n",distInfo, file=sys.stderr)
###############################################################################
###############################################################################

link_count = int(input())  # the number of links between factories
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    
    print("dist ",factory_1, factory_2, distance,file=sys.stderr)
    
    distInfo[factory_1][factory_2] = distance
    distInfo[factory_2][factory_1] = distance
print("dist ini \n",distInfo, file=sys.stderr)    


###############################################################################
###############################################################################
# game loop
turn=0
bombs = 2
while True:
    
    troopList=[]
    ownedList=[]
    enemyList=[]
    neutralList=[]
    factoryList=[]
    initOwnedList=[]
    notOwnedList =[]
    
    factoryOwnedCount=0;
    factoryNotOwnedCount=0;
   
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    for i in range(entity_count):
        entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
        entity_id = int(entity_id)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        arg_5 = int(arg_5)
        
        if (entity_type == "FACTORY"):
            if(arg_1==1):
                factoryOwned.append(i)
                factoryOwnedCount+=1
            else:
                factoryNotOwned.append(i) # todo split into neural and enemy
                factoryNotOwnedCount+=1
                
                if(arg_1==-1):
                    factoryEnemy.append(i)
                
            factoryInfo[i][0]=((i))  # ID 
            factoryInfo[i][1]=((arg_1))  # Owner
            factoryInfo[i][2]=((arg_2))  # # Cyborgs
            factoryInfo[i][3]=((arg_3))  # Production
            factoryInfo[i][4]=((arg_4)) # Turns until production
        
        ##############################################################
        ##############################################################
        
            fac = Factory(i,arg_1,arg_2,arg_3,arg_4)
            factoryList.append(fac)
            
            if (fac.owner==1):
                initOwnedList.append(fac)
            
            print("fac ",fac.i,fac.owner,fac.cyborgs, file=sys.stderr)
            
        if (entity_type == "BOMB"):
            
            bombInfo[0][1]=((arg_1))  # Owner
            bombInfo[0][2]=((arg_2))  # source
            bombInfo[0][3]=((arg_3))  # target
            bombInfo[0][4]=((arg_4)) # Turns until arrival
        
        if (entity_type == "TROOP"):
            
            troopInfo[0][1]=((arg_1))  # Owner
            troopInfo[0][2]=((arg_2))  # source
            troopInfo[0][3]=((arg_3))  # target
            troopInfo[0][4]=((arg_4))  # amount  
            troopInfo[0][5]=((arg_5))  # Turns until arrival
            
            troop = Troop(i,arg_1,arg_2,arg_3,arg_4,arg_5)
            if (troop.turns<3):
                troopList.append(troop)
            
    for i in range(len(troopList)):  # predicts future state of factories except enemy factories
        
        
        if(factoryList[troopList[i].target].owner == 1):
        
            factoryList[troopList[i].target].cyborgs += (troopList[i].amount*troopList[i].owner)    
            
            if ((factoryList[troopList[i].target].cyborgs)<0):
                factoryList[troopList[i].target].owner=-1
                factoryList[troopList[i].target].cyborgs = abs(factoryList[troopList[i].target].cyborgs)
        
        
        elif(factoryList[troopList[i].target].owner == 0):
            
            factoryList[troopList[i].target].cyborgs += (troopList[i].amount*troopList[i].owner)    
            
            if ((factoryList[troopList[i].target].cyborgs)<0):
                factoryList[troopList[i].target].owner=-1
                factoryList[troopList[i].target].cyborgs = abs(factoryList[troopList[i].target].cyborgs)        
                
            elif ((factoryList[troopList[i].target].cyborgs)>0):
                factoryList[troopList[i].target].owner=1    
        
        elif(factoryList[troopList[i].target].owner == -1):
            
            factoryList[troopList[i].target].cyborgs -= (troopList[i].amount*troopList[i].owner) 
            if ((factoryList[troopList[i].target].cyborgs)<0):
               factoryList[troopList[i].target].owner=1
               factoryList[troopList[i].target].cyborgs = abs(factoryList[troopList[i].target].cyborgs)        
           
    updateList()            
    '''
    for i in range(len(factoryList)):
        if (factoryList[i].owner==1):
            ownedList.append(factoryList[i])
        elif (factoryList[i].owner==-1):
            enemyList.append(factoryList[i])
        elif (factoryList[i].owner==0):
            neutralList.append(factoryList[i])
    '''        
    '''       
        #check 3 turns ahead    
        if  (troopInfo[0][5]<4):       
        # target friendly
            if(factoryInfo[troopInfo[0][3]][1]==1): 
                
                # re calc cyborgs in target fac
                factoryInfo[troopInfo[0][3]][2] += (troopInfo[0][4]*troopInfo[0][1])
                
                #if friendly fac has less than 0 borgs it has been converted to enemy
    if((factoryInfo[troopInfo[0][3]][2])<0):
        
        #factoryNotOwned.append(factoryInfo[troopInfo[0][3]][1])
        factoryInfo[troopInfo[0][3]][1]= 1
        factoryInfo[troopInfo[0][3]][2] = abs(factoryInfo[troopInfo[0][3]][2])
        factoryNotOwned.append(factoryInfo[troopInfo[0][3]][0])
        print("factoryOwned ",factoryOwned, file=sys.stderr)
        factoryOwned.remove(troopInfo[0][3]) # move this out of  for loop
    '''
#######################################################################################################       
        
        # target neutral
    '''
            elif(factoryInfo[troopInfo[0][3]][1]==0): 
                
                # re calc cyborgs in target fac
                factoryInfo[troopInfo[0][3]][2] -= (troopInfo[0][4])
                
                #if neutral fac has less than 0 borgs it has been converted to enemy or friendly xd
                if(factoryInfo[troopInfo[0][3]][2]<0):
                    
                    #factoryNotOwned.append(factoryInfo[troopInfo[0][3]][1])
                    factoryInfo[troopInfo[0][3]][1]= 1 # this is hack fix assume converted to friendly
                    factoryInfo[troopInfo[0][3]][2] = abs(factoryInfo[troopInfo[0][3]][2])     
                    
    '''
           #target enemy
    '''
            elif(factoryInfo[troopInfo[0][3]][1]==-1): 
                
                # re calc cyborgs in target fac
                if (troopInfo[0][1]==1):
                    factoryInfo[troopInfo[0][3]][2] -= troopInfo[0][4]
                elif(troopInfo[0][1]==-1):
                    factoryInfo[troopInfo[0][3]][2] += troopInfo[0][4]
                #if fac has less than 0 borgs it has been converted 
                if(factoryInfo[troopInfo[0][3]][2]<0):
                    
                    #factoryNotOwned.append(factoryInfo[troopInfo[0][3]][1])
                    factoryInfo[troopInfo[0][3]][1]= 1 
                    #factoryInfo[troopInfo[0][3]][2] = abs(factoryInfo[troopInfo[0][3]][2])     
    '''
                    
                
    # if all enemies within 3 turns < than friendl node = safe to increase production
    
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    #s = source()
    #s = mainSource()
    #print("main source ",mainSource(), file=sys.stderr)
    
    
#########################################################################
######################################################################### 
    
    commandString =""
    check = 0    
    frontDist = 20
    frontId =0
    minDist = 0
    maxDist = 20
    bombSource = None
    bombTarget = None
    spread =0
    
    notOwnedList=[]
    notOwnedList=neutralList+enemyList

    # todo can be improved by setting target borg count to 0/-50 while bomb is still on way
    # instead of just the instant turn the bomb is sent
    initOwnedList = list(set(initOwnedList)-set(enemyList))
    if (len(enemyList)>1 and bombs >0):
        findBombTargets()
        findBombSource()
        print("bombS1,bombT1,bombS2,bombT2, enemyList ",bombS1,bombT1,bombS2,bombT2,enemyList,file=sys.stderr)
        #commandString += "BOMB {} {};BOMB {} {};".format(bombS1,bombT1,bombS2,bombT2)
        commandString += "BOMB {} {};".format(bombS1,bombT1)
        bombs-=1
        factoryList[bombT1].cyborgs=0
        neutralList.append(factoryList[bombT1])
        enemyList = list(set(enemyList)-set(neutralList))
        prevBombTarget=bombT1
        #factoryList[bombT2].cyborgs=0
        updateList()

    initOwnedList = list(set(initOwnedList)-set(enemyList))
    for j in range(len(initOwnedList)):
        s = initOwnedList[j].i 
        minDist=1
        print("loop ",s ,file=sys.stderr)
        while (minDist<maxDist):
           
            #print("notOwned ",notOwnedList ,file=sys.stderr)    
            for z in range(len(notOwnedList)):
                d = notOwnedList[z].i
                print("minDist, s,d,loop ",minDist,factoryList[s].cyborgs,factoryList[d].cyborgs ,file=sys.stderr)
                #print("notOwned in z ",notOwnedList ,file=sys.stderr)
            # while main source still has cyborgs try to relocate them
            # try to sort it into closet nodes first ? or lowest neutral nodes
            # if dist / all surround nodes friendly, start distributing cyborgs between friendly nodes
                '''                
                if(notOwnedList[d].owner==1):
                    if ((factoryInfo[s][2]>abs((factoryInfo[d][2])+1))):
                        n = abs(factoryInfo[s][2])
                    
                        commandString += "MOVE {} {} {};".format(s,d,n)
                        factoryInfo[s][2]-=n
                        check +=1
                '''                  
                
                if ((factoryList[s].cyborgs>(factoryList[d].cyborgs)+1) and checkDist(s,d)<minDist and factoryList[d].production>0 ):
                     #and checkDist(s,d)<6 
                    if(checkDist(s,d)<frontDist):
                        frontId = d
                        frontDist = checkDist(s,d)
                    '''
                    if(factoryInfo[d][1]==-1):
                        n = factoryInfo[d][2]+1
                    else:
                        n =(factoryInfo[d][2]+1)
                    '''
                    n =(factoryList[d].cyborgs)+1
                    
                    commandString += "MOVE {} {} {};".format(s,d,n)
                    factoryList[s].cyborgs-= n
                    check +=1
                

                    
                    
            minDist+=1
            
            if ( check==0): 
                lowAllyId = None
                lowAlly = 20
                allyDist = 20
                allyId = None
                d = s+1%len(ownedList)
                
                
                if((factoryList[s].cyborgs)>0):
                    
                    for x in range(len(ownedList)):
                        if (ownedList[x].i!=s):
                            d = ownedList[x].i
                        if(checkDist(d,frontId)<checkDist(s,frontId) and checkDist(s,d)<allyDist ):
                            #factoryList[d].cyborgs<lowAlly and
                            #lowAllyId = d 
                            #lowAlly = factoryList[d].cyborgs
                            allyDist = checkDist(s,d)
                            allyId = d
                    #if(factoryList[s].cyborgs>lowAlly and lowAllyId!=None):
                    #n = round((factoryList[s].cyborgs+lowAlly)/2)
                    if(allyId!=None):
                        n = factoryList[s].cyborgs
                        commandString += "MOVE {} {} {};".format(s,allyId,n)
                        factoryList[s].cyborgs-=n
                
                        
                if(factoryList[s].cyborgs>=20):
                    commandString += "INC {};".format(s)
                    factoryList[s].cyborgs-=10
                
                '''
                if(s!=frontId and factoryInfo[s][2]>10):
                    n = factoryInfo[s][2]
                    commandString += "MOVE {} {} {};".format(s,frontId,n)
                    factoryInfo[s][2]-=n
                '''
                '''
                elif(s!=frontId):
                    n = (factoryInfo[s][2]+factoryInfo[s][3])
                    commandString += "MOVE {} {} {};".format(s,frontId,n)
                '''
            # replace this with distribute friendly nodes that are close to enemy nodes
            '''
            if (minDist==maxDist and check==0):
                   
                   for i in range(factoryOwnedCount):
                       d = factoryOwned[i]
                       
                       if ((factoryInfo[s][2]>(factoryInfo[d][2]+1)) and checkDist(s,d)<minDist):
                           n =(factoryInfo[d][2]+1)
                           commandString += "MOVE {} {} {};".format(s,d,n)
                           check +=1
                           factoryInfo[s][2]-=(factoryInfo[d][2]+1)
             '''      
                  
        minDist=1
        check=0
        
        
    if(commandString==""):
        print("WAIT")
    else:
        print(commandString[:-1])            
            
    
   # print("rand fac ",source(),file=sys.stderr)
    factoryOwned=[]
    factoryNotOwned =[]
    factoryEnemy=[]
    ammo=0
    turn+=1
    

    
