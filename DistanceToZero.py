from collections import deque

def distanceToZero(grid):
    sources = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]
    vis = set(sources) 
    q = deque([source+(0,) for source in sources])
    print(q)
    while(q):
        i,j,d = q.popleft()
        grid[i][j] = d
        for v in [(i+1,j),  (i-1,j), (i,j-1),(i,j+1)]:
            #print(v)
            #v[0] is x , v[1] is y
            if 0 <=v[0] < len(grid) and 0 <= v[1] < len(grid[0])  and v not in vis:
                vis.add(v)
                q.append(v + (d + 1,)) 
                    
    return grid

def main(): 
    input =[[1,1,1],
            [0,1,0],
            [0,0,0] 
            ]
    print(distanceToZero(input))

if __name__ == '__main__':
    main()