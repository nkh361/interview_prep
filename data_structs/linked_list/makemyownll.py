class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class CircularLinkedList:
  def __init__(self):
    self.head = None

  def insert(self, data):
    newNode = Node(data)
    tmp = self.head
    newNode.next = self.head

    if self.head != None:
      while tmp.next != self.head:
        tmp = tmp.next
      tmp.next = newNode
    else:
      newNode.next = newNode
    self.head = newNode

  def printLL(self):
    current = self.head
    count = 0
    if self.head != None:
      while(True):
        print("index: {}".format(count))
        print("data: {}".format(current.data))
        current = current.next
        count += 1
        if current == self.head:
          break # to avoid infinite loop

cll = CircularLinkedList()

cll.insert(4)
cll.insert(10)
cll.insert(15)

cll.printLL()
