
def levelOrder(root):
    q = []
    q.append(root)
    while (len(q) !=0):
        root = q.pop(0)
        print(root.info,end=' ')
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)

