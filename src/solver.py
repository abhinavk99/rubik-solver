from cube import Cube

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
