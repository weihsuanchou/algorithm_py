
#use dictionary to keep number and index
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if nums is None or nums == []: return nums
        d = {}
        
        
        for i in range(len(nums)):
            print(i)
            if target - nums[i] in d:
                return [ d.get(target - nums[i])  , i]
            else:
                #not found, so just keep it in set for future use
                d[nums[i]] = i 


def main():
    print( "hello two sum") 
    s = Solution()  
 
    print("output: ", s.twoSum([3,2,4], 6))

if __name__ == "__main__":
    main()