class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def getVal(self):
        return self.val

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

    def getRoot(self):
        return self.root

    def isEmpty(self):
        return self.root == None

    def insert(self, newVal):
        if(self.root == None):
            self.root = Node(newVal)
            print("Added {} to root".format(self.root.val))
        else:
            current = self.root
            while(True):
                parent = current
                if(newVal < current.val):
                    current = current.left
                    if(current == None):
                        parent.left = Node(newVal)
                        print("Added {} to left child of {}".format(newVal, parent.val))
                        break
                else:
                    current = current.right
                    if(current == None):
                        parent.right = Node(newVal)
                        print("Added {} to right child of {}".format(newVal, parent.val))
                        break

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

    testTree.insert(8)
    testTree.insert(5)
    testTree.insert(3)
    testTree.insert(6)
    testTree.insert(10)
    testTree.insert(9)
    testTree.insert(12)

    root = testTree.getRoot()
    print("Root:",root.getVal())
    min = testTree.getMin()
    max = testTree.getMax()
    print("Min:",min.getVal())
    print("Max:",max.getVal())
