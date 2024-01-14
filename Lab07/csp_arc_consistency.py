
class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        for other_variable, constraint in self.constraints[variable]:
            if other_variable in assignment and not constraint(value, assignment[other_variable]):
                return False
        return True

    def select_unassigned_variable(self, assignment):
        unassigned_variables = [var for var in self.variables if var not in assignment]
        return min(unassigned_variables, key=lambda var: len(self.domains[var]))

    def ac3(self):
        queue = [(var, neighbor) for var in self.variables for neighbor in self.constraints[var]]

        while queue:
            (xi, xj) = queue.pop(0)
            if self.revise(xi, xj):
                if not self.domains[xi]:
                    return False  # Inconsistency detected
                for xk in self.constraints[xi]:
                    if xk != xj:
                        queue.append((xk, xi))
        return True

    def revise(self, xi, xj):
        revised = False
        for vi in list(self.domains[xi]):
            if not any(self.constraints(xi, xj, vi, vj) for vj in self.domains[xj]):
                self.domains[xi].remove(vi)
                revised = True
        return revised

    def backtracking_search(self):
        return self.backtrack({})

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment  # All variables are assigned, solution found

        variable = self.select_unassigned_variable(assignment)
        for value in self.domains[variable]:
            if self.is_consistent(variable, value, assignment):
                assignment[variable] = value
                if self.ac3():
                    result = self.backtrack(assignment)
                    if result is not None:
                        return result
                del assignment[variable]  # Backtrack

        return None

# Example usage for map coloring problem with CSP and AC-3
if __name__ == "__main__":
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {var: ['Red', 'Green', 'Blue'] for var in variables}

    def constraint_function(xi, xj, vi, vj):
        return vi != vj

    constraints = {
        'WA': [('NT', constraint_function), ('SA', constraint_function)],
        'NT': [('WA', constraint_function), ('SA', constraint_function), ('Q', constraint_function)],
        'SA': [('WA', constraint_function), ('NT', constraint_function), ('Q', constraint_function), ('NSW', constraint_function), ('V', constraint_function)],
        'Q': [('NT', constraint_function), ('SA', constraint_function), ('NSW', constraint_function)],
        'NSW': [('Q', constraint_function), ('SA', constraint_function), ('V', constraint_function)],
        'V': [('SA', constraint_function), ('NSW', constraint_function)],
        'T': []
    }

    map_coloring_csp = CSP(variables, domains, constraints)
    solution = map_coloring_csp.backtracking_search()

    if solution is not None:
        print("Map Coloring Solution:")
        for variable, color in solution.items():
            print(f"{variable}: {color}")
    else:
        print("No solution found.")
