class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next

def main():
    LL = LinkedList()
    LL.head = node(1)
    second = node(2)
    third = node(3)
    LL.head.next = second
    second.next = third

    LL.printlist()
main()
