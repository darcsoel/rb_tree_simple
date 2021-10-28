from env import BLACK, LEFT, RED, RIGHT
from node import Node, get_color


class RedBlackTree:
    """
    Red-black tree implementation.
    Tree conditions:

    Each node is red or black
    Root always black
    Every leave is black
    If node is red - both children are black
    All paths from each node to leaves has equal number of black nodes

    """

    def __init__(self):
        self.root = None

    def insert(self, value: int):
        """
        inserting in _insert method
        _case method responsible for recolor and rotate
        """

        node = Node(value=value)
        self._insert(node, self.root)
        self._case1(node)

        self.root.color = BLACK
        return True

    def _insert(self, node, parent):
        """
        Recursive insert logic

        :param node: Node
        :param parent: Node

        :return: None
        """
        if not parent:
            return node

        if node >= parent:
            if parent.right_child:
                self._insert(node, parent.right_child)
            else:
                node.parent = parent
                node.position = RIGHT
                parent.right_child = node
                return node
        else:
            if parent.left_child:
                self._insert(node, parent.left_child)
            else:
                node.parent = parent
                node.position = LEFT
                parent.left_child = node
                return node

    def _case1(self, node: Node):
        """
        Case if new node is root. Paint in black and finish procedure.

        :param node: Node
        :return: None
        """
        if self.root:
            self._case2(node)
        else:
            node.color = BLACK
            self.root = node

    def _case2(self, node: Node):
        """
        Case if father is black. Condition 3 and 5 are correct.
        """

        if node.parent.color is BLACK:
            return
        else:
            self._case3(node)

    def _case3(self, node: Node):
        """
        Case if father and uncle are red.
        Recolor both to black and recolor grandfather.

        :param node: Node
        :return: None
        """

        uncle_node = node.parent.brother
        uncle_color = get_color(uncle_node)

        if node.parent.color is RED and uncle_node and uncle_color is RED:
            node.parent.color = BLACK
            if uncle_node:
                uncle_node.color = BLACK

            if node.parent.parent:
                node.parent.parent.recolor()

            return
        else:
            self._case4(node)

    def _case4(self, node: Node):
        """
        Father if red, uncle is black
        New node is right (left) child, parent is left (right) child
        Make left (right) rotate over father

        :param node: Node
        :return: None
        """

        uncle = node.parent.brother
        temp = None

        if node.parent.color is RED and get_color(uncle) is BLACK:
            if node.parent.position is LEFT and node.position is RIGHT:
                temp = node.parent
                node.position = LEFT
                tmp = node.parent.parent
                node.parent.parent.left_child = node
                temp.left_child = None
                node.left_child = temp
                temp.parent = node
                temp.parent.parent = tmp
                temp.right_child = None
            elif node.parent.position is RIGHT and node.position is LEFT:
                temp = node.parent
                node.position = RIGHT
                tmp = node.parent.parent
                node.parent.parent.right_child = node
                temp.right_child = None
                node.right_child = temp
                temp.parent = node
                temp.parent.parent = tmp
                temp.left_child = None

        self._case5(temp if temp else node)

    def _case5(self, node: Node):
        """
        Father if red, uncle is black
        New node is left (right) child, parent is left (right) child
        Make right rotate (left) from grandfather

        :param node: Node
        :return: None
        """
        uncle = node.parent.brother
        temp = None

        if node.parent.color is RED and get_color(uncle) is BLACK:
            if node.parent.position is LEFT and node.position is LEFT:
                temp = node.parent.parent
                node.parent.parent = temp.parent
                temp.parent = node.parent
                temp.left_child = uncle
                temp.recolor()
                temp.position = RIGHT

                if node.parent is None:
                    self.root = node
                else:
                    node.parent.right_child = temp
                    node.parent.recolor()

                    if node.parent.parent:
                        node.parent.parent.left_child = node.parent

            elif node.parent.position is RIGHT and node.position is RIGHT:
                temp = node.parent.parent
                node.parent.parent = temp.parent
                temp.parent = node.parent
                temp.right_child = uncle
                temp.recolor()
                temp.position = LEFT

                if node.parent is None:
                    self.root = node
                else:
                    node.parent.left_child = temp
                    node.parent.recolor()

                    if node.parent.parent:
                        node.parent.parent.right_child = node.parent

        if temp and temp == self.root:
            self.root = temp.parent

        self.root.color = BLACK
        return True
