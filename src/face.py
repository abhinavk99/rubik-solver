# Represents a face of the cube
class Face(object):
    """Represents a Face on a Rubik's cube

    Users creating a Rubik's cube should use 6 of these to represent the
    sides of a cube
    """

    def __init__(self, value):
        """Creates a face with the given value

        Keyword arguments:
        value -- value on Face, should be o, g, r, b, w, or y per WCA regulation
        """
        self.mat = [[value]*3 for i in range(3)]

    def rotate_clock(self):
        """Rotates face clockwise"""
        temp = self.mat[0][0]
        self.mat[0][0] = self.mat[2][0]
        self.mat[2][0] = self.mat[2][2]
        self.mat[2][2] = self.mat[0][2]
        self.mat[0][2] = temp
        temp = self.mat[0][1]
        self.mat[0][1] = self.mat[1][0]
        self.mat[1][0] = self.mat[2][1]
        self.mat[2][1] = self.mat[1][2]
        self.mat[1][2] = temp

    def rotate_counter(self):
        """Rotates face counterclockwise"""
        temp = self.mat[0][0]
        self.mat[0][0] = self.mat[0][2]
        self.mat[0][2] = self.mat[2][2]
        self.mat[2][2] = self.mat[2][0]
        self.mat[2][0] = temp
        temp = self.mat[0][1]
        self.mat[0][1] = self.mat[1][2]
        self.mat[1][2] = self.mat[2][1]
        self.mat[2][1] = self.mat[1][0]
        self.mat[1][0] = temp

    def rotate_2(self):
        """Rotates face twice"""
        self.mat[0][0], self.mat[2][2] = self.mat[2][2], self.mat[0][0]
        self.mat[0][2], self.mat[2][0] = self.mat[2][0], self.mat[0][2]
        self.mat[0][1], self.mat[2][1] = self.mat[2][1], self.mat[0][1]
        self.mat[1][0], self.mat[1][2] = self.mat[1][2], self.mat[1][0]

    def __eq__(self, other):
        """Defines equality for a Face"""
        for i in range(3):
            for j in range(3):
                if self.mat[i][j] != other.mat[i][j]:
                    return False
        return True

    def __ne__(self, other):
        """Defines non-equality for a Face"""
        return not (self == other)

    def __getitem__(self, key):
        """Overloads array indexing for a Face to get values"""
        return self.mat[key]

    def __setitem__(self, key, value):
        """Overloads array indexing for a Face to set values"""
        self.mat[key] = value