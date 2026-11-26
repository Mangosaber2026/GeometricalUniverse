def solve_eq(left_term, right_term, *variables):
    import sympy

    equation = sympy.Eq(left_term, right_term)

    answers: dict = sympy.solve(
        equation,
        *variables,
        dict=True
    )

    output = f"""
Left term: {left_term}
Right term: {right_term}

Equation:
    {left_term} = {right_term}

Simplified:
    {sympy.simplify(equation)}
"""

    if not answers:
        output += "\nNo solutions found."
    
    for i, answer in enumerate(answers, start=1):
        output += f"\nSolution {i}:\n"

        for var, ans in answer.items():
            output += f"    {var} = {ans}\n"

    return output

from sympy.abc import t

left_side = 60000
right_side = -0.138*t**2 + 2.76*t + 45.8
variables = t

result = solve_eq(left_side, right_side, variables)
print(result)