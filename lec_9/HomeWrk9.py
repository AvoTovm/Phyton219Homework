import random

class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = [[random.randint(1,30) for _ in range(m)] for _ in range(n)]

    def __str__(self):
        row_strings = ["| " + " ".join(f"{val:3}" for val in row) + " |" for row in self.matrix]
        return "\n".join(row_strings)
    
    def __add__(self, secondMatrix):
        if self.m != secondMatrix.m or self.n != secondMatrix.n:
            print("matrix are not the same size")
            return
        
        matrix3 = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                matrix3.matrix[i][j] = self.matrix[i][j] + secondMatrix.matrix[i][j]

        return matrix3
    
    def __sub__(self, secondMatrix):
        if self.m != secondMatrix.m or self.n != secondMatrix.n:
            print("matrix are not the same size")
            return
        
        matrix3 = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                matrix3.matrix[i][j] = self.matrix[i][j] - secondMatrix.matrix[i][j]

        return matrix3
    
    def __mul__(self, secondMatrix):
        if self.m != secondMatrix.m or self.n != secondMatrix.n:
            print("matrix are not the same size")
            return
        
        matrix3 = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                matrix3.matrix[i][j] = self.matrix[i][j] * secondMatrix.matrix[i][j]

        return matrix3

m1 = Matrix(3,3)
m2 = Matrix(3,3)

print("Matrix1")
print(m1)
print("\n")
print("Matrix2")
print(m2)
print("\n")

print("addition")
print(m1 + m2)
print("\n")

print("subtraction")
print(m1 - m2)
print("\n")

print("multiply")
print(m1 * m2)
print("\n")

