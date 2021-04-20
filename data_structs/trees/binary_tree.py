# recursive tree in MCS 275 notes

class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def show_tree(self):
    if self.left:
      self.left.show_tree()
    print(self.data)
    if self.right:
      self.right.show_tree()

  def insert(self, data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = Node(data)
        else:
          self.left.insert(data)
      elif data > self.data:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.insert(data)
    else:
      self.data = data


root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)
root.show_tree()
