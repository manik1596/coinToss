from tkinter import *;

DOLLARS = 25


def matrixMultiply(a,b):
    c = []
    for i in range(len(a)):
        c.append([0] * len(b[0]))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

def createTransitionMatrix():
    transitionMatrix = []
    for i in range(DOLLARS+1):
        transitionMatrix.append([0] * (DOLLARS+1))
    transitionMatrix[0][0] = 1
    transitionMatrix[DOLLARS][DOLLARS] = 1
    for i in range(DOLLARS+1):
            if(i != DOLLARS and i+1 != DOLLARS):
                transitionMatrix[i][i+1] = 0.5
            if(i != 0 and i-1 != 0):
                transitionMatrix[i][i-1] = 0.5
    return transitionMatrix

def createStartingMatrix(initCash):
    startingMatrix = [[0]] * (DOLLARS+1)
    startingMatrix[initCash] = [1]
    return startingMatrix

def calcProbability(tMatrix,sMatrix,c):
    for i in range(c):
        sMatrix = matrixMultiply(tMatrix,sMatrix)
    return sMatrix
    
def getCash(e1,e2):
    startingCash = int(e1.get())
    coinTossNumber = int(e2.get())
    transitionMatrix = createTransitionMatrix()
    startingMatrix = createStartingMatrix(startingCash)
    resultMatrix = calcProbability(transitionMatrix,startingMatrix,coinTossNumber)
    output = Tk()
    j = 0
    for i in resultMatrix:
        Label(output,justify = LEFT,text = 'Chance of having ' + str(j) + ' dollars:' + str(i[0] * 100) + '%').pack()
        j += 1
    output.mainloop()

top = Tk()
top.title('Coin Toss Cash Prediction')
top.geometry('200x200')
l1 = Label(top,text = 'Enter starting cash')
l1.pack()
e1 = Entry(top,width = 10)
e1.pack()
l2 = Label(top,text = 'Enter coin toss number')
l2.pack()
e2 = Entry(top,width = 10)
e2.pack()
b1 = Button(top,text = 'Enter',command = lambda: getCash(e1,e2))
b1.pack()
top.mainloop()