import random
from face import Face

#Represents a Rubik's cube
class Cube(object):
    """Represents a Rubik's cube

    Has capabilities of random scrambling, scrambling based on user input,
    and solving the cube
    """

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
        """Creates a Rubik's cube

        Keyword arguments:
        randomizer -- move string to scramble the cube with (default None)
        scramble -- whether to scramble cube (default False)
        """
        if scramble:
            self.scramble()
        else:
            self.reset()
            self.parse_randomizer(randomizer)

    # Resets cube to solved state
    def reset(self, print_msg=False):
        """Resets the cube to solved state

        Keyword arguments:
        print_msg -- whether to print that cube was reset (default False)
        """
        self.faces = {
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
        """Scrambles the cube and prints the random moves taken"""
        self.reset()
        scramble_length = random.randint(5, 15)
        scramble_moves = random.choices(Cube.moves, k=scramble_length)
        scramble_str = ' '.join(scramble_moves)
        self.parse_randomizer(scramble_str)
        print(scramble_str)

    def parse_randomizer(self, randomizer):
        """Does each move in the move string on the cube"""
        # Checks if the randomizer String is valid by WCA standards
        if randomizer is not None:
            if isinstance(randomizer, str) and len(randomizer) is not 0:
                lower = randomizer.lower()
                # Removes all characters that should be in the move string
                trans = lower.translate(dict.fromkeys(map(ord, ' \'lfrbud2'),
                                                      None))
                # Move string is correct if the translated string is empty
                if len(trans) is 0:
                    arr = lower.strip().split(' ')
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

    def solve(self):
        """Solves the cube"""
        self._rec_solve(15, [])

    def _rec_solve(self, num_left, moves_taken):
        """Recursively solves the cube

        Implementation is a depth first search with a maximum iteration depth
        """
        if self.check_solved():
            self._print_moves(moves_taken)
            return True
        elif num_left == 0:
            return False
        else:
            for move in Cube.moves:
                #Take a move from the list of moves
                self.parse_randomizer(move)
                moves_taken.append(move)
                if self._rec_solve(num_left - 1, moves_taken):
                    return True
                moves_taken.pop()
                # Revert the move just taken to try the next move
                if move[-1:] == '\'':
                    self.parse_randomizer(move[:1])
                elif move[-1:] == '2':
                    self.parse_randomizer(move)
                else:
                    self.parse_randomizer(move + '\'')

    def check_solved(self):
        """Checks if cube is solved"""
        faces = ['l', 'f', 'r', 'b', 'u', 'd']
        for face in faces:
            if self.faces[face] != Cube.solved_cube[face]:
                return False
        return True

    def _print_moves(self, moves_taken):
        """Prints contents of moves list"""
        if len(moves_taken) == 0:
            print('Already in solved state')
        else:
            print('Moves needed to solve: ', end='')
            for move in moves_taken:
                print(move, end=' ')
            print()

    def l(self):
        """Moves left side of cube clockwise"""
        self.faces['l'].rotate_clock()
        faces = ['u', 'b', 'd', 'f']
        temp_arr = []
        for i in range(3):
            temp_arr.append(self.faces['u'][i][0])
        for j in range(3):
            for i in range(3):
                self.faces[faces[j]][i][0] = self.faces[faces[j + 1]][i][0]
        for i in range(3):
            self.faces['f'][i][0] = temp_arr[i]

    def l_prime(self):
        """Moves left side of cube counterclockwise"""
        self.faces['l'].rotate_counter()
        faces = ['u', 'f', 'd', 'b']
        temp_arr = []
        for i in range(3):
            temp_arr.append(self.faces['u'][i][0])
        for j in range(3):
            for i in range(3):
                self.faces[faces[j]][i][0] = self.faces[faces[j + 1]][i][0]
        for i in range(3):
            self.faces['b'][i][0] = temp_arr[i]

    def l_2(self):
        """Moves left side of cube twice"""
        self.faces['l'].rotate_2()
        for i in range(3):
            self.faces['u'][i][0], self.faces['d'][i][0] = self.faces['d'][i][0], self.faces['u'][i][0]
            self.faces['f'][i][0], self.faces['b'][i][0] = self.faces['b'][i][0], self.faces['f'][i][0]

    def f(self):
        """Moves front side of cube clockwise"""
        self.faces['f'].rotate_clock()
        temp_arr = list(self.faces['u'][2])
        for i in range(3):
            self.faces['u'][2][i] = self.faces['l'][2 - i][2]
        for i in range(3):
            self.faces['l'][2 - i][2] = self.faces['d'][0][2 - i]
        for i in range(3):
            self.faces['d'][0][2 - i] = self.faces['r'][i][0]
        for i in range(3):
            self.faces['r'][i][0] = temp_arr[i]

    def f_prime(self):
        """Moves front side of cube counterclockwise"""
        self.faces['f'].rotate_counter()
        temp_arr = list(self.faces['u'][2])
        for i in range(3):
            self.faces['u'][2][i] = self.faces['r'][i][0]
        for i in range(3):
            self.faces['r'][i][0] = self.faces['d'][0][2 - i]
        for i in range(3):
            self.faces['d'][0][2 - i] = self.faces['l'][2 - i][2]
        for i in range(3):
            self.faces['l'][2 - i][2] = temp_arr[i]

    def f_2(self):
        """Moves front side of cube twice"""
        self.faces['f'].rotate_2()
        for i in range(3):
            self.faces['u'][2][i], self.faces['d'][0][2 - i] = self.faces['d'][0][2 - i], self.faces['u'][2][i]
            self.faces['r'][i][0], self.faces['l'][2 - i][2] = self.faces['l'][2 - i][2], self.faces['r'][i][0]

    def r(self):
        """Moves right side of cube clockwise"""
        self.faces['r'].rotate_clock()
        faces = ['u', 'f', 'd', 'b']
        temp_arr = []
        for i in range(3):
            temp_arr.append(self.faces['u'][i][2])
        for j in range(3):
            for i in range(3):
                self.faces[faces[j]][i][2] = self.faces[faces[j + 1]][i][2]
        for i in range(3):
            self.faces['b'][i][2] = temp_arr[i]

    def r_prime(self):
        """Moves right side of cube counterclockwise"""
        self.faces['r'].rotate_counter()
        faces = ['u', 'b', 'd', 'f']
        temp_arr = []
        for i in range(3):
            temp_arr.append(self.faces['u'][i][2])
        for j in range(3):
            for i in range(3):
                self.faces[faces[j]][i][2] = self.faces[faces[j + 1]][i][2]
        for i in range(3):
            self.faces['f'][i][2] = temp_arr[i]

    def r_2(self):
        """Moves right side of cube twice"""
        self.faces['r'].rotate_2()
        for i in range(3):
            self.faces['u'][i][2], self.faces['d'][i][2] = self.faces['d'][i][2], self.faces['u'][i][2]
            self.faces['f'][i][2], self.faces['b'][i][2] = self.faces['b'][i][2], self.faces['f'][i][2]

    def b(self):
        """Moves back side of cube clockwise"""
        self.faces['b'].rotate_clock()
        temp_arr = list(self.faces['u'][0])
        for i in range(3):
            self.faces['u'][0][i] = self.faces['r'][i][2]
        for i in range(3):
            self.faces['r'][i][2] = self.faces['d'][2][2 - i]
        for i in range(3):
            self.faces['d'][2][2 - i] = self.faces['l'][2 - i][0]
        for i in range(3):
            self.faces['l'][2 - i][0] = temp_arr[i]

    def b_prime(self):
        """Moves back side of cube counterclockwise"""
        self.faces['b'].rotate_counter()
        temp_arr = list(self.faces['u'][0])
        for i in range(3):
            self.faces['u'][0][i] = self.faces['l'][2 - i][0]
        for i in range(3):
            self.faces['l'][2 - i][0] = self.faces['d'][2][2 - i]
        for i in range(3):
            self.faces['d'][2][2 - i] = self.faces['r'][i][2]
        for i in range(3):
            self.faces['r'][i][2] = temp_arr[i]

    def b_2(self):
        """Moves back side of cube twice"""
        self.faces['b'].rotate_2()
        for i in range(3):
            self.faces['u'][0][i], self.faces['d'][2][2 - i] = self.faces['d'][2][2 - i], self.faces['u'][0][i]
            self.faces['r'][i][2], self.faces['l'][2 - i][0] = self.faces['l'][2 - i][0], self.faces['r'][i][2]

    def u(self):
        """Moves upper side of cube clockwise"""
        self.faces['u'].rotate_clock()
        temp = list(self.faces['f'][0])
        self.faces['f'][0] = list(self.faces['r'][0])
        for i in range(3):
            self.faces['r'][0][i] = self.faces['b'][2][2 - i]
        for i in range(3):
            self.faces['b'][2][2 - i] = self.faces['l'][0][2 - i]
        self.faces['l'][0] = temp

    def u_prime(self):
        """Moves upper side of cube counterclockwise"""
        self.faces['u'].rotate_counter()
        temp = list(self.faces['f'][0])
        self.faces['f'][0] = list(self.faces['l'][0])
        for i in range(3):
            self.faces['l'][0][i] = self.faces['b'][2][2 - i]
        for i in range(3):
            self.faces['b'][2][i] = self.faces['r'][0][2 - i]
        self.faces['r'][0] = temp

    def u_2(self):
        """Moves upper side of cube twice"""
        self.faces['u'].rotate_2()
        self.faces['l'][0], self.faces['r'][0] = self.faces['r'][0], self.faces['l'][0]
        for i in range(3):
            self.faces['f'][0][i], self.faces['b'][2][2 - i] = self.faces['b'][2][2 - i], self.faces['f'][0][i]

    def d(self):
        """Moves down side of cube clockwise"""
        self.faces['d'].rotate_clock()
        temp = list(self.faces['f'][2])
        self.faces['f'][2] = list(self.faces['l'][2])
        for i in range(3):
            self.faces['l'][2][i] = self.faces['b'][0][2 - i]
        for i in range(3):
            self.faces['b'][0][2 - i] = self.faces['r'][2][i]
        self.faces['r'][2] = temp

    def d_prime(self):
        """Moves down side of cube counterclockwise"""
        self.faces['d'].rotate_counter()
        temp = list(self.faces['f'][2])
        self.faces['f'][2] = list(self.faces['r'][2])
        for i in range(3):
            self.faces['r'][2][i] = self.faces['b'][0][2 - i]
        for i in range(3):
            self.faces['b'][0][2 - i] = self.faces['l'][2][i]
        self.faces['l'][2] = temp

    def d_2(self):
        """Moves down side of cube twice"""
        self.faces['d'].rotate_2()
        self.faces['l'][2], self.faces['r'][2] = self.faces['r'][2], self.faces['l'][2]
        for i in range(3):
            self.faces['f'][2][i], self.faces['b'][0][2 - i] = self.faces['b'][0][2 - i], self.faces['f'][2][i]

    def __str__(self):
        """Displays cube in unfolded format (cross on its side)"""
        res = ''
        mat = self.faces['u']
        for i in range(3):
            res += ('      ' + mat[i][0] + ' ' +
                    mat[i][1] + ' ' + mat[i][2] + '\n')
        arr = ['l', 'f', 'r']
        for j in range(3):
            for i in range(3):
                mat = self.faces[arr[i]]
                res += (mat[j][0] + ' ' + mat[j][1] + ' ' + mat[j][2] + ' ')
            mat = self.faces['b']
            res += (mat[2 - j][2] + ' ' + mat[2 - j]
                    [1] + ' ' + mat[2 - j][0] + '\n')
        mat = self.faces['d']
        for i in range(3):
            res += ('      ' + mat[i][0] + ' ' +
                    mat[i][1] + ' ' + mat[i][2] + '\n')
        return res
