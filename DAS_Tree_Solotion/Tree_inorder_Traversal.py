def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.info, end=' ')
        inOrder(root.right)
