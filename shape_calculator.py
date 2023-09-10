class Rectangle:
    def __init__(self, width, height):
        # Initialize a Rectangle with given width and height
        self.width = width
        self.height = height

    def __str__(self):
        # Define a string representation of the Rectangle
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        # Set the width of the Rectangle
        self.width = width

    def set_height(self, height):
        # Set the height of the Rectangle
        self.height = height

    def get_area(self):
        # Calculate and return the area of the Rectangle
        return self.width * self.height

    def get_perimeter(self):
        # Calculate and return the perimeter of the Rectangle
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # Calculate and return the diagonal length of the Rectangle
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # Create a string representation of the Rectangle as a picture
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        rectangle = ("*" * self.width + "\n") * self.height
        return rectangle

    def get_amount_inside(self, shape):
        # Calculate and return the number of smaller shapes that fit inside the Rectangle
        max_width = self.width // shape.width
        max_height = self.height // shape.height
        return max_width * max_height


class Square(Rectangle):
    def __init__(self, side):
        # Initialize a Square with a side length (sets both width and height)
        super().__init__(side, side)

    def __str__(self):
        # Define a string representation of the Square
        return f"Square(side={self.width})"

    def set_side(self, side):
        # Set the side length of the Square (updates both width and height)
        self.width = side
        self.height = side

    def set_width(self, side):
        # Override the set_width method to update both width and height
        self.width = side
        self.height = side

    def set_height(self, side):
        # Override the set_height method to update both width and height
        self.width = side
        self.height = side
