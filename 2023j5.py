WORD = input()
ROWS = int(input())
COLS = int(input())

grid = [list(input().split()) for _ in range(ROWS)]
word_count = 0

class root:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.visited = set()
        self.visited.add((r, c))
        self.turn = False
        self.next_letter = 1
    
    def check_up(self):
        if self.row > 0:
            if grid[self.row-1][self.col] == WORD[self.next_letter]:
                self.row -= 1
                self.visited.add((self.row, self.col))
                self.next_letter += 1
                return True
            else:
                return False

    def check_down(self):
        try:
            if grid[self.row+1][self.col] == WORD[self.next_letter]:
                self.row += 1
                self.visited.add((self.row, self.col))
                self.next_letter += 1
                return True
            else:
                return False
        except IndexError:
            return False
    
    def check_right(self):
        try:
            if grid[self.row][self.col+1] == WORD[self.next_letter]:
                self.col += 1
                self.visited.add((self.row, self.col))
                self.next_letter += 1
                return True
            else:
                return False
        except IndexError:
            return False
    
    def check_left(self):
        if self.col > 0:
            if grid[self.row][self.col-1] == WORD[self.next_letter]:
                self.col -= 1
                self.visited.add((self.row, self.col))
                self.next_letter += 1
                return True
            else:
                return False



# Check through letters in grid for first letter of word
for r, row in enumerate(grid):
    for c, letter in enumerate(row):
        if letter == WORD[0]:
            word = root(r, c)

            # If upwards word
            if word.check_up():
                while word.check_up():
                    if word.next_letter == len(WORD):
                        word_count += 1
                        break

            # If downwards word
            elif word.check_down():
                while word.check_down():
                    if word.next_letter == len(WORD):
                        word_count += 1
                        break

            # If rightwards word
            elif word.check_right():
                while word.check_right():
                    if word.next_letter == len(WORD):
                        word_count += 1
                        break

            # If leftwards word
            elif word.check_left():
                while word.check_left():
                    if word.next_letter == len(WORD):
                        word_count += 1
                        break
                    
print(word_count)
