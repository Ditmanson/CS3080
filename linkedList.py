
class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
    # add to end

    def addToEnd(self, newdata):
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while (current.next):
            current = current.next
        current.next = newNode

    def addToHead(self, newdata):
        newNode = Node(newdata)
        if not self.head:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def removeByValue(self, value):
        if self.head is None:
            return
        
        elif self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current is not None and current.data != value:
            previous = current
            current = current.next
        if current.data == value:
            previous.next = current.next
            current = current.next

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


def main():
    myLinkedList = linkedList()
    
    myLinkedList.addToEnd(("heart"))
    myLinkedList.addToEnd(("diamond"))
    myLinkedList.addToEnd("club")
    myLinkedList.addToEnd("spade")
    myLinkedList.printList()
    myLinkedList.removeByValue(("spade"))
    myLinkedList.printList()


main()
