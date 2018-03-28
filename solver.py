import random

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


#Represents a Rubik's cube
class Cube(object):
    solved_cube = {
        'l': Face('o'),
        'f': Face('g'),
        'r': Face('r'),
        'b': Face('b'),
        'u': Face('w'),
        'd': Face('y')
    }

    moves = ['l', 'l\'', 'l2', 'f', 'f\'', 'f2', 'r', 'r\'', 'r2',
             'b', 'b\'', 'b2', 'u', 'u\'', 'u2', 'd', 'd\'', 'd2']

    def __init__(self, randomizer=None, scramble=False):
        self.reset()
        if scramble:
            self.scramble()
        else:
            self.parse_randomizer(randomizer)

    # Resets cube to solved state
    def reset(self, print_msg=False):
        self.dict = {
            'l': Face('o'),
            'f': Face('g'),
            'r': Face('r'),
            'b': Face('b'),
            'u': Face('w'),
            'd': Face('y')
        }
        if print_msg:
            print('Cube was reset to solved state')

    # Randomly scrambles the cube
    def scramble(self):
        scramble_length = random.randint(5, 15)
        scramble_moves = random.choices(Cube.moves, k=scramble_length)
        scramble_str = ' '.join(scramble_moves)
        self.parse_randomizer(scramble_str)
        print(scramble_str)

    # Goes through the randomizer string to change the cube state move by move
    def parse_randomizer(self, randomizer):
        # Checks if the randomizer String is valid by WCA standards
        if randomizer is not None:
            if isinstance(randomizer, str) and len(randomizer) is not 0:
                lower = randomizer.lower()
                trans = lower.translate(dict.fromkeys(map(ord, ' \'lfrbud2'),
                                        None))
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
                            self.reset()
                else:
                    print('Cube state unchanged as randomizer was not invalid WCA format')
            else:
                print('Cube state unchanged as no randomizer was passed in')

    # Solve the cube
    def solve(self):
        self.__rec_solve(15, [])

    # Uses depth first search with a maximum iteration depth to find a solution
    def __rec_solve(self, num_left, moves_taken):
        if self.check_solved():
            self.__print_moves(moves_taken)
            return True
        elif num_left == 0:
            return False
        else:
            for move in Cube.moves:
                #Take a move from the list of moves
                self.parse_randomizer(move)
                moves_taken.append(move)
                if self.__rec_solve(num_left - 1, moves_taken):
                    return True
                moves_taken.pop()
                # Revert the move just taken to try the next move
                if move[-1:] == '\'':
                    self.parse_randomizer(move[:1])
                elif move[-1:] == '2':
                    self.parse_randomizer(move)
                else:
                    self.parse_randomizer(move + '\'')

    # Checks if cube is solved
    def check_solved(self):
        faces = ['l', 'f', 'r', 'b', 'u', 'd']
        # for i in range(3):
        #     for j in range(3):
        #         for k in range(6):
        #             curr_facelet = self.dict[faces[k]][i][j]
        #             solved_facelet = Cube.solved_cube[faces[k]][i][j]
        #             if curr_facelet != solved_facelet:
        #                 return False

        for face in faces:
            if self.dict[face] != Cube.solved_cube[face]:
                return False
        return True

    # Prints contents of moves list
    def __print_moves(self, moves_taken):
        if len(moves_taken) == 0:
            print('Already in solved state')
        else:
            print('Moves needed to solve: ', end='')
            for move in moves_taken:
                print(move, end=' ')
            print()

    # Moving left side of cube
    def l(self):
        self.dict['l'].rotate_clock()
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
        self.dict['l'].rotate_counter()
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
        self.dict['l'].rotate_2()
        for i in range(3):
            self.dict['u'][i][0], self.dict['d'][i][0] = self.dict['d'][i][0], self.dict['u'][i][0]
            self.dict['f'][i][0], self.dict['b'][i][0] = self.dict['b'][i][0], self.dict['f'][i][0]

    # Moving front side of cube
    def f(self):
        self.dict['f'].rotate_clock()
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
        self.dict['f'].rotate_counter()
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
        self.dict['f'].rotate_2()
        for i in range(3):
            self.dict['u'][2][i], self.dict['d'][0][2 - i] = self.dict['d'][0][2 - i], self.dict['u'][2][i]
            self.dict['r'][i][0], self.dict['l'][2 - i][2] = self.dict['l'][2 - i][2], self.dict['r'][i][0]

    # Moving right side of cube
    def r(self):
        self.dict['r'].rotate_clock()
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
        self.dict['r'].rotate_counter()
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
        self.dict['r'].rotate_2()
        for i in range(3):
            self.dict['u'][i][2], self.dict['d'][i][2] = self.dict['d'][i][2], self.dict['u'][i][2]
            self.dict['f'][i][2], self.dict['b'][i][2] = self.dict['b'][i][2], self.dict['f'][i][2]

    # Moving back side of cube
    def b(self):
        self.dict['b'].rotate_clock()
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
        self.dict['b'].rotate_counter()
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
        self.dict['b'].rotate_2()
        for i in range(3):
            self.dict['u'][0][i], self.dict['d'][2][2 - i] = self.dict['d'][2][2 - i], self.dict['u'][0][i]
            self.dict['r'][i][2], self.dict['l'][2 - i][0] = self.dict['l'][2 - i][0], self.dict['r'][i][2]

    # Moving upper side of cube
    def u(self):
        self.dict['u'].rotate_clock()
        temp = list(self.dict['f'][0])
        self.dict['f'][0] = list(self.dict['r'][0])
        for i in range(3):
            self.dict['r'][0][i] = self.dict['b'][2][2 - i]
        for i in range(3):
            self.dict['b'][2][2 - i] = self.dict['l'][0][2 - i]
        self.dict['l'][0] = temp

    def u_prime(self):
        self.dict['u'].rotate_counter()
        temp = list(self.dict['f'][0])
        self.dict['f'][0] = list(self.dict['l'][0])
        for i in range(3):
            self.dict['l'][0][i] = self.dict['b'][2][2 - i]
        for i in range(3):
            self.dict['b'][2][i] = self.dict['r'][0][2 - i]
        self.dict['r'][0] = temp

    def u_2(self):
        self.dict['u'].rotate_2()
        self.dict['l'][0], self.dict['r'][0] = self.dict['r'][0], self.dict['l'][0]
        for i in range(3):
            self.dict['f'][0][i], self.dict['b'][2][2 - i] = self.dict['b'][2][2 - i], self.dict['f'][0][i]

    # Moving down side of cube
    def d(self):
        self.dict['d'].rotate_clock()
        temp = list(self.dict['f'][2])
        self.dict['f'][2] = list(self.dict['l'][2])
        for i in range(3):
            self.dict['l'][2][i] = self.dict['b'][0][2 - i]
        for i in range(3):
            self.dict['b'][0][2 - i] = self.dict['r'][2][i]
        self.dict['r'][2] = temp

    def d_prime(self):
        self.dict['d'].rotate_counter()
        temp = list(self.dict['f'][2])
        self.dict['f'][2] = list(self.dict['r'][2])
        for i in range(3):
            self.dict['r'][2][i] = self.dict['b'][0][2 - i]
        for i in range(3):
            self.dict['b'][0][2 - i] = self.dict['l'][2][i]
        self.dict['l'][2] = temp

    def d_2(self):
        self.dict['d'].rotate_2()
        self.dict['l'][2], self.dict['r'][2] = self.dict['r'][2], self.dict['l'][2]
        for i in range(3):
            self.dict['f'][2][i], self.dict['b'][0][2 - i] = self.dict['b'][0][2 - i], self.dict['f'][2][i]

    # Display cube in unfolded format (cross on its side)
    def __str__(self):
        res = ''
        mat = self.dict['u']
        for i in range(3):
            res += ('      ' + mat[i][0] + ' ' + mat[i][1] + ' ' + mat[i][2] + '\n')
        arr = ['l', 'f', 'r']
        for j in range(3):
            for i in range(3):
                mat = self.dict[arr[i]]
                res += (mat[j][0] + ' ' + mat[j][1] + ' ' + mat[j][2] + ' ')
            mat = self.dict['b']
            res += (mat[2 - j][2] + ' ' + mat[2 - j][1] + ' ' + mat[2 - j][0] + '\n')
        mat = self.dict['d']
        for i in range(3):
            res += ('      ' + mat[i][0] + ' ' + mat[i][1] + ' ' + mat[i][2] + '\n')
        return res


display_msg = """\nOptions:\n1 to solve\n2 to create new cube
3 to enter randomizer string\n4 to check if cube is solved
5 to reset cube\n6 to re-scramble cube\nAnything else to exit"""

def main():
    ch = input("""Options:\n1 to enter randomizer string\n2 to randomly scramble cube
3 to start with solved cube\nEnter your choice here: """)
    if (ch in ('1', '2', '3')):
        if ch == '1':
            rubik = Cube(input('Enter cube randomizer string in WCA format: '))
        elif ch == '2':
            rubik = Cube(scramble=True)
        elif ch == '3':
            rubik = Cube()
        print(str(rubik))
        print(display_msg)
        choice = input('Enter input here: ')
        while (choice in ('1', '2', '3', '4', '5', '6')):
            print()
            if choice == '1':
                rubik.solve()
            elif choice == '2':
                rubik = Cube(input('Enter cube randomizer string in WCA format: '))
            elif choice == '3':
                rubik.parse_randomizer(input('Enter cube randomizer string in WCA format: '))
            elif choice == '4':
                if rubik.check_solved():
                    print('Cube is solved.')
                else:
                    print('Cube is not solved.')
            elif choice == '5':
                rubik.reset(print_msg=True)
            elif choice == '6':
                rubik.reset()
                rubik.scramble()
            print(str(rubik))
            print(display_msg)
            choice = input('Enter input here: ')
    else:
        print('Exiting - you must choose 1, 2, or 3')


if __name__ == '__main__':
    main()
