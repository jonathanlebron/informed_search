import math


class EightPuzzle():
    def __init__(self, puzzle, operator=None):
        self.n = int(math.sqrt(len(puzzle)))
        self.current_position = puzzle.index(0)
        self.puzzle = puzzle
        self.operator = operator

    def __str__(self):
        """
        Returns a string representing the state.
        """
        result = ""
        if self.operator is not None:
            result += "Operator: " + self.operator + "\n"
        for i in range(0, len(self.puzzle), self.n):
            result += "   ".join([str(d) for d in self.puzzle[i:i+self.n]]) + "\n"
        return result

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.puzzle == other.puzzle
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self == other
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(str(self.puzzle))

    def move_up(self):
        if self.current_position >= self.n:
            new_puzzle = self.swap(self.current_position, self.current_position-self.n)
            return EightPuzzle(new_puzzle, "moveUp")
        else:
            return False

    def move_down(self):
        if self.current_position < len(self.puzzle)-self.n:
            new_puzzle = self.swap(self.current_position, self.current_position+self.n)
            return EightPuzzle(new_puzzle, "moveDown")
        else:
            return False

    def move_left(self):
        if not (self.current_position % self.n == 0):
            new_puzzle = self.swap(self.current_position, self.current_position-1)
            return EightPuzzle(new_puzzle, "moveLeft")
        else:
            return False

    def move_right(self):
        if not ((self.current_position+1) % self.n == 0):
            new_puzzle = self.swap(self.current_position, self.current_position+1)
            return EightPuzzle(new_puzzle, "moveRight")
        else:
            return False

    def swap(self, tile1, tile2):
        new_puzzle = self.puzzle[:]
        new_puzzle[tile1], new_puzzle[tile2] = new_puzzle[tile2], new_puzzle[tile1]

        return new_puzzle

    def apply_operators(self):
        """
        Returns a list of valid successors to the current state.
        """
        all_ops = [self.move_up(), self.move_down(), self.move_left(), self.move_right()]
        return [op for op in all_ops if op]
