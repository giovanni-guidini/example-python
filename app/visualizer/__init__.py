from collections import deque
from collections.abc import Generator
from typing import NamedTuple, Tuple
from app.expression import BaseNode, BinaryOpNode, Node, UnitaryOpNode


class NodeWithLevel(NamedTuple):
    node: Node
    level: int


def pretty_print(root: Node) -> Generator[str, None, None]:
    node_queue: deque[NodeWithLevel] = deque()
    node_queue.append(NodeWithLevel(root, 0))
    current_line = ""
    padding_line = ""
    previous_level = 0
    while node_queue:
        current_node, current_level = node_queue.popleft()
        if current_level != previous_level:
            # We finished a row of the expressions. Emit it and reset for the next one
            yield current_line
            yield padding_line
            current_line = ""
            padding_line = ""
        # Process current node
        if isinstance(current_node, BinaryOpNode):
            current_line += current_node.op.name + " "
            padding_line += "| \\"
            node_queue.append(NodeWithLevel(current_node.lhs, current_level + 1))
            node_queue.append(NodeWithLevel(current_node.rhs, current_level + 1))
        elif isinstance(current_node, UnitaryOpNode):
            current_line += current_node.op.name + " "
            padding_line += "|"
            node_queue.append(NodeWithLevel(current_node.lhs, current_level + 1))
        else:
            # All Nodes are a subclass of BaseNode
            current_line += str(current_node.lhs)
    yield current_line
