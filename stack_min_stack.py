class MinStack:


    def __init__(self):
        """
        initialize your data structure here.
        """ 
        self.stack = []
        self.min_stack = []
        
        

    def push(self, x: int) -> None:

        if (self.getMin() is None) or (x <= self.getMin()):
            self.min_stack.append(x)

        self.stack.append(x)

    def pop(self) -> None: 
        # handle both stacks
         if self.top() is not None:

             stack_top = self.stack.pop()
             if self.getMin() == stack_top:
                 self.min_stack.pop()



    def top(self) -> int:
        return None if self.stack == [] else self.stack[-1]
    

    def getMin(self) -> int:
        return None if self.min_stack == [] else self.min_stack[-1]


def peek(list):
    return None if list == [] else list[-1]

def main():
    print( "hello Doctor!")
    minStack = MinStack()
    minStack.push(-1)
    
    print(minStack.top()) 
    
    print(minStack.getMin()) 


if __name__ == "__main__":
    main()