import numpy as np
import copy

class Problems:

    def __init__(self):
        pass

    def fib(self,n,memo={}):

        if n in memo.keys():
            return memo[n]
        
        if n == 1:
            memo[1] = 1
            return 1

        if n == 2:
            memo[2] = 1
            return 1

        memo[n] = Problems.fib(self,n-1,memo) + Problems.fib(self,n-2,memo) 
        return(memo[n])

    def grid_traveller(self,height,width,memo={}):
        
        if (height,width) in memo.keys():
            return memo[height,width]

        if height == 1 or width == 1 :
            return 1
        
        memo[height,width] = Problems.grid_traveller(self,height-1,width)+ Problems.grid_traveller(self,height,width-1)
        memo[width,height] = memo[height,width]

        return memo[height,width]

    def grid_traveller_matrix(self,height,width,grid=[]):
        grid = np.zeros([height,width])

        grid[1:height,0] = 1
        grid[0,1:width] = 1

        for i in range(1,height):
            for j in range(1,width):

                grid[i,j] = grid[i,j-1] + grid[i-1,j]

        return(grid[height-1,width-1])

    def cansum(self,target,numbers,memo={}):
        if target in memo:
                return memo[target]

        if target == 0:
            return True

        if target < 0:
            return False

        for number in numbers:

            subtarget = target - number

            if Problems.cansum(self,subtarget,numbers,memo):               
                memo[target] = True
                return True 

        memo[target]= False
        return False

    def howsum(self,target,numbers,memo={},subs=[]):
        if target in memo.keys():
            return memo[target]

        if target == 0:
            return []
        
        if target < 0:
            return None
        
        for number in numbers:

            subtarget = target - number
            list = Problems.howsum(self,subtarget,numbers,memo)

            if list != None:
                newlist = [i for i in list]
                newlist.append(number)

                memo[target] = newlist
                return memo[target]
        memo[target] = None
        return memo[target]

    def bestsum(self,target,numbers,memo={},subs=[]):
        if target in memo.keys():
            return memo[target]

        if target == 0:
            return []
        
        if target < 0:
            return None
        
        for number in numbers:

            subtarget = target - number
            list = Problems.bestsum(self,subtarget,numbers,memo)

            if list != None:
                newlist = [i for i in list]
                newlist.append(number)
                if target in memo.keys():
                    if len(memo[target]) >= len(newlist): 
                        memo[target] = newlist
                else:
                    memo[target] = newlist
        if target in memo.keys():
            return memo[target]
        else:
            memo[target] = None
            return memo[target]


    
    def cansum2(self,target,numbers):
        rest = []
        n = len(numbers)
        for number in numbers:
            rest.append(target // number)
        rest = np.array(rest)
        shape = 1
        for i in range(n):
            shape = shape * (rest[i]+1)
        Fshape = shape
        Q = np.zeros((shape,n))
        iterations =1
        for i in range (n):
            for k in range(iterations):
                for j in range(rest[i]+1):
                    a = int((j+k*(rest[i]+1))*shape/(rest[i]+1))
                    b = int((j+1+k*(rest[i]+1))*shape/(rest[i]+1))
                    Q[a:b,i] = j
            iterations = iterations * (rest[i]+1)
            shape = shape / (rest[i]+1)
        sum = np.matmul(Q,np.array(numbers)) 
        for  i in range(Fshape):
            if sum[i] == target:

                return True
        return False

        
    def howsum2(self,target,numbers):
        rest = []
        n = len(numbers)
        for number in numbers:
            rest.append(target // number)
        rest = np.array(rest)
        shape = 1
        for i in range(n):
            shape = shape * (rest[i]+1)
        Fshape = shape
        Q = np.zeros((shape,n))
        iterations =1
        for i in range (n):
            for k in range(iterations):
                for j in range(rest[i]+1):
                    a = int((j+k*(rest[i]+1))*shape/(rest[i]+1))
                    b = int((j+1+k*(rest[i]+1))*shape/(rest[i]+1))
                    Q[a:b,i] = j
            iterations = iterations * (rest[i]+1)
            shape = shape / (rest[i]+1)
        sum = np.matmul(Q,np.array(numbers)) 
        for  i in range(Fshape):
            if sum[i] == target:
                
                Q[i,:]
        return False

        