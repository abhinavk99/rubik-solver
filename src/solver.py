from tkinter import Tk, Label, Button, Canvas, StringVar, Entry
from cube import Cube

class RubikSolverGUI:
    def __init__(self, master):
        """Creates the GUI"""
        self.master = master
        master.title('Rubik Solver')

        self.label = Label(master, text='Rubik Solver')
        self.label.pack()

        self.rand_string_button = Button(master, text='Enter randomizer string', command=self.randStringEntry)
        self.rand_string_button.pack()

        self.rand_scramble_button = Button(master, text='Randomly scramble cube', command=self.randScramble)
        self.rand_scramble_button.pack()

        self.solved_button = Button(master, text='Start with solved cube', command=self.resetCube)
        self.solved_button.pack()

    def randStringEntry(self):
        """Sets up GUI for entering the randomizer string"""
        self.destroyInitButtons()
        self.string = StringVar()

        self.string_entry = Entry(self.master, width=100, textvariable=self.string)
        self.string_entry.pack()

        self.create_button = Button(self.master, text='Create', command=self.randStringCreate)
        self.create_button.pack()

    def randStringCreate(self):
        """Creates the cube with the randomizer string"""
        self.rubik = Cube(self.string.get())
        print(str(self.rubik))

    def randScramble(self):
        """Creates a randomly scrambled cube"""
        self.destroyInitButtons()
        self.rubik = Cube(scramble=True)
        print(str(self.rubik))

    def resetCube(self):
        """Resets the cube to solved state"""
        self.destroyInitButtons()
        self.rubik.reset()
        print(str(self.rubik))

    def destroyInitButtons(self):
        self.rand_string_button.destroy()
        self.rand_scramble_button.destroy()
        self.solved_button.destroy()

display_msg = """
Options:
1 to solve
2 to create new cube
3 to enter randomizer string
4 to check if cube is solved
5 to reset cube
6 to re-scramble cube
Anything else to exit"""

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


top = Tk()
my_gui = RubikSolverGUI(top)
top.minsize(400, 300)
top.mainloop()
