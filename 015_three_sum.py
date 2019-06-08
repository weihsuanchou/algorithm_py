
#left < right
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if nums is None or nums == []: return nums
        
        nums.sort() 
        result = []
        i = 0
        while(i < len(nums)-1): 
            if(i > 0 and nums[i] == nums[i-1]):
                i += 1
                continue

            cur = nums[i]
            left = i+1
            right = len(nums)-1 
             
            while(left < right): 
                target = cur+ (nums[left] + nums[right]) 
                #find out if the following number can make a triplet
                if target == 0 :
                    result.append([ cur, nums[left], nums[right] ])
                    left += 1
                    right -= 1
                    while left< right and nums[left] == nums[left-1]:
                        left += 1
                    while left< right and nums[right] == nums[right+1]:
                        right -= 1


                elif target > 0: 
                    right -= 1
                else:
                    left += 1

            i += 1
        return result
        


def main():
    print( "hello") 
    s = Solution()  
 
    print("output: ", s.threeSum( [-1, 0, 1, 2, -1, -4]))

if __name__ == "__main__":
    main()