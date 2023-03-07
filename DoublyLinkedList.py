class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
            self.tail = node
            return
            
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node
        return
    
    def print_forward(self):
        itr = self.head
        while itr:
            print(itr.data, end='-->')
            itr = itr.next
            
        print('None')
        return
    
    def print_backward(self):
        itr = self.tail
        while itr:
            print(itr.data, end='<--')
            itr = itr.prev
            
        print('None')
        return
    
    def insert_at_end(self, data):
        if self.tail == None:
            node = Node(data)
            self.tail = node
            self.head = node
            return
            
        node = Node(data)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        return
    
LL2 = DoublyLinkedList()
LL2.insert_at_begining('S')
LL2.insert_at_begining('A')
LL2.insert_at_begining('N')
LL2.insert_at_begining('J')
LL2.insert_at_begining('U')
LL2.insert_at_end('Y')
LL2.insert_at_end('A')
LL2.insert_at_end('D')
LL2.insert_at_end('A')
LL2.insert_at_end('V')
LL2.print_backward()
LL2.print_forward()