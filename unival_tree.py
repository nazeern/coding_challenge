class Node():

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def num_unival(self):
        if self.is_leaf():
            return 1
        
        return self.left.num_unival() + self.right.num_unival() + (self.left.val == self.right.val)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
    
    def get_value(self):
        return self.val

    def __str__(self):
        return str(self.val)






if __name__ == "__main__":
    print("Constructing binary tree:")
    root = Node(0, 
                Node(1),
                Node(0,
                    Node(1,
                        Node(1),
                        Node(1)),
                    Node(0)))
    
    print(root.num_unival())

    
    