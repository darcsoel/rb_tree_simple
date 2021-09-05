from env import (
    BLACK,
    LEFT_POSITION,
    LEFT_ROTATION,
    RED,
    RIGHT_POSITION,
    RIGHT_ROTATION,
)
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
                node.position = RIGHT_POSITION
                parent.right_child = node
                return node
        else:
            if parent.left_child:
                self._insert(node, parent.left_child)
            else:
                node.parent = parent
                node.position = LEFT_POSITION
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
                if node.parent.parent.color is BLACK:
                    node.parent.parent.color = RED
                else:
                    node.parent.parent.color = BLACK

            return
        else:
            self._case4(node)

    def _case4(self, node: Node):
        """
        Father if red, uncle is black
        New node is right (left) child, parent is left (right) child
        Make left (right) rotate from father

        :param node: Node
        :return: None
        """

        uncle = node.parent.brother

        if node.parent.color is RED and get_color(uncle) is BLACK:
            if (
                node.parent.position is LEFT_POSITION
                and node.parent.parent.position is LEFT_POSITION
            ):
                pass
            elif (
                node.parent.position is RIGHT_POSITION
                and node.parent.parent.position is RIGHT_POSITION
            ):
                pass
            return
        else:
            self._case5(node)

    def _case5(self, node: Node):
        """
        Father if red, uncle is black
        New node is left (right) child, parent is left (right) child
        Make right rotate (left) from grandfather

        :param node: Node
        :return: None
        """
        pass

    def _rotate(self, node: Node, direction: str = LEFT_ROTATION) -> None:
        """
        Rotate peace of tree
        Child and direction is linked, depends on direction

        :param node: center node to rotate, parent-(node)-child
        :param direction: -1 - left, 1 - right
        :return: None
        """
        if node == self.root:
            node.color = BLACK
            return

        if direction is LEFT_ROTATION:
            parent = node.parent
            rotator = node
            child = node.right_child

            parent.left_child = child
            child.left_child = rotator
        elif direction is RIGHT_ROTATION:
            parent = node.parent
            rotator = node
            child = node.left_child

            parent.left_child = child
            child.left_child = rotator
        else:
            raise ValueError("unknown rotation direction")
