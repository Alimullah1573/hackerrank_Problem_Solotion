def height(root):
    if root is None:
        return -1

    return max(height(root.left), height(root.right)) + 1