"""
Usually, a Python dictionary throws a KeyError
if you try to get an item with a key that is not
 currently in the dictionary. 
 The defaultdict in contrast will simply create 
 any items that you try to access (provided of course they do not exist yet). 
 To create such a "default" item, it calls the function object 
 that you pass to the constructor 
 (more precisely, it's an arbitrary "callable" object, which includes function and type objects). 
 For the first example, default items are created using int(), 
 which will return the integer object 0

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

d.items()

output
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

"""
from collections import defaultdict
from typing import List

#solution: Use a dictionary to store all possible sums (from all numbers with + or -)
#and ++ the sum as the way to get to each sum

class solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dict = defaultdict(int)

        #dummy
        dict[0] = 1
        
        for i in nums:
            sum = defaultdict(int)
            for key in dict:
                sum[key + i] +=  dict[key] 
                sum[key - i] +=  dict[key]  
            dict = sum

        return dict[S]


    def findTargetSumWays2(self, nums: List[int], S: int) -> int: 
        # integers are immutable
        #Everything in Python is an object.
        # Objects of built-in types like (int, float, bool, str, tuple, unicode) are immutable
        count = [0]

        def helper(nums, target, index, count):
            #recursion until the index execess len(nums)
            if index == len(nums):
                
                if target == 0:
                    print(target, index, count)
                    count[0] += 1 
                return 0

            helper(nums, target-nums[index] , index+1, count) 
            helper(nums, target+nums[index] , index+1, count)
              
        helper(nums, S, 0, count)
        print("count ", count[0])
        return count[0]
        
    
def main():
    print( "hello Doctor! Target Sum")
    dict = defaultdict(int)
    dict[0] = 1
    dict[2] = 3
    # for j in dict: 
    #     print('key,val: ', j,  dict[j])  
    
    # newDic = defaultdict(int)
    # newDic[5] = 1
    # dict =newDic

    # print(dict)
    # for j in dict: 
    #     print('val', dict[j]) 
    print(solution().findTargetSumWays2([1, 1, 1, 1, 1], 3))


if __name__ == "__main__":
    main()