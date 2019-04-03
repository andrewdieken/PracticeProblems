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

    def getMin(self, root):
        if (root == None):
            return None
        else:
            current = root
            while(current.left != None):
                current = current.left
            return current

    def getMax(self, root):
        if (root == None):
            return None
        else:
            current = root
            while(current.right != None):
                current = current.right
            return current

    def contains(self, value):
        if(self.root == None):
            return False
        else:
            current = self.root
            while(current.val != value):
                if(value < current.val):
                    current = current.left
                else:
                    current = current.right
                if(current == None):
                    return False

            return True

    def inOrder(self, node):
        if(node != None):
            # UNCOMMENT: if you want to understand how the recursive calls work
            # print("inOrder({})".format(node.val))
            self.inOrder(node.left)
            print(node.val)
            self.inOrder(node.right)

    def preOrder(self, node):
        if(node != None):
            print(node.val)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def postOrder(self, node):
        if(node != None):
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.val)

    def delete(self, val):
        if(self.contains(val)):
            root = delete(root, val)
            return True
        else:
            return False

    def delete(self, val):
        current = self.root
        # find the node with the specified value
        while(current.val != val):
            parent = current
            if(val < current.val):
                current = current.left
            else:
                current = current.right
            if(current == None):
                return False
        #
        # Node has NO CHILDREN
        #
        if (current.left == None and current.right == None):
            # check if current is root
            if(current == self.root):
                root = None
            # current is the left child of parent
            elif(val < parent.val):
                parent.left = None
            # current is the right child of parent
            else:
                parent.right = None
        #
        # Node has only LEFT CHILD
        #
        elif(self.hasLeftChild(current)):
            # check if current is root
            if(current == self.root):
                root = current.left
            # current is the left child of parent
            elif(val < parent.val):
                parent.left = current.left
            # current is the right child of parent
            else:
                parent.right = current.left
        #
        # Node has only RIGHT CHILD
        #
        elif(self.hasRightChild(current)):
            # check if current is root
            if(current == self.root):
                root = current.right
            # current is left child of parent
            elif(val < parent.val):
                parent.left = current.right
            else:
                parnet.right = current.right
        #
        # Node as LEFT & RIGHT CHILDREN
        #
        else:
            # get the largest node in the left subtree
            successor = self.getMax(current.left)
            # check if current is root
            if(current == self.root):
                root = successor
                # TODO: replace successor with None
            # current is left child of parent
            elif(val < parent.val):
                parent.left = successor
                # TODO: replace successor with None
            # current is right child of parent
            else:
                parent.right = successor
                # TODO: replace successor with None

        return True


    def hasRightChild(self, node):
        return node.right != None

    def hasLeftChild(self, node):
        return node.left != None











#===============================================================================
# MAIN
#===============================================================================
if __name__ == '__main__':
    testTree = BinarySearchTree()

    testTree.insert(8)
    testTree.insert(5)
    testTree.insert(3)
    testTree.insert(6)
    testTree.insert(10)
    testTree.insert(9)
    testTree.insert(12)
    testTree.insert(4)

    testTree.inOrder(testTree.getRoot())
    print(testTree.delete(8))
    testTree.inOrder(testTree.getRoot())

    # root = testTree.getRoot()
    # print("Root:",root.getVal())
    # min = testTree.getMin()
    # max = testTree.getMax()
    # print("Min:",min.getVal())
    # print("Max:",max.getVal())
    #
    # print(testTree.contains(13))
    #
    # testTree.inOrder(testTree.getRoot())
    # testTree.preOrder(testTree.getRoot())
    # testTree.postOrder(testTree.getRoot())
