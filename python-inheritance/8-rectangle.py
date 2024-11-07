#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.

Classes:
    Rectangle - A class used to represent a rectangle, inheriting from BaseGeometry.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from BaseGeometry.

    Methods:
        __init__(self, width, height) - Initializes a Rectangle with width and height.
        width(self) - Retrieves the width of the Rectangle.
        height(self) - Retrieves the height of the Rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with the specified width and
        height after validation.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height are not integers.
            ValueError: If width or height are <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

