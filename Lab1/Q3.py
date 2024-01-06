class BinaryTree:
    def __init__(self, root):
      self.left = None
      self.right = None
      self.root = root
      
    def insert(self, data):
      if self.root:
         if data < self.root:
            if self.left is None:
               self.left = BinaryTree(data)
            else:
               self.left.insert(data)
         elif data > self.root:
               if self.right is None:
                  self.right = BinaryTree(data)
               else:
                  self.right.insert(data)
      else:
         self.root = data
         
    def InOrder(self):
      if self.left:
         self.left.InOrder()
      print( self.root,end=" ")
      if self.right:
         self.right.InOrder()
    
    def PreOrder(self):
        print(self.root,end=" ")
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()
            
    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.root,end=" ")
        
def main():
    b = BinaryTree(25)
    values = [15,10,4,12,22,18,24,50,35,31,44,70,66,90]
    for i in values:
        b.insert(i)
    print("InOrder:")
    b.InOrder()
    print("\nPreOrder:")
    b.PreOrder()
    print("\nPostOrder:")
    b.PostOrder()

if __name__ == "__main__":
    main()