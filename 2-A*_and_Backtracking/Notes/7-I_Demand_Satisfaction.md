# I Demand Satisfaction

<img src="https://i.redd.it/o2y6ecet12q81.gif" width="400px" />

## Overview

Let's demonstrate the backtracking concept by implementing a basic satisfiability solver.

As with our previous search programs, the challenge isn't in deciding to use backtracking, it's in thinking about how to represent the solution and encode the constraints. Ideally, we want achieve a few things with our representation:

- It's easy to evaluate the constraints and determine if a candidate assignment is in conflict

- It's easy to select the next unassigned variable; if you're doing optimizations, you want to be able to identify the most contrained variable
  
- If we're using contraint propagation, it should be easy to identify how a variable's value set changes based on the assignment of a neighbor variable

For this problem, we're going to focus on the basic backtracking solver. You can experiment with adding optimizations as part of the deliverable assignment if you need to.

## Solution representation

The problem has *n* boolean variables. Let each clause in the 3-CNF-SAT form be represented as a tuple, where each entry in the tuple corresponds to the index of a variable. Negative indices correspond to logical negations. For example, the tuple `(-1, 3, -4)` corresponds to the clause

$$ (\lnot x_1 \vee x_3 \vee \lnot x_4) $$

The set of clauses is implemented as a list of tuples. For example, the list
```
[(-2, 4, 5), (1, -3, 4), (1, 2, -3)]
```
corresponds to the formula

$$(\lnot x_2 \vee x_4 \vee x_5) \wedge (x_1 \vee \lnot x_3 \vee x_4) \wedge (x_1 \vee x_2 \vee \lnot x_3) $$

Notice that this scheme uses **1-based indexing**. There is no *x*<sub>0</sub> variable because we couldn't use 0 and -0 to distinguish between its positive and negative versions.

Each variable can be in one of three states: `True`, `False`, or currently unassigned.

## Basic procedure

The backtracking search chooses one variable and tries to set it `True`, then recursively continues the search to find the next variable. If that path fails, the method backtracks and tries assigning `False`. T

he basic solution routine is below. Notice that it starts by checking the current assignment for a conflict, discussed in more detail below, and abandons the search path immediately if one is found. This version doesn't do any fancy variable choosing, it just works through the variables in numerical order.

```
def solve(clauses, n_vars, assignment=None):
    """
    Pure backtracking SAT solver.
    
    Args:
        clauses: list of tuples, each containing 3 signed integers
        n_vars: number of variables
        assignment: current partial assignment (used internally)
    
    Returns:
        dict mapping variable -> bool if satisfiable, None otherwise
    """
    if assignment is None:
        assignment = {}
    
    # Pruning: check for conflict before going deeper
    if has_conflict(clauses, assignment):
        return None
    
    # Base case: all variables assigned
    if len(assignment) == n_vars:
        return assignment.copy()
    
    # Choose next unassigned variable (simple: pick smallest index)
    var = None
    for v in range(1, n_vars + 1):
        if v not in assignment:
            var = v
            break
    
    # Try assigning True
    assignment[var] = True
    result = solve(clauses, n_vars, assignment)
    if result is not None:
        return result
    
    # Try assigning False
    assignment[var] = False
    result = solve(clauses, n_vars, assignment)
    if result is not None:
        return result
    
    # Backtrack: undo assignment
    del assignment[var]
    return None
```

The `has_conflict` method is the key to checking if a variable assignment is valid. Recall that the 3-CNF form requires that every clause evaluate to `True`, so if we ever find an assignment that makes any clause `False`, we know that the current path has a conflict. The functions below carry out the checking actions:

- `has_conflict` checks for any clause that evaluates to `False` in the current assignment
- `evaluate_clause` checks the three literals for a given clause. If any literal evaluates to `True`, the clause is satisfied. If all variables have been assigned and all three literals evaluate to `False`, then the clause is also `False`.
- `evaluate_literal` gets the value of an individual literal, negating it if necessary

```
def evaluate_literal(literal, assignment):
    """Evaluate a literal. Returns True, False, or None if unassigned."""
    var = abs(literal)
    if var not in assignment:
        return None
    value = assignment[var]
    return value if literal > 0 else not value

def evaluate_clause(clause, assignment):
    """
    Evaluate a clause under partial assignment.
    Returns:
        True  - satisfied (at least one literal is true)
        False - conflict (all literals are false)
        None  - undetermined (no true literals, some unassigned)
    """
    has_unassigned = False
    for literal in clause:
        val = evaluate_literal(literal, assignment)
        if val is True:
            return True
        if val is None:
            has_unassigned = True
    return None if has_unassigned else False


def has_conflict(clauses, assignment):
    """Check if any clause is falsified."""
    for clause in clauses:
        if evaluate_clause(clause, assignment) is False:
            return True
    return False
```

## Solution

Here's the complete solution, including an example in the `main` part. It uses a dictionary to store the variables using 1-based indexing.

```
"""
3-CNF-SAT Solver using Pure Backtracking

Representation:
- Variables use 1-based indexing
- Literals: positive int = variable, negative int = negated variable
- Clauses: tuples of 3 literals
- Assignment: dict mapping variable index -> bool (unassigned = absent)
"""


def evaluate_literal(literal, assignment):
    """Evaluate a literal. Returns True, False, or None if unassigned."""
    var = abs(literal)
    if var not in assignment:
        return None
    value = assignment[var]
    return value if literal > 0 else not value


def evaluate_clause(clause, assignment):
    """
    Evaluate a clause under partial assignment.
    Returns:
        True  - satisfied (at least one literal is true)
        False - conflict (all literals are false)
        None  - undetermined (no true literals, some unassigned)
    """
    has_unassigned = False
    for literal in clause:
        val = evaluate_literal(literal, assignment)
        if val is True:
            return True
        if val is None:
            has_unassigned = True
    return None if has_unassigned else False


def has_conflict(clauses, assignment):
    """Check if any clause is falsified."""
    for clause in clauses:
        if evaluate_clause(clause, assignment) is False:
            return True
    return False


def solve(clauses, n_vars, assignment=None):
    """
    Pure backtracking SAT solver.
    
    Args:
        clauses: list of tuples, each containing 3 signed integers
        n_vars: number of variables
        assignment: current partial assignment (used internally)
    
    Returns:
        dict mapping variable -> bool if satisfiable, None otherwise
    """
    if assignment is None:
        assignment = {}
    
    # Pruning: check for conflict before going deeper
    if has_conflict(clauses, assignment):
        return None
    
    # Base case: all variables assigned
    if len(assignment) == n_vars:
        return assignment.copy()
    
    # Choose next unassigned variable (simple: pick smallest index)
    var = None
    for v in range(1, n_vars + 1):
        if v not in assignment:
            var = v
            break
    
    # Try assigning True
    assignment[var] = True
    result = solve(clauses, n_vars, assignment)
    if result is not None:
        return result
    
    # Try assigning False
    assignment[var] = False
    result = solve(clauses, n_vars, assignment)
    if result is not None:
        return result
    
    # Backtrack: undo assignment
    del assignment[var]
    return None


def format_solution(solution, n_vars):
    """Format solution for display."""
    if solution is None:
        return "UNSATISFIABLE"
    parts = [f"x{i} = {solution[i]}" for i in range(1, n_vars + 1)]
    return "SATISFIABLE: " + ", ".join(parts)


def format_clause(clause):
    """Format a clause for display."""
    literals = []
    for lit in clause:
        if lit > 0:
            literals.append(f"x{lit}")
        else:
            literals.append(f"¬x{abs(lit)}")
    return "(" + " ∨ ".join(literals) + ")"


def verify_solution(clauses, solution):
    """Verify that a solution satisfies all clauses."""
    if solution is None:
        return False
    for clause in clauses:
        satisfied = False
        for lit in clause:
            var = abs(lit)
            val = solution[var]
            if (lit > 0 and val) or (lit < 0 and not val):
                satisfied = True
                break
        if not satisfied:
            return False
    return True


# =============================================================================
# Example Problem: 5 variables, 10 clauses
# =============================================================================

if __name__ == "__main__":
    n_vars = 5
    
    # 10 clauses over variables x1, x2, x3, x4, x5
    clauses = [
        (1, 2, 3),       # x1 ∨ x2 ∨ x3
        (-1, -2, 4),     # ¬x1 ∨ ¬x2 ∨ x4
        (-3, 4, 5),      # ¬x3 ∨ x4 ∨ x5
        (1, -4, -5),     # x1 ∨ ¬x4 ∨ ¬x5
        (-1, 3, -4),     # ¬x1 ∨ x3 ∨ ¬x4
        (2, -3, 5),      # x2 ∨ ¬x3 ∨ x5
        (-2, 4, -5),     # ¬x2 ∨ x4 ∨ ¬x5
        (1, -2, -3),     # x1 ∨ ¬x2 ∨ ¬x3
        (-1, 2, 5),      # ¬x1 ∨ x2 ∨ x5
        (3, -4, 5),      # x3 ∨ ¬x4 ∨ x5
    ]
    
    print("3-CNF-SAT Problem")
    print("=" * 50)
    print(f"Variables: {n_vars}")
    print(f"Clauses: {len(clauses)}")
    print()
    print("Formula:")
    for i, clause in enumerate(clauses, 1):
        print(f"  C{i}: {format_clause(clause)}")
    print()
    
    # Solve
    print("Solving with pure backtracking...")
    solution = solve(clauses, n_vars)
    
    print()
    print("Result:", format_solution(solution, n_vars))
    
    if solution:
        print()
        print("Verification:")
        for i, clause in enumerate(clauses, 1):
            vals = []
            for lit in clause:
                var = abs(lit)
                val = solution[var]
                actual = val if lit > 0 else not val
                vals.append(actual)
            status = "✓" if any(vals) else "✗"
            print(f"  C{i}: {format_clause(clause)} → {vals} → {status}")
        
        print()
        all_valid = verify_solution(clauses, solution)
        print(f"All clauses satisfied: {all_valid}")
```

## The DPLL algorithm

The canonical method for solving CNF-SAT problems is the Davis–Putnam–Logemann–Loveland (DPLL) algorithm, first developed in the early 1960s. The method uses backtracking search with two main optimizations: *literal elimination* and *unit propagation*.

**Literal elimination** If a variable occurs in only positive form throughout the formula, you can automatically assign it True. Likewise, if a variable only appears in negative form, you can automatically assign it False. Both cases allow you to remove the variable and any clauses containing it from the problem. For example, the formula 

$$ (x_1 \vee \lnot x_2 \vee x_3) \wedge (\lnot x_1 \vee \lnot x_2 \vee x_4) \wedge (\lnot x_3 \vee \lnot x_4 \vee x_5) $$

has only $$ \lnot x_2 $$ in every place where $$x_2$$ appears. Therefore, we can immediately set $$x_2$$ to False, which then satisfies the first two clauses.

**Unit propagation**. This optimization applies to clauses that have only one unassigned variable. Suppose that a clause has two literals that are `False` and one that's unassigned: you're forced to choose the assignment that makes the third literal True. Setting that variable may cause other clauses to become units, which can trigger additional forced variable assignments and quickly reduce the search space.

Unit propagation also helps identify infeasible paths. If you're forced to assign a variable to a certain value, but that assignment makes another clause False, then its infeasible and you can backtrack immediately.
