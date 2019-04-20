from collections import deque
from typing import List

class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:

        #[ print(item) for item in grid]
        if len(grid) == 0: return 0

        # print(  [  3 in row for row in grid]   )
        
        visited = [ [False] * len(row) for row in grid]  
        # [ print(item) for item in visited]
        count = 0
        r_len = len(grid)
        c_len = len(grid[0])
        myQueue = deque()

        while not visited[r_len-1][c_len-1]:

            for i in range(r_len):
                for j in range(c_len):
                    
                    if not visited[i][j]:
                        
                        visited[i][j] = True
                        #check if current is an island
                        if grid[i][j] == 1:
                            myQueue.append({ 'i':i, 'j':j})
                            count += 1

                        while myQueue:
                            # print("myQueue {}".format(myQueue))
                            cur = myQueue.popleft()
                            # print("cur ", cur) 

                            #find four direction of cur
                            # up
                            tempI = cur['i']-1
                            tempJ = cur['j']
                            # print("{} {}".format(tempI, tempJ))
                            if tempI >= 0: 
                                if not visited[tempI][tempJ] and grid[tempI][tempJ] == 1: 
                                    myQueue.append({'i': tempI, 'j': tempJ})
                                
                                visited[tempI][tempJ] = True

                            #right
                            tempI = cur['i']
                            tempJ = cur['j']+1
                            # print("{} {}".format(tempI, tempJ))

                            if tempJ < c_len:
                                if not visited[tempI][tempJ] and grid[tempI][tempJ] == 1: 
                                    myQueue.append({'i': tempI, 'j': tempJ})
                                
                                visited[tempI][tempJ] = True

                            #down
                            tempI = cur['i']+1
                            tempJ = cur['j']
                            # print("{} {}".format(tempI, tempJ))

                            if tempI < r_len:
                                if not visited[tempI][tempJ] and grid[tempI][tempJ] == 1: 
                                    myQueue.append({'i': tempI, 'j': tempJ})
                                
                                visited[tempI][tempJ] = True

                            
                            #left
                            tempI = cur['i']
                            tempJ = cur['j']-1
                            # print("{} {}".format(tempI, tempJ))

                            if tempJ >= 0:
                                if not visited[tempI][tempJ] and grid[tempI][tempJ] == 1: 
                                    myQueue.append({'i': tempI, 'j': tempJ})
                                
                                visited[tempI][tempJ] = True
                            

 

        return count



def main():
    print( "hello numIslands") 
    s = Solution() 
    input = [[1,1,1,1,0] ,
            [1,1,0,1,0] ,
            [1,1,0,0,0] ,
            [0,0,0,0,0]]
 
    print("island count: ", s.numIslands(input))

    input = [[1,1,0,0,0] ,
            [1,1,0,0,0] ,
            [0,0,1,0,0] ,
            [0,0,0,1,1]]
 
    print("island count: ", s.numIslands(input))

if __name__ == "__main__":
    main()