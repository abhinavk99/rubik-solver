import random
from face import Face

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
                        # Convert move string to function name
                        move = move.replace('\'', '_prime')
                        move = move.replace('2', '_2')
                        # Gets function from name, 0 returned if func not found
                        move_func = getattr(self, move, 0)
                        if move_func == 0:
                            print('Reverted to solved state as randomizer could not be parsed correctly')
                            self.reset()
                        else:
                            move_func()
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
            res += ('      ' + mat[i][0] + ' ' +
                    mat[i][1] + ' ' + mat[i][2] + '\n')
        arr = ['l', 'f', 'r']
        for j in range(3):
            for i in range(3):
                mat = self.dict[arr[i]]
                res += (mat[j][0] + ' ' + mat[j][1] + ' ' + mat[j][2] + ' ')
            mat = self.dict['b']
            res += (mat[2 - j][2] + ' ' + mat[2 - j]
                    [1] + ' ' + mat[2 - j][0] + '\n')
        mat = self.dict['d']
        for i in range(3):
            res += ('      ' + mat[i][0] + ' ' +
                    mat[i][1] + ' ' + mat[i][2] + '\n')
        return res
