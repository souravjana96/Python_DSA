class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Traverse linked list and print the elements
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next

        result_str = ""
        for i, data in enumerate(result):
            if i == len(result) - 1:
                result_str += str(data)
            else:
                result_str += str(data) + " -> "
    
        print(result_str)


    # Insert a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert a node at a specific position
    def insert_at_position(self, position, data):
        if position < 0 :
            print("Invalid position")
            return
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        
        count = position - 1
        while count > 0:
            current = current.next
            count -= 1
            
        new_node.next = current.next
        current.next = new_node


    # Delete a node from the beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # Delete a node from the end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    # Delete a node at a specific position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position < 0 :
            print("Invalid position")
            return
        current = self.head

        
        if position == 0:
            self.head = current.next
            return

        # Find the previous node 
        count = position - 1  
        while count > 0:
            current = current.next
            count -= 1

        
        current.next = current.next.next

if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    # ll.traverse()

    ll.insert_at_beginning(5)
    # ll.traverse()

    ll.insert_at_position(2, 15)
    ll.traverse()

    ll.delete_at_position(2)
    ll.traverse()

    ll.delete_from_beginning()
    ll.traverse()

    ll.delete_from_end()
    ll.traverse()

    
    