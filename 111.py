class Node:
 def __init__(self, data=None, index=None, next_node=None):
    self.data = data
    self.index = index
    self.next_node = next_node
class LinkedList:
 def __init__(self, array=None):
    self.length = 0
    self.root = None
    #for element in array:
       #self.add_back(element)
       
 def add_back(self, value):
    if self.root is None:
       self.root=Node(value,None)
    last_node = self.root
    while last_node.next_node is not None:
       last_node = last_node.next_node
       self.length+=1
       self.update_indexes()
    last_node.next_node=Node(value,None)   
       
    #last_node.next_node = Node(element, None)
 def update_indexes(self):
    if self.root is  not None:
       last_node=self.root
       idx=0
       last_node.index=0
       while last_node.next_node is not None:
          last_node = last_node.next_node
          idx+=1
          last_node.index=idx
       self.length=idx    
    
 def delete_back(self):
    if self.root is  not None:
       last_node = self.root
       if last_node.next_node is None:
          self.root=None
       else:   
          prev = last_node
          while last_node.next_node is not None:
             prev = last_node
             last_node = last_node.next_node
          prev.next_node = None
          self.update_indexes()
          self.length-=1
 
 def get_item(self,index):
     x_node = self.root
     while x_node.next_node is not None:
      if x_node.index == index:
         x_node = x_node.next_node
         if x_node.next_node==None:
           return 'IndexError'
      return x_node.data

linked_list = LinkedList()
linked_list.add_back(8)
linked_list.add_back(17)
linked_list.add_back(2)
print(linked_list.get_item(2))   
    
# метод print_list(self) необходимо
