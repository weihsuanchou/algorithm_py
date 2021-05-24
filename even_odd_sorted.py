
def moves(arr):
    swap_cnt = 0
    # Initialize left and right indexes
    left,right = 0,len(arr)-1
 
    while left < right:
 
        # add left index while we see 0 at left
        while (arr[left]%2==0 and left < right):
            left += 1
 				#left=2, right=6
        # minus right index while we see 1 at right
        while (arr[right]%2 == 1 and left < right):
            right -= 1
 				
 				#left=2, right=5
        if (left < right):
              # Swap arr[left] and arr[right]*/
              arr[left],arr[right] = arr[right],arr[left] 34, 3
              left += 1
              right = right-1
              swap_cnt+=1
 
    return swap_cnt

