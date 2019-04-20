from collections import deque

'''
collections.deque is a great default choice if you’re looking for a queue data structure in Python’s standard library.
'''

class cQueue(object):

    list = []
    size = 0
    head = -1
    tail = -1

    def __init__(self, k):
        print(" in init ") 
        self.size = k

    def isEmpty(self):
        return self.head == -1
    
    def isFull(self):
        return ((self.tail+1) % self.size) == self.head

    def peek(self):
        if(self.isEmpty()): return -1

        return self.list[self.head]

    def enQueue(self, a):
        if(self.isFull()): return False

        if(self.isEmpty()): self.head = 0

        self.tail = (self.tail + 1) % self.size

        if (len(self.list) > self.tail ):
            print('already space')
            self.list[self.tail] = a
        else:
            print('new space')
            self.list.append(a)

        return True

    def deQueue(self):
        
        if(self.isEmpty()): return False
        
        if(self.head == self.tail):
            self.head = -1
            self.tail = -1
            return True
        
        self.head = (self.head + 1 ) % self.size

        return True
    

def main():
    print( "hello Doctor!")
    #myqueue = cQueue(5)
    list = [5,6,7]
    q = deque(list,5)

    q.append(1)
    print(q[0])
    q.append(2)
    print(q[0])
    q.popleft()
    q.popleft()
    q.popleft()
    print('size: ', len(q))
    q.popleft() 
    
    print('len: ', q.maxlen )
    if q:
        print('has value ', q[0])
    else:
        print('Queue is empty')

     


if __name__ == "__main__":
    main()