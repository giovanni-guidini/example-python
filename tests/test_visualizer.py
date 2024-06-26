import pytest

from app.expression import (
    BaseNode,
    BinaryOpNode,
    BinaryOperation,
    UnaryOperation,
    UnitaryOpNode,
)
from app.visualizer import pretty_print


@pytest.mark.parametrize(
    "expression, expected",
    [
        pytest.param(
            UnitaryOpNode(lhs=BaseNode(lhs=1), op=UnaryOperation.MINUS),
            "MINUS \n|\n1",
            id="-1",
        ),
    ],
)
def test_visualizer(expression, expected):
    expected_lines = expected.split("\n")
    emitted_lines = []
    for line in pretty_print(expression):
        emitted_lines.append(line)
    assert len(expected_lines) == len(
        emitted_lines
    ), f"Expected {len(expected_lines)} lines, received {len(emitted_lines)}"
    assert expected_lines == emitted_lines
