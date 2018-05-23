class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __last(self):
        n = self
        while n.next is not None:
            n = n.next
        return n

    def peek(self):
        return self.last().data


    def length(self):
        n = self
        counter = 0
        while n is not None:
            counter += 1
            n = n.next
        return counter

    def push(self, data):
        self.__last().next = Node(data)

    def pop(self):
        if self.next is not None:
            n = self
            while n.next.next is not None:
                n = n.next
            n.next = None

    def printList(self, separator = ", "):
        n = self
        print(n.data, end="")
        while n.next is not None:
            print(separator, end="")
            n = n.next
            print(n.data, end="")
        print("")
