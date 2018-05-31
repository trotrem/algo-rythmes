from implementation import Node

def delete_middle(node):
    "deletes non-terminal node"
    try:
        node.data = node.next.data
        node.next = node.next.next
    except AttributeError:
        print("node must be non-terminal")
        
# testing
a = Node(4)
a.push(3)
a.push(2)

delete_middle(a.next)

print(a.length())
# >> 2

delete_middle(a.next)
# >> node must be non-terminal
