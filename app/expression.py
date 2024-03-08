from dataclasses import dataclass
from enum import Enum
from typing import Union
from app.calculator import Calculator


class Operation(Enum):
    ADD = Calculator.add
    SUBTRACT = Calculator.subtract
    MULTIPLY = Calculator.multiply
    DIVIDE = Calculator.divide


@dataclass
class BaseNode:
    lhs: float
    op = None


@dataclass
class OpNode:
    op: Operation
    lhs: "Node"
    rhs: "Node"


Node = Union[BaseNode, OpNode]


def evaluate_expression(root: Node):
    if root.op is None:
        return root.lhs
    evaluated_lhs = evaluate_expression(root.lhs)
    evaluated_rhs = evaluate_expression(root.rhs)
    return root.op(evaluated_lhs, evaluated_rhs)
