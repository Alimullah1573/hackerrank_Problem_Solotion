def preOrder(root):
    if root is not None:

        preOrder(root.left)
        preOrder(root.right)
        print(root.info, end=' ')