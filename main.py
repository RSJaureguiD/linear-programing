from scipy.optimize import linprog as lp, OptimizeResult
from warnings import simplefilter

simplefilter("ignore", DeprecationWarning)

def solve_problem_without_vars() -> OptimizeResult:
    # Coefficients of the objective function (inverted for max to min switch)
    c = [-40, -10]

    # Coefficients of the equality constraints
    A_eq = [
        [-6, 1],
    ]

    # Coefficients of the inequality constraints
    A_ub = [
        [8,  2],
        [0,  6],
        [20, 0]
    ]

    # Right-hand side of the equality constraints
    b_eq = [0]

    # Right-hand side of the inequality constraints
    b_ub = [7200, 10800, 6600]

    # Initial restrictions (bounds for each variable)
    x_bounds = [(3, None), (0, None)]

    # Solve the linear programming problem
    res = lp(c, A_ub, b_ub, A_eq, b_eq, bounds=x_bounds, method='simplex')

    return res

   
def solve_problem_with_vars() -> OptimizeResult:
    # Define the variable w
    w = 1_000_000

    # Coefficients of the objective function (inverted for max to min switch)
    c = [-40, -10, 0, 0, 0, w]

    # Coefficients of the equality constraints
    A_eq = [
        [8, 2, 1, 0, 0, 0],
        [0, 6, 0, 1, 0, 0],
        [20, 0, 0, 0, 1, 0],
        [-6, 1, 0, 0, 0, 1],
    ]

    # Right-hand side of the equality constraints
    b_eq = [7200, 10800, 6600, 0]

    # Initial restrictions (bounds for each variable)
    x_bounds = [(3, None)].append([(0, None)] * 5)

    # Solve the linear programming problem
    res = lp(c, None, None, A_eq, b_eq, bounds=x_bounds, method='simplex')

    return res

def solve_problem(withvars: bool = False) -> OptimizeResult:
    if withvars:
        res = solve_problem_with_vars()
    else:
        res = solve_problem_without_vars()

    if res.success:
        print("Optimal solution found:")
        print(f"Number of tables (x1): {res.x[0]}")
        print(f"Number of chairs (x2): {res.x[1]}")
        print(f"Value of the objective function (Z): {-res.fun}")
    else:
        print("No optimal solution found.")

    return res

if __name__ == "__main__":
    solve_problem()
   