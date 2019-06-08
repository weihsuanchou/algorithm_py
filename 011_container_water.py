#use mid and 2 pointers hight and lower as boundery
from typing import List
class Solution:
     def maxArea(self, nums: List[int]) -> int:
        
        if nums is None or nums == []: return 0  

        l = 0
        r = len(nums)-1
        max_area = 0
        
        while l < r:
            #max_area = max( min(nums[l], nums[r]) * (r - l) , max_area) 
            #reduce the usage of max, will increase speed
            cur = min(nums[l], nums[r]) * (r - l) 
            if(cur > max_area):
                max_area = cur 

            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        return max_area
        # for i in range(len(nums)): 
        #     print("i:", i)
        #     max_area = max(inner_max(i), max_area)
        #     print("max_area:", max_area)
            
        
        
        # return max_area

        


def main():
    print( "hello") 
    s = Solution()  
 
    print("output: ", s.maxArea([1,8,6,2,5,4,8,3,7])) 
    print("output: ", s.maxArea([2,1])) 
    print("output: ", s.maxArea([1,2])) 
   # print(max([1,1]))
if __name__ == "__main__":
    main()