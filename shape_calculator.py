class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        picture_width = ("*" * self.width) + "\n"
        picture = picture_width * self.height
        if self.width >= 50 or self.height >= 50:
            oversize = "Too big for picture."
            return oversize
        else:
            return picture

    def get_amount_inside(self, square):
        amount = self.get_area() // square.get_area()
        return amount

    def __str__(self):
        output = f"Rectangle(width={self.width}, height={self.height})"
        return output


class Square(Rectangle):
    side_length = 0

    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length

    def set_side(self, new_side_length):
        self.side_length = new_side_length
        super().set_height(new_side_length)
        super().set_width(new_side_length)

    def set_width(self, new_width):
        self.side_length = new_width

    def set_height(self, new_height):
        self.side_length = new_height

    def __str__(self):
        output = f"Square(side={self.side_length})"
        return output
