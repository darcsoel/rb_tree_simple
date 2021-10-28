import unittest

from env import BLACK, LEFT, RED, RIGHT
from node import Node
from red_black_tree import RedBlackTree


def insert_values_into_rb_tree(values):
    tree = RedBlackTree()

    for value in values:
        tree.insert(value)

    return tree


class NodeTest(unittest.TestCase):
    def test_color_correct(self):
        node = Node(color=RED, value=1)
        self.assertEqual(node.color, RED)

    def test_color_incorrect(self):
        with self.assertRaises(ValueError):
            Node(color="YELLOW", value=1)


class ThreeElementsBaseTestCase(unittest.TestCase):
    def test_insert_case1(self):
        # values = [5, 6, 3, 10, 1, 40]
        values = [5]
        tree = insert_values_into_rb_tree(values)
        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.left_child, None)
        self.assertEqual(tree.root.right_child, None)

    def test_insert_case2_1(self):
        # values = [5, 6, 3, 10, 1, 40]
        values = [5, 6]
        tree = insert_values_into_rb_tree(values)
        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.left_child, None)
        self.assertEqual(tree.root.right_child.value, 6)

    def test_insert_case2_2(self):
        values = [5, 3]
        tree = insert_values_into_rb_tree(values)
        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.left_child.value, 3)
        self.assertEqual(tree.root.right_child, None)

    def test_insert_case2_3(self):
        values = [5, 6, 3]
        tree = insert_values_into_rb_tree(values)

        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.color, BLACK)

        self.assertEqual(tree.root.left_child.value, 3)
        self.assertEqual(tree.root.left_child.color, RED)
        self.assertEqual(tree.root.left_child.position, LEFT)

        self.assertEqual(tree.root.right_child.value, 6)
        self.assertEqual(tree.root.right_child.color, RED)
        self.assertEqual(tree.root.right_child.position, RIGHT)

    def test_insert_case3_1(self):
        values = [5, 6, 3, 10]
        tree = insert_values_into_rb_tree(values)

        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.color, BLACK)

        self.assertEqual(tree.root.left_child.value, 3)
        self.assertEqual(tree.root.left_child.color, BLACK)

        self.assertEqual(tree.root.right_child.value, 6)
        self.assertEqual(tree.root.right_child.color, BLACK)

        self.assertEqual(tree.root.right_child.right_child.value, 10)
        self.assertEqual(tree.root.right_child.right_child.color, RED)

    def test_insert_case3_2(self):
        values = [5, 6, 3, 1]
        tree = insert_values_into_rb_tree(values)

        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.color, BLACK)

        self.assertEqual(tree.root.left_child.value, 3)
        self.assertEqual(tree.root.left_child.color, BLACK)

        self.assertEqual(tree.root.left_child.left_child.value, 1)
        self.assertEqual(tree.root.left_child.left_child.color, RED)

        self.assertEqual(tree.root.right_child.value, 6)
        self.assertEqual(tree.root.right_child.color, BLACK)

    def test_insert_case3_3(self):
        values = [5, 6, 3, 10, 1]
        tree = insert_values_into_rb_tree(values)

        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.color, BLACK)

        self.assertEqual(tree.root.left_child.value, 3)
        self.assertEqual(tree.root.left_child.color, BLACK)

        self.assertEqual(tree.root.left_child.left_child.value, 1)
        self.assertEqual(tree.root.left_child.left_child.color, RED)

        self.assertEqual(tree.root.right_child.value, 6)
        self.assertEqual(tree.root.right_child.color, BLACK)

        self.assertEqual(tree.root.right_child.right_child.value, 10)
        self.assertEqual(tree.root.right_child.right_child.color, RED)

    def test_insert_case4_1(self):
        values = [5, 6, 3, 10, 1, 2]
        tree = insert_values_into_rb_tree(values)

        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.color, BLACK)

        self.assertEqual(tree.root.left_child.value, 2)
        self.assertEqual(tree.root.left_child.color, BLACK)

        self.assertEqual(tree.root.left_child.left_child.value, 1)
        self.assertEqual(tree.root.left_child.left_child.color, RED)

        self.assertEqual(tree.root.left_child.right_child.value, 3)
        self.assertEqual(tree.root.left_child.right_child.color, RED)

        self.assertEqual(tree.root.right_child.value, 6)
        self.assertEqual(tree.root.right_child.color, BLACK)

        self.assertEqual(tree.root.right_child.right_child.value, 10)
        self.assertEqual(tree.root.right_child.right_child.color, RED)

    def test_insert_case5_1(self):
        """
        Testing case 4 and case 5 at same time
        """

        values = [3, 1, 2]
        tree = insert_values_into_rb_tree(values)

        self.assertEqual(tree.root.value, 2)
        self.assertEqual(tree.root.color, BLACK)

        self.assertEqual(tree.root.left_child.value, 1)
        self.assertEqual(tree.root.left_child.color, RED)

        self.assertEqual(tree.root.right_child.value, 3)
        self.assertEqual(tree.root.right_child.color, RED)

    def test_insert_case5_2(self):
        values = [5, 6, 3, 10, 1, 40]
        tree = insert_values_into_rb_tree(values)

        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.color, BLACK)

        self.assertEqual(tree.root.left_child.value, 3)
        self.assertEqual(tree.root.left_child.color, BLACK)

        self.assertEqual(tree.root.left_child.left_child.value, 1)
        self.assertEqual(tree.root.left_child.left_child.color, RED)

        self.assertEqual(tree.root.right_child.value, 10)
        self.assertEqual(tree.root.right_child.color, BLACK)

        self.assertEqual(tree.root.right_child.left_child.value, 6)
        self.assertEqual(tree.root.right_child.left_child.color, RED)

        self.assertEqual(tree.root.right_child.right_child.value, 40)
        self.assertEqual(tree.root.right_child.right_child.color, RED)


if __name__ == "__main__":
    unittest.main()
