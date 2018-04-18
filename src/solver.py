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

        self.canvas = Canvas(master, width=400, height=300)
        self.canvas.pack()

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
        self.drawCube()

    def startRandScramble(self):
        """Creates a randomly scrambled cube"""
        self.destroyInitButtons()
        self.rubik = Cube(scramble=True)
        self.showOptions()
        self.drawCube()

    def startSolved(self):
        """Starts the cube to solved state"""
        self.destroyInitButtons()
        self.rubik = Cube()
        self.showOptions()
        self.drawCube()

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
        self.drawCube()

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
        self.drawCube()

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
        self.drawCube()

    def resetCube(self):
        """Resets the cube to solved state"""
        self.rubik.reset(print_msg=True)
        self.drawCube()

    def randScramble(self):
        """Randomly scrambles the cube"""
        self.rubik = Cube(scramble=True)
        self.drawCube()

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

    def drawCube(self):
        """Displays cube in unfolded format (cross on its side)"""
        colors = {
            'o': 'orange',
            'g': 'green',
            'r': 'red',
            'b': 'blue',
            'w': 'white',
            'y': 'yellow'
        }
        mat = self.rubik.faces['u']
        for i in range(3):
            self.canvas.create_rectangle(90, 30 * i, 120, 30 + 30 * i,
                                         fill=colors[mat[i][0]])
            self.canvas.create_rectangle(120, 30 * i, 150, 30 + 30 * i,
                                         fill=colors[mat[i][1]])
            self.canvas.create_rectangle(150, 30 * i, 180, 30 + 30 * i,
                                         fill=colors[mat[i][2]])
        arr = ['l', 'f', 'r']
        for j in range(3):
            for i in range(3):
                mat = self.rubik.faces[arr[i]]
                self.canvas.create_rectangle(90 * i, 90 + 30 * j,
                    30 + 90 * i, 120 + 30 * j, fill=colors[mat[j][0]])
                self.canvas.create_rectangle(30 + 90 * i, 90 + 30 * j,
                    60 + 90 * i, 120 + 30 * j, fill=colors[mat[j][1]])
                self.canvas.create_rectangle(60 + 90 * i, 90 + 30 * j,
                    90 + 90 * i, 120 + 30 * j, fill=colors[mat[j][2]])
            mat = self.rubik.faces['b']
            self.canvas.create_rectangle(270, 90 + 30 * j, 300, 120 + 30 * j,
                                         fill=colors[mat[2 - j][2]])
            self.canvas.create_rectangle(300, 90 + 30 * j, 330, 120 + 30 * j,
                                         fill=colors[mat[2 - j][1]])
            self.canvas.create_rectangle(330, 90 + 30 * j, 360, 120 + 30 * j,
                                         fill=colors[mat[2 - j][0]])
        mat = self.rubik.faces['d']
        for i in range(3):
            self.canvas.create_rectangle(90, 180 + 30 * i, 120, 210 + 30 * i,
                                         fill=colors[mat[i][0]])
            self.canvas.create_rectangle(120, 180 + 30 * i, 150, 210 + 30 * i,
                                         fill=colors[mat[i][1]])
            self.canvas.create_rectangle(150, 180 + 30 * i, 180, 210 + 30 * i,
                                         fill=colors[mat[i][2]])


top = Tk()
my_gui = RubikSolverGUI(top)
top.minsize(600, 450)
top.mainloop()
