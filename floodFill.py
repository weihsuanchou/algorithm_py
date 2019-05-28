class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        curColor = image[sr][sc]
        
        print(curColor)
        stack = [[sr,sc]]
        
        print(stack)
        while stack:
            csr, csc = stack.pop()
            print (csr, csc)
            image[csr][csc] = newColor

            #check 4 direction 
            for a,b  in zip ((1,-1,0,0), (0,0,1, -1)): 

                x = csr+a
                y = csc+b
                if x >= 0 and y >= 0 and x < len(image) and y < len(image[0]):

                    if image[x][y] != newColor and image[x][y] == curColor:
                        stack.append([x, y])
            
            print("stack", stack)

        print(image)
        return image
        
        
