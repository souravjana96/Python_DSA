class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Traverse the linked list and print the elements
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

    # 2. Search for a node with a specific value
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return f"Node with data {data} found at position {position}"
            current = current.next
            position += 1
        return f"Node with data {data} not found"

    # 3. Get the length of the linked list
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # 4. Insert a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 5. Insert a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 6. Insert a node at a specific position
    def insert_at_position(self, position, data):
        if position < 0 or position > self.get_length():
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

    # 7. Delete a node from the beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # 8. Delete a node from the end
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

    # 9. Delete a node at a specific position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position < 0 or position >= self.get_length():
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

# Main function to test the LinkedList class
if __name__ == "__main__":
    ll = LinkedList()
    
    # Insert nodes at the end
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_at_position(2, 15)

    # Traverse the list
    print("Traversal:")
    ll.traverse()  # Output: 5 -> 10 -> 15 -> 20

    # Search for a node
    print("\nSearch for 15:")
    print(ll.search(15))  # Output: Node with data 15 found at position 2

    # Get the length of the list
    print("\nLength of the list:")
    print(ll.get_length())  # Output: 4

    # Delete operations
    print("\nDeleting node at position 0 (head):")
    ll.delete_at_position(0)
    ll.traverse()  # Output: 10 -> 15 -> 20

    print("\nDeleting node at position 2 (end):")
    ll.delete_at_position(2)
    ll.traverse()  # Output: 10 -> 15

    print("\nDeleting node at position 1 (middle):")
    ll.delete_at_position(1)
    ll.traverse()  # Output: 10
