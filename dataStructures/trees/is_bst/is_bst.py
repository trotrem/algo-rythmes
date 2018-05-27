class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBST(root):
    if root:
        return (checkLeftRight(root.left, root.data, float('-inf'))
                and checkLeftRight(root.right, float('inf'), root.data))
    return True


def checkLeftRight(root, less, more):
    if root == None:
        return True
    if root.data <= more or root.data >= less:
        return False
    return (checkLeftRight(root.left, root.data, more)
            and checkLeftRight(root.right, less, root.data))
