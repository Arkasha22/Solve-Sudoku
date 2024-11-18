#Script to solve Sudoku puzzles
#Created by Donald Maruta 08 Nov 24

#Import modules
import pandas as pd
import os, random

os.chdir(r'c:\temp')

#Read CSV file with Sudoku puzzle in it
sudoku = pd.read_csv('sudoku.csv', header=None, keep_default_na=False)

print(sudoku)

ctSpcNum = 1 #Counter for number of runs

#Code to solve Sudoku
while ctSpcNum > 0:
    oldCtSpcNum = ctSpcNum
    for x in range(9):
        for y in range(9):
            if sudoku.iloc[x,y] == '':
                allVals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                tempCol = sudoku[y].tolist()
                tempCol = list(filter(None, tempCol))
                tempCol = [int(i) for i in tempCol]
                allVals = list(set(allVals) - set(tempCol))
                tempRow = sudoku.loc[x, :].values.tolist()
                tempRow = list(filter(None, tempRow))
                tempRow = [int(i) for i in tempRow]
                allVals = list(set(allVals) - set(tempRow))
                tempX = int(x / 3)
                tempY = int(y / 3)
                tmpSudoku = sudoku.iloc[(tempX * 3): (tempX * 3) + 3, (tempY * 3): (tempY * 3) + 3]
                tmpLst = tmpSudoku.values.tolist()
                tmpLst = sum(tmpLst, [])
                tmpLst = list(filter(None, tmpLst))
                tmpLst = [int(i) for i in tmpLst]
                allVals = list(set(allVals) - set(tmpLst))
                if len(allVals) == 1:
                    sudoku.iloc[x,y] = allVals[0]
    ctSpc = sudoku.values.tolist()
    ctSpc = sum(ctSpc, [])
    ctSpcNum = ctSpc.count('')
    print(ctSpcNum)
    if ctSpcNum == oldCtSpcNum:
        print(sudoku)
        break
