
#i manually increase
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if nums is None or nums == []: return 0 
        i = 0
        for j in range(len(nums)):

            if nums[j] != val: 
                #bring all follwing number one index forward 
                nums[i] = nums[j]
                i += 1
        
        return i
        


def main():
    print( "hello") 
    s = Solution()  
 
    print("output: ", s.removeElement( [0,1,2,2,3,0,4,2], 2))

if __name__ == "__main__":
    main()