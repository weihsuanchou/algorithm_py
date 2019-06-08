
#left < right
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if nums is None or nums == []: return nums
        
         
        slow = 0 
        for fast in range(1, len(nums)): 
            print(fast)
            if nums[slow] != nums[fast]:
                slow += 1 
                nums[slow] = nums[fast] 
        
        return slow+1
        


def main():
    print( "hello") 
    s = Solution()  
 
    print("output: ", s.removeDuplicates( [0,0,1,1,1,2,2,3,3,4]))

if __name__ == "__main__":
    main()