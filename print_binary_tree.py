# Recursive Python program for level
# order traversal of Binary Tree
from collections import deque

class BinarySearchTree:

    class __Node:

        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def get_val(self):
            return self.val

        def set_val(self, val):
            self.val = val

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def set_left(self, new_left):
            self.left = new_left

        def set_right(self, new_right):
            self.right = new_right

        # this method is the inorder traversal of the binary tree
        def __iter__(self):
            if self.left is not None:
                for e in self.left:
                    yield e

            yield self.val

            if self.right is not None:
                for e in self.right:
                    yield e

    def __init__(self):
        self.root = None

    def insert(self, val):

        def __insert(root, val):
            if root is None:
                return BinarySearchTree.__Node(val)

            if val is None:
                return root

            if val < root.get_val():
                root.set_left(__insert(root.get_left(), val))
            else:
                root.set_right(__insert(root.get_right(), val))

            return root

        self.root = __insert(self.root, val)

    def __iter__(self):

        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()

# Driver program to test above function


def in_order(root):
    if root is not None:
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


def level_order(root):

    if root is None: return
    q = deque()
    q.append(root)

    while q:
        current = q.popleft()
        # print(f'current: {current}')
        print(f'node: {current.val}', end=' ')
        if current.left: q.append(current.left)
        if current.right: q.append(current.right)


def main():

    # lst = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    lst = [-10, -3, 0, 5, 9]
    # lst = [5, 8, 2, 1, 4, 9, 6, 7]

    tree = BinarySearchTree()

    for x in lst:
        tree.insert(x)

    # for x in tree:
    #     print(x)

    # print('in order traversal ->')
    # in_order(tree.root)
    # print()

    # print('pre order traversal ->')
    # pre_order(tree.root)
    # print()

    # print('post order traversal ->')
    # post_order(tree.root)
    # print()

    print('level order traversal ->')
    level_order(tree.root)
    print()

    print('Done')


if __name__ == "__main__":
    main()
