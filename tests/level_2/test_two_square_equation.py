from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__full_square_equation_success():
    square_coefficient = 1
    linear_coefficient = -4
    const_coefficient = -5

    result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert result[0] == -1
    assert result[1] == 5


def test__solve_square_equation__discriminant_less_than_zero():
    square_coefficient = 2
    linear_coefficient = -1
    const_coefficient = 1

    result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert result[0] is None
    assert result[1] is None


def test__solve_square_equation__without_square_and_linear_coefficients():
    square_coefficient = 0
    linear_coefficient = 0
    const_coefficient = 1

    result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert result[0] is None
    assert result[1] is None


def test__solve_square_equation__without_square_coefficient():
    square_coefficient = 0
    linear_coefficient = 2
    const_coefficient = 1

    result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert result[0] == -0.5
    assert result[1] is None
