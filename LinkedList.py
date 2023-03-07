class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, None)
        node.next = self.head
        self.head = node

    def show(self):
        itr = self.head
        result = ''
        while itr:
            result += str(itr.data) + '-->'
            itr = itr.next
        print(result + 'None')

    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head == None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def insert_values(self, list):
        for i in list:
            self.insert_at_end(i)

    def len(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count +=1
        return count

    def inser_at(self, data, index):
        if index > self.len():
            print('index value is more than the length of the list')
            return
        count = 0
        itr = self.head
        node = Node(data, None)
        if index==0:
            node.next = itr
            self.head = node
            return
        while count< index-1:
            count+=1
            itr = itr.next
        node.next = itr.next
        itr.next = node

    def remove(self, index):
        if index > self.len():
            print('index value is more than the length of the list')
            return
        count = 0
        itr = self.head
        while count<index-1:
            count+=1
            itr = itr.next
        itr.next = itr.next.next

l = Linkedlist()
l.insert_at_begining(5)
l.insert_at_begining(10)
l.insert_at_begining(15)
l.insert_at_begining(25)
l.insert_at_end(105)
l.insert_at_end(110)
l.show()

l2=Linkedlist()
l2.insert_at_end('A')
l2.insert_at_end('B')
l2.insert_at_end('C')
l2.insert_at_end(1)
l2.insert_at_end(2)
l2.show()

l2.insert_values(['sanju', 'yadav', 1991])
print(l2.len())
l2.show()
l2.inser_at('Kumar',6)
l2.show()
l2.remove(6)
l2.show()