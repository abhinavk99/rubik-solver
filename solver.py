#Represents a Rubik's cube
class Cube(object):
    solved_cube = {'l':[['o']*3 for i in range(3)],
                   'f':[['g']*3 for i in range(3)],
                   'r':[['r']*3 for i in range(3)],
                   'b':[['b']*3 for i in range(3)],
                   'u':[['w']*3 for i in range(3)],
                   'd':[['y']*3 for i in range(3)]}

    def __init__(self, randomizer=None):
        self.dict = {'l':[['o']*3 for i in range(3)],
                     'f':[['g']*3 for i in range(3)],
                     'r':[['r']*3 for i in range(3)],
                     'b':[['b']*3 for i in range(3)],
                     'u':[['w']*3 for i in range(3)],
                     'd':[['y']*3 for i in range(3)]}

        #Checks if the randomizer String is valid by WCA standards
        if randomizer is not None:
            if isinstance(randomizer, str) and len(randomizer) is not 0:
                lower = randomizer.lower()
                trans = lower.translate(dict.fromkeys(map(ord, ' \'lfrbud2'), None))
                if len(trans) is 0:
                    self.__parse_randomizer(lower)
                else:
                    print('String must only have valid cubing moves and one ' +
                        'space between characters') 
            else:
                print('Must send in a String of length greater than 0')

    #Goes through the randomizer string to change the cube state move by move
    def __parse_randomizer(self, randomizer):
        arr = randomizer.split(' ')
        for move in arr:
            if move == 'l':
                self.l()
            elif move == 'l\'':
                self.l_prime()
            elif move == 'l2':
                self.l_2()
            elif move == 'f':
                self.f()
            elif move == 'f\'':
                self.f_prime()
            elif move == 'f2':
                self.f_2()
            # elif move == 'r':
            #     self.r()
            # elif move == 'r\'':
            #     self.r_prime()
            # elif move == 'r2':
            #     self.r_2()
            # elif move == 'b':
            #     self.b()
            # elif move == 'b\'':
            #     self.b_prime()
            # elif move == 'b2':
            #     self.l_2()
            # elif move == 'u':
            #     self.u()
            # elif move == 'u\'':
            #     self.u_prime()
            # elif move == 'u2':
            #     self.u_2()
            # elif move == 'd':
            #     self.d()
            # elif move == 'd\'':
            #     self.d_prime()
            # else:
            #     self.d_2()

    #Solve the cube
    # def solve(self):
    #     arr = ['l', 'l\'', 'l2', 'f', 'f\'', 'f2', 'r', 'r\'', 'r2',
    #            'b', 'b\'', 'b2', 'u', 'u\'', 'u2', 'd', 'd\'', 'd2']            

    #Moving left side of cube
    def l(self):
        self.__rotate_clock('l')
        faces = ['u', 'b', 'd', 'f']
        temp_arr = []
        for i in range(3):
            temp_arr.append(self.dict['u'][i][0])
        for j in range(3):
            for i in range(3):
                self.dict[faces[j]][i][0] = self.dict[faces[j + 1]][i][0]
        for i in range(3):
            self.dict['f'][i][0] = temp_arr[i]

    def l_prime(self):
        self.__rotate_counter('l')
        faces = ['u', 'f', 'd', 'b']
        temp_arr = []
        for i in range(3):
            temp_arr.append(self.dict['u'][i][0])
        for j in range(3):
            for i in range(3):
                self.dict[faces[j]][i][0] = self.dict[faces[j + 1]][i][0]
        for i in range(3):
            self.dict['b'][i][0] = temp_arr[i]

    def l_2(self):
        self.__rotate__2('l')
        for i in range(3):
            self.dict['u'][i][0], self.dict['d'][i][0] = self.dict['d'][i][0], self.dict['u'][i][0]
            self.dict['f'][i][0], self.dict['b'][i][0] = self.dict['b'][i][0], self.dict['f'][i][0]

    # Moving front side of cube
    def f(self):
        self.__rotate_clock('f')
        temp_arr = list(self.dict['u'][2])
        for i in range(3):
            self.dict['u'][2][i] = self.dict['l'][2 - i][2]
        for i in range(3):
            self.dict['l'][2 - i][2] = self.dict['d'][0][2 - i]
        for i in range(3):
            self.dict['d'][0][2 - i] = self.dict['r'][i][0]
        for i in range(3):
            self.dict['r'][i][0] = temp_arr[i]

    def f_prime(self):
        self.__rotate_counter('f')
        temp_arr = list(self.dict['u'][2])
        for i in range(3):
            self.dict['u'][2][i] = self.dict['r'][i][0]
        for i in range(3):
            self.dict['r'][i][0] = self.dict['d'][0][2 - i]
        for i in range(3):
            self.dict['d'][0][2 - i] = self.dict['l'][2 - i][2]
        for i in range(3):
            self.dict['l'][2 - i][2] = temp_arr[i]

    def f_2(self):
        self.__rotate__2('f')
        for i in range(3):
            self.dict['u'][2][i], self.dict['d'][0][2 - i] = self.dict['d'][0][2 - i], self.dict['u'][2][i]
            self.dict['r'][i][0], self.dict['l'][2 - i][2] = self.dict['l'][2 - i][2], self.dict['r'][i][0]

    # # Moving right side of cube 
    # def r(self):

    # def r_prime(self):

    # def r_2(self):

    # # Moving back side of cube  
    # def b(self):

    # def b_prime(self):

    # def b_2(self):

    # # Moving upper side of cube 
    # def u(self):

    # def u_prime(self):

    # def u_2(self):

    # # Moving down side of cube  
    # def d(self):

    # def d_prime(self):

    # def d_2(self):

    #Rotate face clockwise
    def __rotate_clock(self, face):
        temp = self.dict[face][0][0]
        self.dict[face][0][0] = self.dict[face][2][0]
        self.dict[face][2][0] = self.dict[face][2][2]
        self.dict[face][2][2] = self.dict[face][0][2]
        self.dict[face][0][2] = temp
        temp = self.dict[face][0][1]
        self.dict[face][0][1] = self.dict[face][1][0]
        self.dict[face][1][0] = self.dict[face][2][1]
        self.dict[face][2][1] = self.dict[face][1][2]
        self.dict[face][1][2] = temp

    #Rotate face counterclockwise
    def __rotate_counter(self, face):
        temp = self.dict[face][0][0]
        self.dict[face][0][0] = self.dict[face][0][2]
        self.dict[face][0][2] = self.dict[face][2][2]
        self.dict[face][2][2] = self.dict[face][2][0]
        self.dict[face][2][0] = temp
        temp = self.dict[face][0][1]
        self.dict[face][0][1] = self.dict[face][1][2]
        self.dict[face][1][2] = self.dict[face][2][1]
        self.dict[face][2][1] = self.dict[face][1][0]
        self.dict[face][1][0] = temp

    #Rotate face twice
    def __rotate__2(self, face):
        self.dict[face][0][0], self.dict[face][2][2] = self.dict[face][2][2], self.dict[face][0][0]
        self.dict[face][0][2], self.dict[face][2][0] = self.dict[face][2][0], self.dict[face][0][2]
        self.dict[face][0][1], self.dict[face][2][1] = self.dict[face][2][1], self.dict[face][0][1]
        self.dict[face][1][0], self.dict[face][1][2] = self.dict[face][1][2], self.dict[face][1][0]

    #Display cube in unfolded format (cross on its side)
    def display(self):
        mat = self.dict['u']
        for i in range(3):
            print('      ' + mat[i][0] + ' ' + mat[i][1] + ' ' + mat[i][2])
        arr = ['l', 'f', 'r']
        for j in range(3):
            for i in range(3):
                mat = self.dict[arr[i]]
                print(mat[j][0] + ' ' + mat[j][1] + ' ' + mat[j][2] + ' ', end='')
            mat = self.dict['b']
            print(mat[2 - j][2] + ' ' + mat[2 - j][1] + ' ' + mat[2 - j][0])
        mat = self.dict['d']
        for i in range(3):
            print('      ' + mat[i][0] + ' ' + mat[i][1] + ' ' + mat[i][2])

def main():
    rubik = Cube(input('Enter cube randomizer string in WCA format. '))
    rubik.display()

if __name__ == '__main__':
    main()