class Deque:
    def __init__(self):
        self.items = []
        
    def add_front(self, item):
        self.items.insert(0, item)
    
    def add_rear(self, item):
        self.items.append(item)
        
    def remove_front(self):
        return self.items.pop(0)
    
    def remove_rear(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
    
    
    
    
def check_palin(inputstr):
    
    my_q = Deque()
    for char in inputstr:
        my_q.add_rear(char)
            
    while my_q.size() >= 2:
        front_item = my_q.remove_front()
        rear_item = my_q.remove_rear()
            
        if front_item != rear_item:
            return False
    return True
    
print(check_palin('racecar'))
print(check_palin('oranges'))