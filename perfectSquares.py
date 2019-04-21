from collections import deque
from typing import List

class Solution:


    def numSquares(self, n: int) -> int:

        if n <= 0: return 0
        if n == 1: return 1
        #find possible max integer 
        possible = [] 
        counter = 0
        #put 1 ~ maxInt to a list 
        for i in range(1, n):
            squareNum = i*i
            if squareNum <= n:
                possible.append(squareNum)

        print(possible)
        
        # use tree shape to record the reuslt of n - all possible number
        # my goal is to find the shortest path to nodeVal = 0
        myQueue = deque()
        myQueue.append(n)
        step = 0 
        counter=1
        while myQueue: 

            cur = myQueue.popleft()  
            if counter == 0:
                step += 1
                counter = pow(len(possible), step)
            
            print("cur{} counter{}  step{} ",cur, counter,step)
            for i in range(len(possible)):
                
                nodeVal = cur - possible[i] 
                if nodeVal == 0: 
                    return step+1
                else: #need to kepp this value
                    myQueue.append(nodeVal) 
                
            counter -=1

        return 0


def main():
    print( "hello numSquares") 
    s = Solution()   
    print("min count: ", s.numSquares(12))
    print("min count: ", s.numSquares(13))
    print("min count: ", s.numSquares(7))
     
if __name__ == "__main__":
    main()