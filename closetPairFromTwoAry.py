class Solution:


    def colestPair(self, x , ary1, ary2):
        if ary1 == [] or ary2 == []: return None

        minDis = None
        result_i = None
        result_j = None

        for i, val_i in enumerate(ary1):
          for j, val_j in enumerate(ary2):
             cur = abs(int(x) - (val_i+ val_j))
            
             print('val_i {} val_j {} min {} cur {}'.format(val_i, val_j, minDis, cur))    
             minDis = min(minDis, cur) if minDis is not None else cur
             if cur <= minDis: 
                result_i = val_i 
                result_j = val_j

        return print('{} and {} '.format(result_i, result_j))
def main():
    print( "hello numIslands") 
    s = Solution() 
    ar1 = [1,4,5,7] 
    ar2 = [10,20,30,40]
    
    s.colestPair(32, ar1, ar2)
 

if __name__ == "__main__":
    main()