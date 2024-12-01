import random

class Matrix:
    def __init__(self, m, n):
        self.m = m #// rows
        self.n = n #   cols
        self.matrix = [[random.randint(1,30) for _ in range(m)] for _ in range(n)] #Generate random in constructor
    
    def printMatrix(self): #print matrix row by row
        for row in self.matrix:
            print(row)

    def meanOfTheMatrix(self): 
        for row in self.matrix: # getting total matrix Sum row by row and dividing by k
            matrixSum =+ sum(row)
        k = self.n * self.m 
        print(matrixSum / k)

    def sumOfTheGiveRow(self, givenRow): 
        if givenRow < 0 or givenRow >= self.n:
            print("out of bounds")
            return

        rowSum = sum(self.matrix[givenRow])  #sum of a given row
        print(f"Sum of a row = ", rowSum)

    def avgOftheGivenCol(self, givenCol):
        if givenCol < 0 or givenCol >= self.m:
            print("out of bounds")
            return
        
        colSum = 0
        for i in range(0, self.m):
            colSum += self.matrix[i][givenCol] 
        avgSum = colSum / self.n
        print(f"Avg of a given col = ", avgSum)

    def submatrix(self, col1, col2, row1, row2):
        if row1 < 0 or row2 >= self.n or col1 < 0 or col2 >= self.m:
            print("out of bounds ")
            return
        for i in range(row1, row2 + 1):
            print(self.matrix[i][col1:col2 + 1])


matrix1 = Matrix(3,3)

matrix1.printMatrix()
matrix1.meanOfTheMatrix()
matrix1.sumOfTheGiveRow(2)
matrix1.avgOftheGivenCol(2)
matrix1.submatrix(1,2, 1,2)