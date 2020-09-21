class Stack:
      
    def __init__(self):
        self.items = []
    
    def push(self, item):
        #This method accepts an item and appends it to the end of the list and returns nothing
        #The run time for this methiod is O(1). Because appending to the end of the list happens in constant time
        
        self.items.append(item)     

    def pop(self):
        #Removes and returns the last titem of the list which is the top item for stack
        #The runtime here is constant time because all it does is index to the last item of the list.
        if self.items:
            return self.items.pop()
        else:
            return None
    
    def peek(self):
        #Returns the last items the last items in the list, which is also the top of the stack
        #The run time in the case is constant because the indexing is done in constant time
        if self.items:
            return self.items[-1]
        else:
            return None
    
    def size(self):
        #Returns the length of the list that is representing the stack.
        #This method runs in constant time because finding the length of the list happens in constant time
        
        return len(self.items)
    
    def isempty(self):
        #returns the boolean value whether or not the stack is empty
        #The testing for equality hapooens in constant time. 
        
        return self.items == []

    
    
mystack = Stack()
mystack.push('apple')
mystack.push('banana')
print(mystack.items)
mystack.push('orange')
mystack.push('peach')
mystack.pop()
print(mystack.items)
print(mystack.size())
print(mystack.isempty())
    