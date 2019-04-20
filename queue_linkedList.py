from collections import deque

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

def main():
    print( "hello Doctor!") 
    llist = SLinkedList()
    llist.head = Node('A')
    list = []
    q = deque(list,5) 

if __name__ == "__main__":
    main()