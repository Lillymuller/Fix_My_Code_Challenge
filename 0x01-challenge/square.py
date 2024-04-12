class Square:
    """
    Represents a square with a width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Square object.

        Args:
            width (int, optional): The width of the square. Defaults to 0.
            height (int, optional): The height of the square. Defaults to 0.
        """

        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (width * width).
        """

        return self.width * self.width

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            int: The perimeter of the square (2 * width + 2 * height).
        """

        return 2 * self.width + 2 * self.height

    def __str__(self):
        """
        Returns a string representation of the square in the format "width/height".

        Returns:
            str: The string representation of the square.
        """

        return f"{self.width}/{self.height}"


if __name__ == "__main__":
    square_object = Square(width=12, height=9)
    print(square_object)  # Output: 12/9
    print(square_object.area())  # Output: 144
    print(square_object.perimeter())  # Output: 42

