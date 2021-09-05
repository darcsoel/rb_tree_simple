import unittest

from red_black_tree import RedBlackTree


def insert_values_into_rb_tree(values):
    tree = RedBlackTree()

    for value in values:
        tree.insert(value)

    return tree


class ThreeElementsBaseTestCase(unittest.TestCase):
    def test_insert_case1(self):
        # values = [5, 6, 3, 10, 1, 40]
        values = [5]
        tree = insert_values_into_rb_tree(values)
        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.left_child, None)
        self.assertEqual(tree.root.right_child, None)


if __name__ == '__main__':
    unittest.main()
