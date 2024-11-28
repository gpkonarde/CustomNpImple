import numpy as np
class CustomMatrix:
    def __init__(self,X,Y) :
        self.X = X
        self.Y = Y
    def dot(self):
        new_arr = []
        if(type(self.X) != list or type(self.Y) != list):
            for i in range(len(self.X)):
                row = []
                for j in range(len(self.X[i])):
                    row.append(self.X[i][j] * self.Y)
                new_arr.append(row)
            return new_arr
        else:
            if len(self.Y) == len(self.X[0]):  
                for i in range(len(self.X)):  
                    row = []  
                    for j in range(len(self.Y[0])):  
                        res = 0  
                        for k in range(len(self.Y)):  
                            print(f"X[{i}][{k}] * Y[{k}][{j}] -> {self.X[i][k]} * {self.Y[k][j]}")
                            res += self.X[i][k] * self.Y[k][j]
                        row.append(res)  
                    new_arr.append(row)
            else : 
                print("Value of columns and rows doesnt match")
        return new_arr

    def reshape(self ,arr , shape):
        rows = shape[0]
        col = shape[1]
        new_arr = []
        flat_arr = [item for sublist in arr for item in sublist] if isinstance(arr[0], list) else arr

        if rows == -1:
            rows = len(flat_arr) // col
        elif col == -1:
            col = len(flat_arr) // rows
        if len(flat_arr) != rows * col:
            print("Reshaping cannot be done")
            return None
        for i in range(rows):
            row = []
            for j in range(col):
                idx = i * col + j
                print(f"idx{idx}")
                row.append(flat_arr[idx])
            print(row)
            new_arr.append(row)
        return new_arr


X = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
Y = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
# Y = 2
obj = CustomMatrix(X,Y)
list = obj.reshape(X,shape=(-1,1))
