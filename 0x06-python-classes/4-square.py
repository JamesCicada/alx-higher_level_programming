#!/usr/bin/python3

"""Define a Square Class"""

class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Init a new Square.

        Args: size (int): size of the new square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    
    @property
    def size(self):
        """Getter and Setter for the current size of the square."""
        return (self.__size)

    @size.setter
    def area(self):
        """Returns the area of the current square."""
        return (self.__size**2)
