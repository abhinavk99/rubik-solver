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

        self.rand_scramble_button = Button(master, text='Randomly scramble cube', command=self.startRandScramble)
        self.rand_scramble_button.pack()

        self.solved_button = Button(master, text='Start with solved cube', command=self.startSolved)
        self.solved_button.pack()

    def randStringEntry(self):
        """Sets up GUI for entering the randomizer string"""
        self.destroyInitButtons()
        self.showEntry(self.randStringCreate)

    def randStringCreate(self):
        """Creates the cube with the randomizer string"""
        self.string_entry.destroy()
        self.create_button.destroy()
        self.rubik = Cube(self.string.get())
        self.showOptions()
        print(str(self.rubik))

    def startRandScramble(self):
        """Creates a randomly scrambled cube"""
        self.destroyInitButtons()
        self.rubik = Cube(scramble=True)
        self.showOptions()
        print(str(self.rubik))

    def startSolved(self):
        """Starts the cube to solved state"""
        self.destroyInitButtons()
        self.rubik = Cube()
        self.showOptions()
        print(str(self.rubik))

    def showOptions(self):
        """Shows options for acting on cube"""
        self.solve_button = Button(self.master, text='Solve cube', command=self.solveCube)
        self.solve_button.pack()

        self.new_scramble_button = Button(self.master, text='Enter move string for new cube', command=self.newCubeEntry)
        self.new_scramble_button.pack()

        self.add_moves_button = Button(self.master, text='Add moves to current cube', command=self.addMovesEntry)
        self.add_moves_button.pack()

        self.check_solved_button = Button(self.master, text='Check if cube is solved', command=self.checkCubeSolved)
        self.check_solved_button.pack()

        self.reset_button = Button(self.master, text='Reset cube', command=self.resetCube)
        self.reset_button.pack()

        self.rand_scramble_button = Button(self.master, text='Randomly scramble cube', command=self.randScramble)
        self.rand_scramble_button.pack()

    def solveCube(self):
        """Solves the cube"""
        self.rubik.solve()
        print(str(self.rubik))

    def newCubeEntry(self):
        """Sets up GUI to create a new cube with randomizer string"""
        self.destroyOptions()
        self.showEntry(self.randStringCreate)

    def addMovesEntry(self):
        """Sets up GUI to add moves to current cube with randomizer string"""
        self.destroyOptions()
        self.showEntry(self.addMoves)

    def addMoves(self):
        """Add moves to current cube with randomizer string"""
        self.string_entry.destroy()
        self.create_button.destroy()
        self.rubik.parse_randomizer(self.string.get())
        self.showOptions()
        print(str(self.rubik))

    def showEntry(self, method):
        """Sets up GUI for entering randomizer string"""
        self.string = StringVar()

        self.string_entry = Entry(self.master, width=100, textvariable=self.string)
        self.string_entry.pack()

        self.create_button = Button(self.master, text='Create', command=method)
        self.create_button.pack()

    def checkCubeSolved(self):
        """Checks if cube is solved"""
        print('Cube is ' + ('' if self.rubik.check_solved() else 'not ') + 'solved.')
        print(str(self.rubik))

    def resetCube(self):
        """Resets the cube to solved state"""
        self.rubik.reset(print_msg=True)
        print(str(self.rubik))

    def randScramble(self):
        """Randomly scrambles the cube"""
        self.rubik = Cube(scramble=True)
        print(str(self.rubik))

    def destroyInitButtons(self):
        """Destroys initial buttons"""
        self.rand_string_button.destroy()
        self.rand_scramble_button.destroy()
        self.solved_button.destroy()

    def destroyOptions(self):
        """Destroys options buttons"""
        self.solve_button.destroy()
        self.new_scramble_button.destroy()
        self.add_moves_button.destroy()
        self.check_solved_button.destroy()
        self.reset_button.destroy()
        self.rand_scramble_button.destroy()


top = Tk()
my_gui = RubikSolverGUI(top)
top.minsize(400, 300)
top.mainloop()
