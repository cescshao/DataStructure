class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        str1 = ""
        temp = self.head
        while temp:
            str1 += str(temp.data)
            str1 += "->"
            temp = temp.next
        str1 += "None"
        print(str1)

    def insertHead(self, Node):
        if self.head == None:
            self.head = Node
        else:
            Node.next = self.head
            self.head = Node

    def insertEnd(self, Node):
        if self.head == None:
            self.head = Node
        else:
            temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def printNode(self):
        print(str(self.data))
        

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
list1 = LinkedList()
list1.head = node1
node1.next = node2
list1.insertHead(node3)
list1.insertEnd(node4)
list1.printList()