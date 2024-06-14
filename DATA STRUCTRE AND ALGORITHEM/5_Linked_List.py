class Node:
    def __init__(self, data):
        self.data = data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("Lined List is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.ref
    def add_begning(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        n=self.head
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        while n.ref is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def insert_empty_LL(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("LL is not empty")
    def remove_start(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head=self.head.ref
    def remove_end(self):
        if self.head is None:
            print("LL is empty")
        elif self.head.ref is None:
            self.head=None    
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def remove_By_Value(self,x):
        if self.head is None:
            print("LL is Empty")
            return
        elif self.head.data==x:
            self.head=self.head.ref
            return
        else:
            n=self.head
            while n.ref is not None:
                if x==n.ref.data:
                    break
                n=n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            n.ref=n.ref.ref
                
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_empty_LL(10) # Insert into empty list
    ll.print_ll() # Output: 10 --> None

    ll.add_begning(5)  # Add at beginning
    ll.print_ll() # Output: 5 --> 10 --> None

    ll.add_end(15)  # Add at end
    ll.print_ll() # Output: 5 --> 10 --> 15 --> None

    ll.add_after(12, 10)  # Add after 10
    ll.print_ll() # Output: 5 --> 10 --> 12 --> 15 --> None

    ll.add_before(8, 10)  # Add before 10
    ll.print_ll() # Output: 5 --> 8 --> 10 --> 12 --> 15 --> None

    ll.remove_start()  # Remove from start
    ll.print_ll() # Output: 8 --> 10 --> 12 --> 15 --> None

    ll.remove_end()  # Remove from end
    ll.print_ll() # Output: 8 --> 10 --> 12 --> None

    ll.remove_By_Value(10)  # Remove node with value 10
    ll.print_ll() # Output: 8 --> 12 --> None        
        
                        
            