#use mid and 2 pointers hight and lower as boundery
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if nums is None or nums == []: return 0  
        if target in nums:
            return nums.index(target)
        else:
            lw = 0
            ht = len(nums)
            while(lw < ht):
                # // will do ceilling
                mid = (lw+ht)//2

                if nums[mid] > target: ht = mid
                else: lw = mid + 1

            return lw

        # for i in range(len(nums)):
        #     if nums[i] == target or nums[i] > target: return i 
            

        # return len(nums)

        


def main():
    print( "hello") 
    s = Solution()  
 
    #print("output: ", s.searchInsert( [1,3,5,6], 2))
    print(4/2)
    print(4//2)
    print(5/2)
    print(5//2)

    print(5//2.63)
if __name__ == "__main__":
    main()