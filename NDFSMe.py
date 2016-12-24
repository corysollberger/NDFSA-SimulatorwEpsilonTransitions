from random import randint
#By: Cory Sollberger  COS 451  Homework 5

#A function (FSM) that will take the input and determine the conclusion
#Input a 5-tuple (Q, Sigma, Delta, q0, F)
#Where Q = Finite set of states, Sigma = finite set of input symbols,
#Delta = Transition function, q0 = starting state, and F = set of final states.
def FSM(Q, Sigma, Delt, Q0, F, sInput):
    currentState = epsTrans(q0, Delt)
    
    #currentState = Q0 #Starting state
    for x in sInput:
        nextState = set() #empty set
        for y in currentState: #For each state in the currentState, plug back into FSM
            trans = 0 #number of transitions found
            for z in Delt:
                if (z[0] == y and z[1] == x):
                    trans = trans + 1
                    for a in range(len(z))[2:]: #Add all iterative states
                        nextState.add(z[a])
            if(trans == 0): #if no transition found, maintain state
                nextState.add(y)
        currentState = nextState
        currentState = epsTrans(currentState, Delt) #Add Epsilon Closure to states
    if (len(currentState.intersection(F))>0): #check if a final state
        return True
    else:
        return False

#Handles the epsilon transitions
#Creates an epsilon closure using the q0 argument, the current state of the FSM
def epsTrans(q0, Delt):
        done = True #tells us when we have gathered the epsilon-closure
        curStates = q0
        while(done):
            nextState = set();
            for y in curStates:
                for z in Delt:
                    if (z[0] == y and z[1] == '.'):
                        for a in range(len(z))[2:]: #Add all iterative states
                            nextState.add(z[a])
            prevState = set()
            prevState.update(curStates)
            curStates.update(nextState) #Repeatedly add states to the currentState
            if (curStates == prevState):
                done = False #Breaks the loop
        return curStates
    
#Read the desired information from a file
def readFSM(fileName):
    f = open(fileName, 'r') #opens file to read the 5 elements of the NDFA
    inpLines = []
    for line in f:
        inpLines.append(line.rstrip('\n'))

    count = 0
    for x in inpLines:
        if count == 0:
            q.clear()
            for a in inpLines[count]:
                q.add(a)
        elif count == 1:
            S.clear()
            for a in inpLines[count]:
                S.add(a)
        elif count == 2:
            delt.clear()
            s = ""
            for a in inpLines[count]:
                if a != ',':
                    s = s + a
                else:
                    tempTuple = ()
                    for t in s:
                        temp = (t,)
                        tempTuple = tempTuple + temp
                    delt.append(tempTuple)
                    s = ""
        elif count == 3:
            q0.clear()
            for a in inpLines[count]:
                q0.add(a)
        elif count == 4:
            F.clear()
            for a in inpLines[count]:
                F.add(a)
        count = count + 1

#Generates the String from the given expression
def generateString(ex):
    gen = ""
    char = ""
    block = ""
    for c in ex:    
        if (c == '*'):
            ran = randint(0,9)
            for x in range(0,ran):
                gen+=char
            char = ""
        elif(c == ','):
            gen+=char
            char = ""
        elif(c == '('):
            pass
        elif(c == ')'):
            pass
        else:
            char += c
    return gen
            

#Splits expression into possibilities, then sends to generate strings from the language
def splitExpression(regX):
    exp = []
    s = ""
    for c in regX:
        if (c == "|"):
            exp.append(s)
            s = ""
        else:
            s+=c
    exp.append(s)
    print (exp)
    for x in range (0,10):
        r = randint(0,2)
        gS = generateString(exp[r])
        regOutput.append(gS)
    
#Initialize the Variables for the FSM
q = set()
S = set()
delt = []
q0 = set()
F = set()

regExp = "0*|(0*,1,0*)*|(0*,11,0*)" #The Regular Expression that generates strings for prob5
regOutput = []
splitExpression(regExp)

#Problem 5
readFSM("hw5prb5.txt")
for str in regOutput:
    print (str)
    print (FSM(q, S, delt, q0, F, str)) #true
    
"""
#Problem 2 DFA & NDFA
readFSM("hw5prb2.txt")
print ("Problem 2:")
print (FSM(q, S, delt, q0, F, "ab")) #true
print (FSM(q, S, delt, q0, F, "aac")) #true
print (FSM(q, S, delt, q0, F, "bc")) #true
print (FSM(q, S, delt, q0, F, "")) #false
print (FSM(q, S, delt, q0, F, "bcbc")) #false
print (FSM(q, S, delt, q0, F, "aacaac")) #false
print (FSM(q, S, delt, q0, F, "abab")) #false
#Problem 4 NDFA
readFSM("hw5prb4.txt")
print ("Problem 4: Testing 10 Inputs")
print (FSM(q, S, delt, q0, F, "ab")) #true
print (FSM(q, S, delt, q0, F, "ca")) #true
print (FSM(q, S, delt, q0, F, "bca")) #true
print (FSM(q, S, delt, q0, F, "")) #true
print (FSM(q, S, delt, q0, F, "abbc")) #true
print (FSM(q, S, delt, q0, F, "aacc")) #true
print (FSM(q, S, delt, q0, F, "bbccaa")) #true
print (FSM(q, S, delt, q0, F, "abcabc")) #true
print (FSM(q, S, delt, q0, F, "accb")) #true
print (FSM(q, S, delt, q0, F, "abbbcbcbbabbabbc")) #true
"""


