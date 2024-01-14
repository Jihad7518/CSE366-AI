class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}

    def is_consistent(self, variable, value, assignment):
        for neighbor in self.constraints[variable]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def select_unassigned_variable(self, assignment):
        unassigned_variables = [var for var in self.variables if var not in assignment]
        return min(unassigned_variables, key=lambda var: len(self.domains[var]))

    def order_domain_values(self, variable, assignment):
        return sorted(self.domains[variable], key=lambda val: sum(1 for neighbor in self.constraints[variable] if neighbor not in assignment and val in self.domains[neighbor]))

    def improved_backtracking(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment  # All variables are assigned, solution found

        variable = self.select_unassigned_variable(assignment)
        ordered_domain = self.order_domain_values(variable, assignment)

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


# Example usage for map coloring problem
if __name__ == "__main__":
    # Variables represent regions, and domains represent possible colors
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {var: ['Red', 'Green', 'Blue'] for var in variables}

    # Constraints represent neighboring regions
    constraints = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    map_coloring_csp = MapColoringCSP(variables, domains, constraints)
    solution = map_coloring_csp.solve()

    if solution is not None:
        print("Map Coloring Solution:")
        for variable, color in solution.items():
            print(f"{variable}: {color}")
    else:
        print("No solution found.")

