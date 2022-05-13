import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
        ##print(row)
            for j in range(self.width):
                row.append(False)
            self.board.append(row)
            ##print(self.board)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if (len(self.cells) == self.count):
            return self.cells
        else:
            return set()    

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if(self.count == 0):
            return self.cells
        else:
            return set()    
        

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """      
        if cell not in self.cells:
            return
        updated_cell=[]
        for current_cell in self.cells:
            if current_cell == cell:
                continue
            updated_cell.append(current_cell)

        self.cells =set(updated_cell)
        if len(updated_cell):
            self.count =self.count-1
        elif updated_cell==[]:
            self.count=0 
        return

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """ 
        if cell not in self.cells:
            return       
        updated_cell =[]
        
        for current_cell in self.cells:
            if current_cell== cell:
                continue
            updated_cell.append(current_cell)

        self.cells = set(updated_cell)
        return


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        #1) mark the cell as a move that has been made
        self.moves_made.add(cell)
        #2) mark the cell as safe
        self.mark_safe(cell)
        #3) add a new sentence to the AI's knowledge base based on the value of `cell` and `count`        
        neighboring_cells = set()
        for i in range(self.height):
            for j in range(self.width):
                row=cell[0]
                column=cell[1]
                if (i, j) in self.safes:
                    continue
                elif  ((i - row) == 1 and (j-column)==0) or ((i - row) == -1 and (j-column)==0):
                    neighboring_cells.add((i, j))
                elif ((i - row) == 0 and (j-column)==-1) or ((i - row) == 0 and (j-column)==1):
                    neighboring_cells.add((i, j))
                elif ((i - row) == 1 and abs(j - column) == 1) or ((i - row) == 1 and abs(j - column) == -1) or ((i - row) == -1 and abs(j - column) == 1) or ((i - row) == -1 and abs(j - column) == -1):
                    neighboring_cells.add((i, j))
                else:
                    continue                   
        
        new_sentence = Sentence(neighboring_cells, count)      
        self.knowledge.append(new_sentence)

        #4) mark any additional cells as safe or as mines if it can be concluded based on the AI's knowledge base
        for current_sentence in self.knowledge:
            mines_marked = current_sentence.known_mines()
            safes_marked = current_sentence.known_safes()
            for current_cell in current_sentence.cells:
                if current_cell in mines_marked:
                    self.mark_mine(current_cell)
                if current_cell in safes_marked:
                    self.mark_safe(current_cell)
                    
        # 5)mark any additional cells as safe or as mines if it can be concluded based on the AI's knowledge base

        new_knowledge = []        
        for sentence1 in self.knowledge:
            for sentence2 in self.knowledge:
                if sentence1.cells == sentence2.cells:
                    continue
                if len(sentence1.cells)==0:
                    continue
                if len(sentence2.cells)==0:
                    continue
                if sentence1.count == 0:
                    continue
                if sentence2.count == 0:
                    continue
                if sentence2.cells.issuperset(sentence1.cells):
                    new_cells = sentence2.cells - sentence1.cells
                    new_count = sentence2.count - sentence1.count
                    new_sentence = Sentence(new_cells, new_count)
                    new_knowledge.append(new_sentence)
        
        for new_sentence in new_knowledge:   
            if len(new_knowledge):    
                self.knowledge.append(new_sentence)
        return

                  


    def mark_cells(self):
        safes = []
        mines = []

        for sentence in self.knowledge:
            for safe in sentence.known_safes():
                if safe not in safes and safe not in self.safes:
                    safes.append(safe)
            for mine in sentence.known_mines():
                if mine not in mines and mine not in self.mines:
                    mines.append(mine)   

        for tempSafe in safes:
            self.mark_safe(tempSafe)
        for tempMine in mines:
            self.mark_mine(tempMine)                             
        

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """       
        
        for safe_move in self.safes:
            ## If the safe move not made before and not in mines, and is not an empty set, then return the safe move
            if (safe_move not in self.moves_made) and (safe_move not in self.mines):                                          
                return safe_move
        return None
            
        
                      
       
    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
            
        """ 
        ## initially declare all possible moves as empty list[]
        all_possible_moves=set()
        ## Always run
        while True:
            ## Check each row and column
            for i in range(self.height):
                for j in range(self.width):  
                    ## If the move is not made and not in mines                   
                    if (i,j) not in self.moves_made and (i,j) not in self.mines: 
                        ## Add to the possible move                       
                        all_possible_moves.add((i,j))
                  
            if all_possible_moves==set(): ## If the moves are empty set, then no moves are possible
                return None        
            elif len(all_possible_moves): ## Randomly choose a possible move if the set is not empty                  
                random_move=random.choice(tuple(all_possible_moves))
                 ## If the move is not made and not in mines 
                 ## return the random choice move
                if random_move not in self.moves_made and random_move not in self.mines and len(all_possible_moves)!=0:
                    return random_move 

                                                    
                       
        