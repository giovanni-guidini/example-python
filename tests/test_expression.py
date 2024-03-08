import pytest
from app.expression import evaluate_expression, Operation, OpNode, BaseNode


@pytest.mark.parametrize(
    "expression,expected_result",
    [
        (BaseNode(lhs=1), 1),
        (OpNode(op=Operation.ADD, lhs=BaseNode(lhs=1), rhs=BaseNode(lhs=1)), 2),
        (
            OpNode(
                op=Operation.ADD,
                lhs=OpNode(
                    op=Operation.MULTIPLY, lhs=BaseNode(lhs=2), rhs=BaseNode(lhs=2)
                ),
                rhs=BaseNode(lhs=2),
            ),
            6,
        ),
    ],
)
def test_expressions(expression, expected_result):
    assert evaluate_expression(expression) == expected_result
