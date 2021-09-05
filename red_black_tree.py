from env import BLACK, LEFT_ROTATION, NIL, RED, RIGHT_ROTATION
from node import Node


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
        node = Node(value=value)

        try:
            self._case1(node)
        except RuntimeError:
            pass

        return True

    # def find(self, value) -> Node:
    #     """
    #     Find node with needed value
    #
    #     :param value: search value
    #     :return: Node
    #     """
    #     if node.parent_node is None:
    #         parent_node = self.root
    #     else:
    #         parent_node = node.parent
    #
    #     if node < parent_node:
    #         return self.find(node.left_child)
    #     elif node > parent_node:
    #         return self.find(node.right_child)
    #
    #     if node == parent_node:
    #         return parent_node
    #
    #     raise KeyError('Value not exist')

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

    def _case2(self, node: Node, parent=None):
        """
        Case if father is black. Condition 3 and 5 are correct.

        :param node: Node
        :return: None
        """

        parent = parent or self.root

        if parent.color is BLACK:
            if node > parent:
                if parent.right_child is not None:
                    self._case2(node, parent.right_child)
                else:
                    parent.right_child = node
                    return
            else:
                if parent.left_child is not None:
                    self._case2(node, parent.left_child)
                else:
                    parent.left_child = node
                    return

        self._case3(node)

    def _case3(self, node: Node):
        """
        Case if father and uncle are red.
        Recolor both to black and recolor grandfather.

        :param node: Node
        :return: None
        """

        uncle = node.uncle

        if node.parent.color is RED and uncle and uncle.color is RED:
            pass
        else:
            self._case4(node)

    def _case4(self, node: Node):
        """
        Father if red, uncle is black
        New node is right child, parent is left child
        Make left rotate

        :param node: Node
        :return: None
        """
        pass

    def _case5(self, node: Node):
        """
        Father if red, uncle is black
        New node is left child, parent is left child
        Make right rotate with grandfather

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
            raise ValueError('unknown rotation direction')
