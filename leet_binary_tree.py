import math


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
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

    def make_tree(self, lst):
        pass


################################################################
# level 0, i = 0
# level 1, i = 1, 2
# level 2, i = 3, 4, 5, 6
# level 3, i = 7, 8, 9, 10, 11, 12, 13, 14
################################################################
def main():

    lst = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    print(f'Tree (length {len(lst)}): {lst}')

    level = int(math.log2(len(lst)))
    print(f'level of this tree is {level}')

    parent = [(0, 0)]
    while parent:
        j, depth = parent.pop(0)

        if (2 * j + 1) <= len(lst) and lst[j] is not None:
            parent.append((2*j+1, depth+1))
        if (2 * j + 2) <= len(lst) and lst[j] is not None:
            parent.append((2*j+2, depth+1))

        print(f'list index = {j} -> children {parent}')


if __name__ == '__main__':
    main()
