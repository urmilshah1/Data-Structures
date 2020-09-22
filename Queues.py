class Queue():
    
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        #This method takes in an item and inserts it to the front of the list that is representing the queue.
        #The run time is O(n) because inserting into the 0Th index of a list forces all other items to move one index to the right.
        self.items.insert(0, item)
    
    def dequeue(self):
        #This method returns and removes the front most item of the queue which is represented by the last time of the list.
        #The run time is O(1). Because indexing to the end of the list happens in constant time. 
        if self.items:
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        #Returns the last item in the list, which represents the front most item in the queue
        #The run time is O(1) because we're just indexing to the last item of the list and returning the value found there. 
        if self.items:
            return self.items[-1]
        else:
            return None
    def size(self):
        #Returns the size of the queue, which is represented by the length of the queue
        #The run time of this method is O(1), or constant time, because we are only returning the length
        return len(self.items)
    
    def isempty(self):
        #The method returns true or false on whether the queue represented by the list is empty or not
        #The k
        run time of this method is O(1) because its a comparator operator. 
        return self.items == []
    
    

    
    
myqueue = Queue()
myqueue.enqueue('apple')
print(myqueue.items)
myqueue.enqueue('banana')
print(myqueue.items)
myqueue.dequeue()
print(myqueue.peek())
print(myqueue.items)
