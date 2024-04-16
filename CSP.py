from collections import deque
from typing import Callable, List, Tuple


class CSP(object):
    """
    Represents a Constraint Satisfaction Problem (CSP).

    Attributes:
        variables (dict): A dictionary that maps variables to their domains.
        constraints (list): A list of constraints in the form of [constraint_func, *variables].
        unassigned_var (list): A list of unassigned variables.
        var_constraints (dict): A dictionary that maps variables to their associated constraints.

    Methods:
        add_constraint(constraint_func, variables): Adds a constraint to the CSP.
        add_variable(variable, domain): Adds a variable to the CSP with its domain.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes a Constraint Satisfaction Problem (CSP) object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            variables (dict): A dictionary to store the variables of the CSP.
            constraints (list): A list to store the constraints of the CSP.
            unassigned_var (list): A list to store the unassigned variables of the CSP.
            var_constraints (dict): A dictionary to store the constraints associated with each variable.
            assignments (dict): A dictionary to store the assignments of the CSP.
        """
        self.variables = {}
        self.constraints = []
        self.unassigned_var = []
        self.var_constraints = {}
        self.assignments = {}
        self.assignments_number = 0

    def add_constraint(self, constraint_func: Callable, variables: List[str]) -> None:
        """
        Adds a constraint to the CSP.

        Args:
            constraint_func (function): The constraint function to be added.
            variables (list): The variables involved in the constraint.

        Returns:
            None
        """
        "*** YOUR CODE HERE ***"

    def add_variable(self, variable: str, domain: List) -> None:
        """
        Adds a variable to the CSP with its domain.

        Args:
            variable: The variable to be added.
            domain: The domain of the variable.

        Returns:
            None
        """
        "*** YOUR CODE HERE ***"

    def assign(self, variable: str, value) -> bool:
        """
        Assigns a value to a variable in the CSP.

        Args:
            variable (str): The variable to be assigned.
            value: The value to be assigned to the variable.

        Returns:
            bool: True if the assignment is consistent with the constraints, False otherwise.
        """
        "*** YOUR CODE HERE ***"

    def is_consistent(self, variable: str, value) -> bool:
        """
        Checks if assigning a value to a variable violates any constraints.

        Args:
            variable (str): The variable to be assigned.
            value: The value to be assigned to the variable.

        Returns:
            bool: True if the assignment is consistent with the constraints, False otherwise.
        """
        "*** YOUR CODE HERE ***"

    def is_complete(self) -> bool:
        """
        Checks if the CSP is complete, i.e., all variables have been assigned.

        Returns:
            bool: True if the CSP is complete, False otherwise.
        """
        "*** YOUR CODE HERE ***"

    def is_assigned(self, variable: str) -> bool:
        """
        Checks if a variable has been assigned a value.

        Args:
            variable (str): The variable to check.

        Returns:
            bool: True if the variable has been assigned, False otherwise.
        """
        "*** YOUR CODE HERE ***"

    def unassign(self, removed_values_from_domain: List[Tuple[str, any]], variable: str) -> None:
        """
        Unassign a variable and restores its domain values.

        Args:
            removed_values_from_domain (list): A list of domain values to be restored.
            variable (str): The variable to be unassigned.

        Returns:
            None
        """
        "*** YOUR CODE HERE ***"
