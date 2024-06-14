from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, items):
        for item in items:
            self.stack.append(item)
            print(f"Pushed {item} onto the stack.")
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        item = self.stack.pop()
        print(f"Popped {item} from the stack.")
        return item
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        print(f"Top item is {self.stack[-1]}.")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        print(f"Stack size is {len(self.stack)}.")
        return len(self.stack)
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Current stack (from bottom to top):")
            for item in list(self.stack):
                print(item, end=' ')
            print()

def display_menu():
    print("\nStack Operations Menu:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if empty")
    print("5. Get size")
    print("6. Display stack")
    print("7. Exit")

if __name__ == "__main__":
    stack = Stack()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            items = input("Enter items to push onto the stack (separated by spaces): ").split()
            stack.push(items)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == '5':
            stack.size()
        elif choice == '6':
            stack.display()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
