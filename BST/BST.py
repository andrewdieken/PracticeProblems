class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    # Returns the children in an Array
    def getChildren(self):
        children = []
        if(self.left != None):
            children.append(self.left)
        if(self.right != None):
            children.append(self.right)
        return children

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(val)
        if self.root == None:
            root = newNode
        else:
            current = self.root
            while(True):
                if(newNode.val < current.val):
                    if(current.left == None):
                        current.left = newNode
                        break
                    else:
                        current = current.left
                else:
                    if(current.right == None):
                        current.right = newNode
                        break
                    else:
                        current = current.right

    def getMin(self):
        if (self.root == None):
            return None
        else:
            current = self.root
            while(current.left != None):
                current = current.left
            return current

    def getMax(self):
        if (self.root == None):
            return None
        else:
            current = self.root
            while(current.right != None):
                current = current.right
            return current



if __name__ == '__main__':
    testTree = BinarySearchTree()

    print("Insert 5")
    testTree.insert(5)
    print(testTree.getMin())

    print("Insert 10")
    testTree.insert(10)
    print("Insert 2")
    testTree.insert(2)
    print(testTree.getMin())
    print(testTree.getMax())
