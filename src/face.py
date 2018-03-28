# Represents a face of the cube
class Face(object):

    def __init__(self, value):
        self.mat = [[value]*3 for i in range(3)]

    # Rotate face clockwise
    def rotate_clock(self):
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

    # Rotate face counterclockwise
    def rotate_counter(self):
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

    # Rotate face twice
    def rotate_2(self):
        self.mat[0][0], self.mat[2][2] = self.mat[2][2], self.mat[0][0]
        self.mat[0][2], self.mat[2][0] = self.mat[2][0], self.mat[0][2]
        self.mat[0][1], self.mat[2][1] = self.mat[2][1], self.mat[0][1]
        self.mat[1][0], self.mat[1][2] = self.mat[1][2], self.mat[1][0]

    def __eq__(self, other):
        for i in range(3):
            for j in range(3):
                if self.mat[i][j] != other.mat[i][j]:
                    return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __getitem__(self, key):
        return self.mat[key]

    def __setitem__(self, key, value):
        self.mat[key] = value