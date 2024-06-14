class Node:
    def __init__(self, data):
        self.data = data
        self.nref=None
        self.pref=None
class Doubley_Linked_List:
    def __init__(self):
        self.head=None  
    def print_Forwared(self):
        if self.head is None:
            print("Doubley LL is Empty")
        else:   
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.nref
    def print_BackWard(self):
        if self.head is None:
            print("LL is Empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end="")
                n=n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("LL is not empty")
    def insert_begining(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            new_node=Node(data)
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node 
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref = new_node
            new_node.pref=n
    def insert_after(self,data,x):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("Node is not present")
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
                
    def insert_before(self,data,x):
        if self.head is None:
            print("LL is Empty")
            return
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
                if n is None:
                    print("Node is not present")
                else:
                    new_node=Node(data)
                    new_node.nref=n
                    new_node.pref=n.nref
                    if n.pref is not None:
                        n.pref.nref=new_node
                    n.perf=new_node    
    def remove_start(self):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.nref is None:
            self.head=None
            print("LL is Empty")
        else:
            self.head=self.head.nref
            self.head.pref=None
    def remove_end(self):
        if self.head is None:
            print("LL is empty")
            return
        elif self.head.nref is None:
            self.head=None
            print("LL is Empty")   
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def remove(self,x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.nref is not None:
            if self.head.data==x:
                self.head=None
            else:
                print("Node is wrong")
                return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref=n.nref
            n.pref.nref=n.pref  
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print("Wrong Node")    
             
if __name__ == "__main__":
    dll = Doubley_Linked_List()

    dll.insert_begining(10)
    dll.insert_begining(20)
    dll.insert_end(30)
    dll.insert_after(25, 20)
    dll.insert_before(15, 10)

    print("Print Forward:")
    dll.print_Forwared()

    print("Print Backward:")
    dll.print_BackWard()

    dll.remove_start()
    print("After removing start:")
    dll.print_Forwared()

    dll.remove_end()
    print("After removing end:")
    dll.print_Forwared()

    dll.remove(25)
    print("After removing 25:")
    dll.print_Forwared()
                
            
                    
                
                          
                
                    
                    
                  