import pytest
from shapes_lib import is_right_triangle, ValidationError


@pytest.mark.parametrize(
    "sides",
    [
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
    ],
)
def test_is_right_true(sides):
    a, b, c = sides
    assert is_right_triangle(a, b, c)
    assert is_right_triangle(c, a, b)
    assert is_right_triangle(b, c, a)


def test_is_right_false_close_but_not_right():
    assert not is_right_triangle(3, 4, 5.001)


def test_is_right_eps_tolerance():
    assert is_right_triangle(3, 4, (3**2 + 4**2) ** 0.5 * (1 + 1e-12))


def test_is_right_validates_input():
    with pytest.raises(ValidationError):
        is_right_triangle(1, 2, 3)
    with pytest.raises(ValidationError):
        is_right_triangle(-3, 4, 5)
