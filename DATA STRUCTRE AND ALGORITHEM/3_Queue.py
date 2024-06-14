class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size
    
    def enqueue(self, item):
        if len(self.queue) < self.max_size:
            self.queue.append(item)
            print(f"Enqueued {item} to the queue.")
        else:
            print(f"Queue is full. Cannot enqueue {item}.")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue.pop(0)
        print(f"Dequeued {item} from the queue.")
        return item
    
    def front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        print(f"Front item is {self.queue[0]}.")
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        print(f"Queue size is {len(self.queue)}.")
        return len(self.queue)
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current queue (from front to rear):")
            for item in self.queue:
                print(item, end=' ')
            print()

def display_menu():
    print("\nQueue Operations Menu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Front")
    print("4. Display Queue")
    print("5. Queue Size")
    print("6. Exit")

if __name__ == "__main__":
    max_size = int(input("Enter the maximum size of the queue: "))
    q = Queue(max_size)
    
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item = input("Enter the item to enqueue: ")
            q.enqueue(item)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.front()
        elif choice == 4:
            q.display()
        elif choice == 5:
            q.size()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
