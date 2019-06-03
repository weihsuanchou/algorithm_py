class Solution:
    def dailyTemperatures(self, list): 
      # try 1
      result = [0] * len(list)
      stack = []
      for i in range(len(list)): 
    
        while len(stack) > 0 and list[stack[-1]] < list[i]: 
          # it is an index 
          cur = stack.pop() # = stack[-1]
          result[cur] = i-cur # i will always greater than cur because cur is from previous i
            
        #only store the number has not found another greater than it
        stack.append(i) 

      return result