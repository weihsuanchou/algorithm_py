from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadSet = set(deadends)
        myQueue = deque([('0000', 0)]) #passcode and step
        visited = set('0000')

        while myQueue:

            #think about one combination you can get with one move?
            (passcode, steps) = myQueue.popleft()

            if passcode == target: return steps
            elif passcode in deadSet: continue
            
            # try 4 digit and up/ down once
            for i in range(4): 
                lookat = int(passcode[i])
                for j in [1,-1]: 
                    newDigit = (lookat + j) % 10
                    newPasscode = passcode[:i] + str(newDigit) + passcode[i+1:]
                
                    if newPasscode not in visited:
                        visited.add(newPasscode)
                        myQueue.append((newPasscode, steps+1))

        return -1

def main():

    print( "hello openLock") 
    s = Solution() 
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
 
    print("island count: ", s.openLock(deadends, target))

if __name__ == "__main__":
    main()