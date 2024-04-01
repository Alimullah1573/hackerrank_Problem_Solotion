def postOrder(root):
    if root is not None:

        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=' ')
