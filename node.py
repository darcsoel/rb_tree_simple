from env import BLACK, LEFT, RED, RIGHT


class Node:
    def __init__(self, color=RED, value=None, parent=None):
        """
        At start - node always red, recolor on condition
        Child nodes are None, not NIL, to prevent redundant object creating
        """

        self._check_color(color)

        self.color = color
        self.value = value
        self.parent = parent
        self._position = None

        self.left_child = self.right_child = None

    @staticmethod
    def _check_color(color):
        if color not in [BLACK, RED]:
            raise ValueError(
                f"Wrong color {color}. Acceptable is {(BLACK, RED)}"
            )

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if value not in (LEFT, RIGHT):
            raise ValueError(f"Node position could be {LEFT} or {RIGHT}")

        self._position = value

    @property
    def brother(self) -> ("Node", None):
        """
        We cannot get node uncle before we insert it,
        so we will get potential uncle as "brother" of current node

        :return: Node or null
        """
        try:
            parent = self.parent

            if parent.left_child.value == self.value:
                brother = parent.right_child
            else:
                brother = parent.left_child
        except AttributeError:
            return None

        return brother

    def recolor(self):
        if self.color is RED:
            self.color = BLACK
        elif self.color is BLACK:
            self.color = RED
        else:
            raise ValueError(f"Wrong node color - {self.color}")

    def __lt__(self, other):
        return self.value < other.value

    def __ge__(self, other):
        return self.value >= other.value


def get_color(node: Node = None):
    """
    Default color is red, so we save memory and not creating NIL
    If node is NIL - it doesnt exists
    We catch exception and saying its black colored NIL
    """

    try:
        color = node.color
    except AttributeError:
        # because NIL is black leave
        color = BLACK

    return color
