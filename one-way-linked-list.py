# from matplotlib.pyplot import cla


# class Node:
#     def __init__(self) -> None:
#         self.data = None
#         self.next = None

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None
#         self.size = 0
    
#     def insert(self, data) -> None:
#         new_node = Node()
#         new_node.data = data
#         new_node.next = None
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.size += 1
    
#     def delete(self, data) -> None:
#         current = self.head
#         previous = None
#         while current is not None:
#             if current.data == data:
#                 if previous is None:
#                     self.head = current.next
#                 else:
#                     previous.next = current.next
#                 self.size -= 1
#                 return
#             previous = current
#             current = current.next

#     def print_list(self) -> None:
#         current = self.head
#         while current is not None:
#             print(current.data)
#             current = current.next
    
#     def get_size(self) -> int:
#         return self.size

#     def get_head(self) -> Node:
#         return self.head

#     def get_tail(self) -> Node:
#         return self.tail

#     def get_node(self, index) -> Node:
#         current = self.head
#         for i in range(index):
#             current = current.next
#         return current
    
#     def get_data(self, index) -> int:
#         return self.get_node(index).data

#     def get_index(self, data) -> int:
#         current = self.head
#         for i in range(self.size):
#             if current.data == data:
#                 return i
#             current = current.next
#         return -1
    
#     def get_next(self, index) -> Node:
#         return self.get_node(index).next

#     def get_previous(self, index) -> Node:
#         current = self.head
#         for i in range(index):
#             current = current.next
#         return current
    
#     def get_next_data(self, index) -> int:
#         return self.get_next(index).data
    
#     def get_previous_data(self, index) -> int:
#         return self.get_previous(index).data
    
#     def get_middle(self) -> int:
#         if self.size % 2 == 0:
#             return self.get_data(self.size // 2)
#         else:
#             return self.get_data(self.size // 2 + 1)
    
#     def get_middle_index(self) -> int:
#         if self.size % 2 == 0:
#             return self.get_index(self.get_middle())
#         else:
#             return self.get_index(self.get_middle())
    
#     def get_middle_next(self) -> int:
#         return self.get_next(self.get_middle_index())
    
#     def get_middle_previous(self) -> int:
#         return self.get_previous(self.get_middle_index())

#     def get_middle_next_data(self) -> int:
#         return self.get_next_data(self.get_middle_index())
    
#     def get_middle_previous_data(self) -> int:
#         return self.get_previous_data(self.get_middle_index())

#     def get_middle_next_index(self) -> int:
#         return self.get_index(self.get_middle_next())

#     def get_middle_previous_index(self) -> int:
#         return self.get_index(self.get_middle_previous())

class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    #connect the nodes
    ll.head.next = second
    second.next = third

    #print the linked list
    while ll.head is not None:
        print(ll.head.item)
        print(ll.head.next)
        ll.head = ll.head.next


