#!/usr/bin/python3
"""
This module defines a BaseGeometry class with methods for validation and area calculation.
"""

class BaseGeometry:
    """
    A class used to represent the base for geometric shapes.
    It contains methods for validation and calculating the area.
    """

    def area(self):
        """
        Raises an exception with the message 'area() is not implemented'.
        This method is meant to be overridden in subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the value is a positive integer.

        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
