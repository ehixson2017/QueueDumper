
#create the queue

class Node:
    def __init__(self, value):
        self.next = None
        self.last = None
        self.value = value

    def getValue(self):
        return self.value


#first in, first out
class Queue:
    def __init__(self, topNode = None):
        self.topNode = topNode
    
    #add element to bottom of list and shift everything up one
    def enqueue(self, newNode):
        #go to top node in queue, move everything below that node up, place newNode at bottom
        if self.topNode.last == None:
            newNode.next = self.topNode
            self.topNode.last = newNode
        elif self.topNode.last != None:
            newNode.next = self.getBot(self.topNode)
            newNode.next.last = newNode
            
    def dequeue(self, node=None):
        if node == None:
            self.dequeue(self.topNode)
        elif node.next == None:
            self.pop()
        elif node.last == None:
            self.getBot(node).next.last = None
        else:
            node.last.next = node.next
            node.next.last = node.last
        

    def pop(self):
        self.topNode = self.topNode.last
        if self.topNode.next:
            self.topNode.next = None
        else: pass
        

    #gets bottom most node (last out)
    def getBot(self, node=None):
        if node.last == None:
            return node
        else:
            return self.getBot(node.last)

    #gets top most node (first out)
    def getTop(self, node=None):
        if node.next == None:
            return node
        else:
            return self.getTop(node.next)

    def getNext(self, node=None):
        if node.next == None:
            return None
        else:
            return node.next

    #print the queue in order from top to bottom
    def print_queue(self, node=None):
        item = node
        if item == None:
            self.print_queue(self.topNode)
        else:
            if item.last != None:
                self.print_queue(item.last)
            val = node.getValue()
            print("NODE VALUE: " + str(val))
            
        

        


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
test_queue = Queue(node0)
test_queue.enqueue(node1)  
test_queue.enqueue(node2)
test_queue.enqueue(node3)  
test_queue.enqueue(node4)  

#test_queue.print_queue(node4)

node5 = Node(5)
test_queue.enqueue(node5)
test_queue.dequeue()
test_queue.print_queue()
test_queue.dequeue()
test_queue.print_queue()
test_queue.dequeue()
test_queue.print_queue()
test_queue.dequeue()
test_queue.print_queue()
test_queue.dequeue()
test_queue.print_queue()

