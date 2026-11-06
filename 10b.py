queue=[]
def enqueue():
    passenger = input("Enter passenger name: ")
    queue.append(passenger)
    print("Passenger added successfully")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Passenger served:", queue.pop(0))

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Passengers in queue:")
        for passenger in queue:
            print(passenger)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting program")
        break
    else:
        print("Invalid choice")
