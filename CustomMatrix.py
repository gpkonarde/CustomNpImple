class CustomMatrix:
    def __init__(self,X,Y) :
        self.X = X
        self.Y = Y
    def display(self):
        print(X)
        print(Y)
    
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
            for i in range(len(self.X)):
                row =[]  
                for j in range(len(self.Y[0])): 
                    res = 0
                    for k in range(len(self.Y)):
                        res += X[i][k] * Y[k][j] 
                    row.append(res)
                new_arr.append(row)
            return new_arr

X = [[1,2],[3,4]]
Y = [[5,6],[7,8]]
# Y = 2
obj = CustomMatrix(X,Y)
list = obj.dot()
print(list)