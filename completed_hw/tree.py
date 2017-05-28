class Node(object):
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

class BinarySearchTree(object):
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self,data,node):
        if data<node.data:
            if node.leftChild:
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild=Node(data)
        else:
            if node.rightChild:
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild=Node(data)

    def Inorder(self):
        if self.root:
            self.traverseInorder(self.root)

    def traverseInorder(self, node):
        if node.leftChild:
            self.traverseInorder(node.leftChild)

        print(str(node.data))

        if node.rightChild:
            self.traverseInorder(node.rightChild)

    def Preorder(self):
        if self.root:
            self.traversePreorder(self.root)


    def traversePreorder(self, node):
        print(str(node.data))

        if node.leftChild:
            self.traverseInorder(node.leftChild)


        if node.rightChild:
            self.traverseInorder(node.rightChild)

    def search(self,value):
         if self.root:
             self.searchBST(value, node)


    def searchBST(self,value,node):
        
        if value==node.data:
            return True
        elif value>node.data:
            if node.rightChild:
                searchBST(node.rightChild)
        elif value<node.data:
            if node.leftChild:
                searchBST(node.leftChild)
        return False



bst=BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)