import queue

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
    q = queue.Queue(maxsize=max_size)
    
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            if q.full():
                print("Queue is full. Cannot enqueue.")
            else:
                item = input("Enter the item to enqueue: ")
                q.put(item)
                print(f"Enqueued {item} to the queue.")
                
        elif choice == 2:
            if q.empty():
                print("Queue is empty. Cannot dequeue.")
            else:
                item = q.get()
                print(f"Dequeued {item} from the queue.")
                
        elif choice == 3:
            if q.empty():
                print("Queue is empty.")
            else:
                item = q.queue[0]
                print(f"Front item is {item}.")
                
        elif choice == 4:
            if q.empty():
                print("Queue is empty.")
            else:
                print("Current queue (from front to rear):")
                for item in list(q.queue):
                    print(item, end=' ')
                print()
                
        elif choice == 5:
            size = q.qsize()
            print(f"Queue size is {size}.")
            
        elif choice == 6:
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")
