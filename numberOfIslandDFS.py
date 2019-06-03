# def dfs(Node cur, Node target, Set<Node> visited):
#     return True if cur is target
#     for i in cur.neighbor:
#         if i not in visited:
#             visited.append(i)
#             return True if dfs(i, target, visited) == True
#     return False

 

def countIsland(grid):
    if grid is None or grid == []: return 0
    def checkIsland(i, j):
        if (0 <= i < len(grid)) and (0 <= j < len(grid[0])) and grid[i][j] == 1:
            grid[i][j] = 0
            #just want to use this to turn 1 to 0
            #use list to make map object works
            list(map(checkIsland, (i+1, i-1, i, i), (j, j, j+1, j-1)))
            # for i, j in zip((i, i+1, i, i-1), (j+1, j, j-1, j)): 
            #     checkIsland(i, j)
            return 1
       
        return 0
    
    return sum( checkIsland(i, j) for i in range(len(grid)) for j in range(len(grid[0])) )

def main():
    print( "hello Doctor! Loop 2 vairables")

    #[print(x, y) for x in range(3) for y in range(5)]
    
    def myFunc(a, b):
        return len(a) + len(b)
    
    #for a,b in zip((0, 1, 0, -1), (1, 0, -1, 0)): print (a, b)
    # print(sum(map( myFunc, ("rrr", "ggg"), ("f", "ooooo"))))
    
    input = [[1,1,1,1,0] ,
             [1,1,0,1,0] ,
             [1,1,0,0,0] ,
             [0,0,0,0,0]]
 
    print("island count: ", countIsland(input))


if __name__ == "__main__":
    main()