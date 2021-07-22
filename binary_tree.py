from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> None:
        """Object representation. Using python >= 3.9 feature"""
        return f"{self.val=}, {self.left=}, {self.right=}"


def to_binary_tree(items: List[int]) -> TreeNode:
    """Creates BT from list of values"""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, end=' ')
        in_order(root.right)


def pre_order(root):
    if root:
        print(root.val, end=' ')
        pre_order(root.left)
        pre_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val, end=' ')


root = to_binary_tree([-10, -3, 0, 5, 9])
# root = to_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
# print(root)
print('inorder ->'), in_order(root)
print('')
print('-' * 30)
print('preorder ->'), pre_order(root)
print('')
print('-' * 30)
print('postorder ->'), post_order(root)
print('')
print('-' * 30)
