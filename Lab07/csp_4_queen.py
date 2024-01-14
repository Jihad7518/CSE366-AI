class FourQueensCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}

    def is_consistent(self, variable, value, assignment):
        for other_variable in self.constraints[variable]:
            if other_variable in assignment:
                other_value = assignment[other_variable]
                if value == other_value or abs(value - other_value) == abs(self.variables[variable] - self.variables[other_variable]):
                    return False
        return True

    def select_unassigned_variable(self, assignment):
        unassigned_variables = [var for var in self.variables if var not in assignment]
        return min(unassigned_variables, key=lambda var: len(self.domains[var]))

    def improved_backtracking(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment  # All variables are assigned, solution found

        variable = self.select_unassigned_variable(assignment)
        ordered_domain = self.domains[variable]

        for value in ordered_domain:
            if self.is_consistent(variable, value, assignment):
                assignment[variable] = value
                result = self.improved_backtracking(assignment)
                if result is not None:
                    return result
                del assignment[variable]  # Backtrack

        return None

    def solve(self):
        return self.improved_backtracking({})


# Example usage for the 4-queens problem
if __name__ == "__main__":
    # Variables represent columns, and domains represent possible row positions
    variables = {0, 1, 2, 3}
    domains = {var: {0, 1, 2, 3} for var in variables}

    # Constraints represent the no-attack condition between queens
    constraints = {
        0: {1, 2, 3},
        1: {0, 2, 3},
        2: {0, 1, 3},
        3: {0, 1, 2}
    }

    four_queens_csp = FourQueensCSP(variables, domains, constraints)
    solution = four_queens_csp.solve()

    if solution is not None:
        print("4-Queens Solution:")
        for variable, value in solution.items():
            print(f"Column {variable}: Row {value}")
    else:
        print("No solution found.")

