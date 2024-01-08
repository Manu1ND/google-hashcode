import pytest
import solver

case1 = ("azzzzz" "zzazz")
case2 = ("azzxxx" "zzxxax")

cases = [case1, case2]


@pytest.mark.parametrize("input1, output", cases)
def test_solve1(input1, output):
    assert solver.solver(input1) == output
