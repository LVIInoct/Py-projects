#declaring constructors
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# adding
    def append(self, value):
        newNode = Node(value) # gives newNode the value
        newNode.next = None # pointer for next becomes none
        newNode.prev = self.tail # previous will point to tail
        if self.head is None: # if theres no tail, set tail to newNode
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode # tail's next will be newNode 
            self.tail = newNode # tail becomes newNode too
        print("Value added to list")

# polling
    def delete(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head # temp points to head
        self.head = self.head.next # head points to next
        if self.head is None: # if head is empty, tail is too
            self.tail = None
        else:
            self.head.prev = None # set previous pointer to empty too
        print("Removed:", temp.data)
        
# display from front to back
    def display_forward(self):
        trav = self.head
        size = 0
        if trav == None:
            print("List is empty\n")
            return
        while trav != None:
            print(f"[{trav.data}]", end=" ")
            size += 1
            trav = trav.next
        print(f"\nSize: {size}")

# display from back to front
    def display_backward(self):
        trav = self.tail
        size = 0
        if trav is None:
            print("List is empty")
            return
        while trav != None:
            print(f"[{trav.data}]", end=" ")
            size += 1
            trav = trav.prev
        print(f"\nSize: {size}")


def main():
    queue = DoublyLinkedList()
    while True:
        print("What would you like to do?\n1) append\n2) delete\n3)display forwards\n4) display backwards\n5) exit")
        choice = int(input(">"))
        # checking input
        match choice:
            case 1:
                print("Enter a value:")
                value = int(input())
                list.append(value)
            case 2:
                list.delete()
            case 3:
                list.display_forward()
            case 4:
                list.display_backward()
            case 5:
                break
            case _:
                print("Please give a valid answer as an integer.")


main()
