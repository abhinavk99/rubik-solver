from cube import Cube

start_msg = """Options:
1 to enter randomizer string
2 to randomly scramble cube
3 to start with solved cube
Enter your choice here: """

display_msg = """
Options:
1 to solve
2 to create new cube
3 to enter randomizer string
4 to check if cube is solved
5 to reset cube
6 to re-scramble cube
Anything else to exit"""

cube_init = {
    '1': lambda: Cube(input('Enter cube randomizer string in WCA format: ')),
    '2': lambda: Cube(scramble=True),
    '3': lambda: Cube()
}

def display_info(rubik):
    """Shows information about cube's state and asks for next input"""
    print(str(rubik) + '\n' + display_msg)
    return input('Enter input here: ')

def main():
    """Creates a cube and does operations on it based on user input"""
    op = input(start_msg)
    if op in '123':
        # Create the cube from the options in the dict
        rubik = cube_init[op]()
        choice = display_info(rubik)
        while choice in '123456':
            print()
            if choice == '1':
                rubik.solve()
            elif choice == '2':
                rubik = Cube(input('Enter cube randomizer string in WCA format: '))
            elif choice == '3':
                rubik.parse_randomizer(input('Enter cube randomizer string in WCA format: '))
            elif choice == '4':
                print('Cube is ' + ('' if rubik.check_solved() else 'not ') + 'solved.')
            elif choice == '5':
                rubik.reset(print_msg=True)
            elif choice == '6':
                rubik.scramble()
            choice = display_info(rubik)
    else:
        print('Exiting - you must choose 1, 2, or 3')


if __name__ == '__main__':
    main()
