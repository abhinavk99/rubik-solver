#Represents a Rubik's cube
class Cube(object):
    solved_cube = {'l':[['o']*3 for i in range(3)],
                   'f':[['g']*3 for i in range(3)],
                   'r':[['r']*3 for i in range(3)],
                   'b':[['b']*3 for i in range(3)],
                   'u':[['w']*3 for i in range(3)],
                   'd':[['y']*3 for i in range(3)]}

    moves = ['l', 'l\'', 'l2', 'f', 'f\'', 'f2', 'r', 'r\'', 'r2',
             'b', 'b\'', 'b2', 'u', 'u\'', 'u2', 'd', 'd\'', 'd2'] 

    def __init__(self, randomizer=None):
        self.dict = {'l':[['o']*3 for i in range(3)],
                     'f':[['g']*3 for i in range(3)],
                     'r':[['r']*3 for i in range(3)],
                     'b':[['b']*3 for i in range(3)],
                     'u':[['w']*3 for i in range(3)],
                     'd':[['y']*3 for i in range(3)]}
        self.parse_randomizer(randomizer)

    #Goes through the randomizer string to change the cube state move by move
    def parse_randomizer(self, randomizer):
        #Checks if the randomizer String is valid by WCA standards
        if randomizer is not None:
            if isinstance(randomizer, str) and len(randomizer) is not 0:
                lower = randomizer.lower()
                trans = lower.translate(dict.fromkeys(map(ord, ' \'lfrbud2'), None))
                if len(trans) is 0:
                    arr = randomizer.strip().split(' ')
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
                        elif move == 'r':
                            self.r()
                        elif move == 'r\'':
                            self.r_prime()
                        elif move == 'r2':
                            self.r_2()
                        elif move == 'b':
                            self.b()
                        elif move == 'b\'':
                            self.b_prime()
                        elif move == 'b2':
                            self.b_2()
                        elif move == 'u':
                            self.u()
                        elif move == 'u\'':
                            self.u_prime()
                        elif move == 'u2':
                            self.u_2()
                        elif move == 'd':
                            self.d()
                        elif move == 'd\'':
                            self.d_prime()
                        elif move == 'd2':
                            self.d_2()
                        else:
                            print('Reverted to solved state as randomizer could not be parsed correctly')
                            self.dict = dict(Cube.solved_cube)
                else:
                    print('Cube state unchanged as randomizer was not in valid WCA format') 
            else:
                print('Cube state unchanged as no randomizer was passed in')

    #Solve the cube
    def solve(self):
        self.__rec_solve(15, [])

    #Uses depth first search with a maximum iteration depth to find a solution
    def __rec_solve(self, num_left, moves_taken):
        if self.check_solved():
            self.__print_moves(moves_taken)
            return True
        elif num_left == 0:
            return False
        else:
            for move in Cube.moves:
                self.parse_randomizer(move)
                moves_taken.append(move)
                if self.__rec_solve(num_left - 1, moves_taken):
                    return True
                moves_taken.pop()
                #Revert the move just taken to try the next move
                if move[-1:] == '\'':
                    self.parse_randomizer(move[:1])
                elif move[-1:] == '2':
                    self.parse_randomizer(move)
                else:
                    self.parse_randomizer(move + '\'')

    #Checks if cube is solved
    def check_solved(self):
        faces = ['l', 'f', 'r', 'b', 'u', 'd']
        for i in range(3):
            for j in range(3):
                for k in range(6):
                    if self.dict[faces[k]][i][j] != Cube.solved_cube[faces[k]][i][j]:
                        return False
        return True

    #Prints contents of moves list
    def __print_moves(self, moves_taken):
        if len(moves_taken) == 0:
            print('Already in solved state')
        else:
            print('Moves needed to solve: ', end='')
            for move in moves_taken:
                print(move, end=' ')
            print()

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

    # Moving right side of cube 
    def r(self):
        self.__rotate_clock('r')
        faces = ['u', 'f', 'd', 'b']
        temp_arr = []
        for i in range(3):
            temp_arr.append(self.dict['u'][i][2])
        for j in range(3):
            for i in range(3):
                self.dict[faces[j]][i][2] = self.dict[faces[j + 1]][i][2]
        for i in range(3):
            self.dict['b'][i][2] = temp_arr[i]

    def r_prime(self):
        self.__rotate_counter('r')
        faces = ['u', 'b', 'd', 'f']
        temp_arr = []
        for i in range(3):
            temp_arr.append(self.dict['u'][i][2])
        for j in range(3):
            for i in range(3):
                self.dict[faces[j]][i][2] = self.dict[faces[j + 1]][i][2]
        for i in range(3):
            self.dict['f'][i][2] = temp_arr[i]

    def r_2(self):
        self.__rotate__2('r')
        for i in range(3):
            self.dict['u'][i][2], self.dict['d'][i][2] = self.dict['d'][i][2], self.dict['u'][i][2]
            self.dict['f'][i][2], self.dict['b'][i][2] = self.dict['b'][i][2], self.dict['f'][i][2]

    # Moving back side of cube  
    def b(self):
        self.__rotate_clock('b')
        temp_arr = list(self.dict['u'][0])
        for i in range(3):
            self.dict['u'][0][i] = self.dict['r'][i][2]
        for i in range(3):
            self.dict['r'][i][2] = self.dict['d'][2][2 - i]
        for i in range(3):
            self.dict['d'][2][2 - i] = self.dict['l'][2 - i][0]
        for i in range(3):
            self.dict['l'][2 - i][0] = temp_arr[i]

    def b_prime(self):
        self.__rotate_counter('b')
        temp_arr = list(self.dict['u'][0])
        for i in range(3):
            self.dict['u'][0][i] = self.dict['l'][2 - i][0]
        for i in range(3):
            self.dict['l'][2 - i][0] = self.dict['d'][2][2 - i]
        for i in range(3):
            self.dict['d'][2][2 - i] = self.dict['r'][i][2]
        for i in range(3):
            self.dict['r'][i][2] = temp_arr[i]

    def b_2(self):
        self.__rotate__2('b')
        for i in range(3):
            self.dict['u'][0][i], self.dict['d'][2][2 - i] = self.dict['d'][2][2 - i], self.dict['u'][0][i]
            self.dict['r'][i][2], self.dict['l'][2 - i][0] = self.dict['l'][2 - i][0], self.dict['r'][i][2]

    # Moving upper side of cube 
    def u(self):
        self.__rotate_clock('u')
        temp = list(self.dict['f'][0])
        self.dict['f'][0] = list(self.dict['r'][0])
        for i in range(3):
            self.dict['r'][0][i] = self.dict['b'][2][2 - i]
        for i in range(3):
            self.dict['b'][2][2 - i] = self.dict['l'][0][2 - i]
        self.dict['l'][0] = temp

    def u_prime(self):
        self.__rotate_counter('u')
        temp = list(self.dict['f'][0])
        self.dict['f'][0] = list(self.dict['l'][0])
        for i in range(3):
            self.dict['l'][0][i] = self.dict['b'][2][2 - i]
        for i in range(3):
            self.dict['b'][2][i] = self.dict['r'][0][2 - i]
        self.dict['r'][0] = temp

    def u_2(self):
        self.__rotate__2('u')
        self.dict['l'][0], self.dict['r'][0] = self.dict['r'][0], self.dict['l'][0]
        for i in range(3):
            self.dict['f'][0][i], self.dict['b'][2][2 - i] = self.dict['b'][2][2 - i], self.dict['f'][0][i]

    # Moving down side of cube  
    def d(self):
        self.__rotate_clock('d')
        temp = list(self.dict['f'][2])
        self.dict['f'][2] = list(self.dict['l'][2])
        for i in range(3):
            self.dict['l'][2][i] = self.dict['b'][0][2 - i]
        for i in range(3):
            self.dict['b'][0][2 - i] = self.dict['r'][2][i]
        self.dict['r'][2] = temp

    def d_prime(self):
        self.__rotate_counter('d')
        temp = list(self.dict['f'][2])
        self.dict['f'][2] = list(self.dict['r'][2])
        for i in range(3):
            self.dict['r'][2][i] = self.dict['b'][0][2 - i]
        for i in range(3):
            self.dict['b'][0][2 - i] = self.dict['l'][2][i]
        self.dict['l'][2] = temp

    def d_2(self):
        self.__rotate__2('d')
        self.dict['l'][2], self.dict['r'][2] = self.dict['r'][2], self.dict['l'][2]
        for i in range(3):
            self.dict['f'][2][i], self.dict['b'][0][2 - i] = self.dict['b'][0][2 - i], self.dict['f'][2][i]

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
    rubik = Cube(input('Enter cube randomizer string in WCA format: '))
    rubik.display()
    print('\nOptions:\n1 to solve\n2 to create new cube\n3 to enter randomizer string\n4 to check if cube is solved')
    print('Anything else to exit')
    choice = input('Enter input here: ')
    while (choice == '1' or choice == '2' or choice == '3' or choice == '4'):
        print()
        if choice == '1':
            rubik.solve()
        elif choice == '2':
            rubik = Cube(input('Enter cube randomizer string in WCA format: '))
        elif choice == '3':
            rubik.parse_randomizer(input('Enter cube randomizer string in WCA format: '))
        else:
            if rubik.check_solved():
                print('Cube is solved.')
            else:
                print('Cube is not solved.')
        rubik.display()
        print('\nOptions:\n1 to solve\n2 to create new cube\n3 to enter randomizer string\n4 to check if cube is solved')
        print('Anything else to exit')
        choice = input('Enter input here: ')

if __name__ == '__main__':
    main()
