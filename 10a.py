stack = []
def push():
    page = input("Enter the page name: ")
    stack.append(page)
    print("Page added successfully")

def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Removed page:", stack.pop())

def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top page:", stack[-1])

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Visited pages (top to bottom):")
        for page in reversed(stack):
            print(page)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting program")
        break
    else:
        print("Invalid choice")

