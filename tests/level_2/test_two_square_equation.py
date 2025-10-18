from functions.level_2.two_square_equation import solve_square_equation
import pytest


@pytest.mark.parametrize("square_coefficient, linear_coefficient, const_coefficient, root_1, root_2",
                         [(1, -4, -5, -1, 5)]
                         )
def test__solve_square_equation__full_square_equation_returns_two_roots(square_coefficient, linear_coefficient, const_coefficient, root_1, root_2):
    result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert result[0] == root_1
    assert result[1] == root_2


@pytest.mark.parametrize("square_coefficient, linear_coefficient, const_coefficient, root_1, root_2",
                         [(2, -1, 1, None, None)]
                         )
def test__solve_square_equation__returns_none_when_discriminant_less_than_zero(square_coefficient, linear_coefficient, const_coefficient, root_1, root_2):
    result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert result[0] == root_1
    assert result[1] == root_2


@pytest.mark.parametrize("square_coefficient, linear_coefficient, const_coefficient, root_1, root_2",
                         [(0, 0, 1, None, None)]
                         )
def test__solve_square_equation__returns_none_without_square_and_linear_coefficients(square_coefficient, linear_coefficient, const_coefficient, root_1, root_2):
    result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert result[0] == root_1
    assert result[1] == root_2


@pytest.mark.parametrize("square_coefficient, linear_coefficient, const_coefficient, root_1, root_2",
                         [(0, 2, 1, -0.5, None)]
                         )
def test__solve_square_equation__returns_one_root_without_square_coefficient(square_coefficient, linear_coefficient, const_coefficient, root_1, root_2):
    result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert result[0] == root_1
    assert result[1] == root_2
