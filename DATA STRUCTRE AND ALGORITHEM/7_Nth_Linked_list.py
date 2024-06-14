class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref
            print("None")

    def add_beginning(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def find_nth_from_end(self, n):
        nh = self.head
        length = 0
        while nh is not None:
            length += 1
            nh = nh.ref

        if n > length or self.head is None:
            print("No node found")
            return

        nh = self.head
        for _ in range(length - n):
            nh = nh.ref
        print(nh.data)
        
        
    def remove_start(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.ref

    def remove_end(self):
        if self.head is None:
            print("LL is empty")
        elif self.head.ref is None:
            self.head = None    
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def remove_By_Value(self, x):
        if self.head is None:
            print("LL is Empty")
            return
        elif self.head.data == x:
            self.head = self.head.ref
            return
        else:
            n = self.head
            while n.ref is not None:
                if x == n.ref.data:
                    break
                n = n.ref
        if n.ref is None:
            print("Node is not present in LL")
        else:
            n.ref = n.ref.ref

    def insert_empty_LL(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LL is not empty")

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

def menu():
    ll = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Add element at the beginning")
        print("2. Add element at the end")
        print("3. Print linked list")
        print("4. Find Nth element from end")
        print("5. Remove node by value")
        print("6. Insert into empty list")
        print("7. Add element after a specific value")
        print("8. Add element before a specific value")
        print("9. Remove element from the start")
        print("10. Remove element from the end")
        print("11. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter the element to add at the beginning: "))
            ll.add_beginning(data)
        elif choice == 2:
            data = int(input("Enter the element to add at the end: "))
            ll.add_end(data)
        elif choice == 3:
            ll.print_ll()
        elif choice == 4:
            n = int(input("Enter the position from the end: "))
            ll.find_nth_from_end(n)
        elif choice == 5:
            x = int(input("Enter the value to remove: "))
            ll.remove_By_Value(x)
        elif choice == 6:
            data = int(input("Enter the element to insert into empty list: "))
            ll.insert_empty_LL(data)
        elif choice == 7:
            data = int(input("Enter the element to add: "))
            x = int(input("Enter the value after which to add: "))
            ll.add_after(data, x)
        elif choice == 8:
            data = int(input("Enter the element to add: "))
            x = int(input("Enter the value before which to add: "))
            ll.add_before(data, x)
        elif choice == 9:
            ll.remove_start()
        elif choice == 10:
            ll.remove_end()
        elif choice == 11:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
