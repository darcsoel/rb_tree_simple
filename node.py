from env import BLACK, NIL, RED


class Node:
    def __init__(self, color=RED, value=NIL, parent=None):
        """At start - node always red, recolor on condition"""

        self._check_color(color)

        self.color = color
        self.value = value
        self.parent = parent

        self.left_child = self.right_child = None

    @staticmethod
    def _check_color(color):
        if color in [BLACK, RED]:
            return True
        raise ValueError(f'wrong color - {color}')

    def is_has_children(self):
        """Check if children are diff from NIL"""
        return self.left_child != NIL and self.right_child != NIL

    @property
    def uncle(self):
        try:
            parent = self.parent
            grandparent = parent.parent
        except AttributeError:
            return None

        if grandparent.left_child.value == parent.value:
            uncle = grandparent.right_child
        else:
            uncle = grandparent.left_child

        return uncle

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        if self.color == NIL and self.color == other.color:
            return True

        if self.parent is None or other.parent is None:
            parents_same = self.parent is None and other.parent is None
        else:
            parents_same = self.parent.value == other.parent.value \
                               and self.parent.color == other.parent.color

        node_same = self.value == other.value and self.color == other.color

        return node_same and parents_same
