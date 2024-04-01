def insert(self, val):
    if self.root is None:
        self.root = Node(val)
        return
    root = self.root
    while 1:
        if val < root.info:
            if root.left is not None:
                root = root.left
            else:
                root.left = Node(val)
                break
        elif val >= root.info:
            if root.right is not None:
                root = root.right
            else:
                root.right = Node(val)
                break