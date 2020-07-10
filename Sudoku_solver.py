#-----------------------------------------------------------------------Sudoku Solver----------------------------------------------------------------------------
from copy import deepcopy

#--------------------------------------------------------------------Enter Your Question------------------------------------------------------------------------
a = ([[[0], [0], [0],   [0], [0], [5],   [0], [7], [0]],
      [[0], [0], [0],   [3], [0], [0],   [0], [6], [0]],
      [[7], [6], [0],   [0], [2], [9],   [0], [0], [0]],
    
      [[8], [0], [0],   [0], [9], [0],   [0], [4], [0]],
      [[0], [0], [0],   [0], [0], [0],   [0], [0], [0]],
      [[0], [5], [6],   [0], [0], [3],   [8], [0], [0]],
      
      [[4], [0], [0],   [0], [5], [8],   [9], [0], [0]],
      [[9], [0], [0],   [0], [0], [0],   [0], [0], [7]],
      [[0], [0], [3],   [0], [0], [0],   [2], [0], [0]]])

class Sudoku:
    
    def __init__(self,a):
        self.a = a

    def check_column(self, i,j):

        num =self.a[i][j]

        for (k,l) in [(0,j), (1,j), (2,j), (3,j), (4,j), (5,j), (6,j), (7,j), (8,j)]:
            if (k,l) != (i,j):
                if len(self.a[k][l]) == 1:
                    if num == self.a[k][l]:
                        return True


    def check_row(self,i,j):
        
        num = self.a[i][j]

        for (k,l) in [(i,0), (i,1), (i,2), (i,3), (i,4), (i,5), (i,6), (i,7), (i,8)]:
            if (k,l) != (i,j):
                if len(self.a[k][l]) == 1:
                    if num == self.a[k][l]:
                        return True
        

    def check_square_is_valid(self, square,i,j):

        num = self.a[i][j]
        for (k,l) in square:
            if (k,l) != (i,j):
                if len(self.a[k][l]) == 1:
                    if num == self.a[k][l]:
                        return True

    def check_square(self,i,j):

        square_1 = [(0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2)]
        square_2 = [(3,0), (4,0), (5,0), (3,1), (4,1), (5,1), (3,2), (4,2), (5,2)]
        square_3 = [(6,0), (7,0), (8,0), (6,1), (7,1), (8,1), (6,2), (7,2), (8,2)]
        square_4 = [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]
        square_5 = [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)]
        square_6 = [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)]
        square_7 = [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)]
        square_8 = [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)]
        square_9 = [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]

        if (i,j) in square_1:
            return self.check_square_is_valid(square_1,i,j)

        elif (i,j) in square_2:
            return self.check_square_is_valid(square_2,i,j)

        elif (i,j) in square_3:
            return self.check_square_is_valid(square_3,i,j)

        elif (i,j) in square_4:
            return self.check_square_is_valid(square_4,i,j)

        elif (i,j) in square_5:
            return self.check_square_is_valid(square_5,i,j)

        elif (i,j) in square_6:
            return self.check_square_is_valid(square_6,i,j)

        elif (i,j) in square_7:
            return self.check_square_is_valid(square_7,i,j)

        elif (i,j) in square_8:
            return self.check_square_is_valid(square_8,i,j)

        elif (i,j) in square_9:
            return self.check_square_is_valid(square_9,i,j)


        
        

    def check(self,i,j):
        if (self.check_square(i,j) or self.check_row(i,j) or self.check_column(i,j)):
            return True
        
        return False
        
    def assume_after_valid(self, changes, c):

        something_different = deepcopy(c[-1])
        for i in range(9):
            for j in range(9):
                self.a[i][j] = something_different[i][j]
        
        

        if (changes[-1][2]+1) < len(self.a[changes[-1][0]][changes[-1][1]]):
            i = changes[-1][0]
            j = changes[-1][1]
            k = changes[-1][2]
            self.a[i][j] = [self.a[i][j][k+1]]
            changes.pop()
            changes.append([i,j,k+1])
        else:
            changes.pop()
            c.pop()
            self.assume_after_valid(changes, c)

    def is_not_valid(self):

        for i in range(9):
            for j in range(9):
                if self.a[i][j] == []:
                    return True
                
        for i in range(9):
            for j in range(9):
                if len(self.a[i][j]) == 1:
                    if self.check(i,j):
                        return True
                    
            
        return False

    def continue_assume(self, changes):
        k=0
        for i in range(9):
            for j in range(9):
                if len(self.a[i][j])>1:
                    changes.append([i,j,k])
                    self.a[i][j] = [self.a[i][j][k]]
                    k=1
                    break
            if k==1:
                break

        
    def check_in_square_1(self,square, i,j):
        
        for num in range(1,10):
            coun=0
            for (k,l) in square:
                if self.a[k][l] != [0] and len(self.a[k][l]) == 1:
                    if num in self.a[k][l]:
                        coun=1
                        break
            if coun==0:
                if self.a[i][j] == [0]:
                    self.a[i][j] = [num]
                else:
                    self.a[i][j].append(num)

    def check_in_square(self,square, i,j):
        
        for num in self.a[i][j]:
            for (k,l) in square:
                if self.a[k][l] != [0] and len(self.a[k][l]) == 1:
                    if num in self.a[k][l]:
                        self.a[i][j].remove(num)
                        break

        

    def check_in_row(self, i,j):

        for num in self.a[i][j]:

            for (k,l) in [(i,0), (i,1), (i,2), (i,3), (i,4), (i,5), (i,6), (i,7), (i,8)]:
                if (k,l) != (i,j):
                    if self.a[k][l] != [0] and len(self.a[k][l]) == 1:
                        if num in self.a[k][l]:
                            if num in self.a[i][j]:
                                self.a[i][j].remove(num)
                            break

    def check_in_column(self, i,j):

        for num in self.a[i][j]:

            for (k,l) in [(0,j), (1,j), (2,j), (3,j), (4,j), (5,j), (6,j), (7,j), (8,j)]:
                if (k,l) != (i,j):
                    if self.a[k][l] != [0] and len(self.a[k][l]) == 1:
                        if num in self.a[k][l]:
                            if num in self.a[i][j]:
                                self.a[i][j].remove(num)
                            break

    def square_1(self, i,j):

        square_1 = [(0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2)]
        square_2 = [(3,0), (4,0), (5,0), (3,1), (4,1), (5,1), (3,2), (4,2), (5,2)]
        square_3 = [(6,0), (7,0), (8,0), (6,1), (7,1), (8,1), (6,2), (7,2), (8,2)]
        square_4 = [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]
        square_5 = [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)]
        square_6 = [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)]
        square_7 = [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)]
        square_8 = [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)]
        square_9 = [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]
        
        if (i,j) in square_1:
            self.check_in_square_1(square_1,i,j)

        elif (i,j) in square_2:
            self.check_in_square_1(square_2,i,j)

        elif (i,j) in square_3:
            self.check_in_square_1(square_3,i,j)

        elif (i,j) in square_4:
            self.check_in_square_1(square_4,i,j)

        elif (i,j) in square_5:
            self.check_in_square_1(square_5,i,j)

        elif (i,j) in square_6:
            self.check_in_square_1(square_6,i,j)

        elif (i,j) in square_7:
            self.check_in_square_1(square_7,i,j)

        elif (i,j) in square_8:
            self.check_in_square_1(square_8,i,j)

        elif (i,j) in square_9:
            self.check_in_square_1(square_9,i,j)

    def square(self, i,j):

        square_1 = [(0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2)]
        square_2 = [(3,0), (4,0), (5,0), (3,1), (4,1), (5,1), (3,2), (4,2), (5,2)]
        square_3 = [(6,0), (7,0), (8,0), (6,1), (7,1), (8,1), (6,2), (7,2), (8,2)]
        square_4 = [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]
        square_5 = [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)]
        square_6 = [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)]
        square_7 = [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)]
        square_8 = [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)]
        square_9 = [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]
        
        if (i,j) in square_1:
            self.check_in_square(square_1,i,j)

        elif (i,j) in square_2:
            self.check_in_square(square_2,i,j)

        elif (i,j) in square_3:
            self.check_in_square(square_3,i,j)

        elif (i,j) in square_4:
            self.check_in_square(square_4,i,j)

        elif (i,j) in square_5:
            self.check_in_square(square_5,i,j)

        elif (i,j) in square_6:
            self.check_in_square(square_6,i,j)

        elif (i,j) in square_7:
            self.check_in_square(square_7,i,j)

        elif (i,j) in square_8:
            self.check_in_square(square_8,i,j)

        elif (i,j) in square_9:
            self.check_in_square(square_9,i,j)

    def solve_1(self):

        for j in range(9):
            for i in range(9):
                if self.a[i][j] == [0] or len(self.a[i][j])>1:
                    self.square_1(i,j)
                    self.check_in_row(i,j)
                    self.check_in_column(i,j)

    def solve(self):

        for j in range(9):
            for i in range(9):
                if len(self.a[i][j])>1:
                    self.square(i,j)
                    self.check_in_row(i,j)
                    self.check_in_column(i,j)
    
c=[]
changes = []
question = Sudoku(a)        
question.solve_1()
run = True

print("START")
while run:
    
    b = deepcopy(a)
    
    for i in range(9):
        for j in range(9):
            question.solve()
    
    counter = 0
    for i in range(9):
        for j in range(9):
            if len(a[i][j]) == 1:
                counter+=1
    if counter == 81:
        run = False
        for i in range(9):
            for j in range(9):
                print(a[i][j], end="")
            print()
        print()

    if question.is_not_valid():
        question.assume_after_valid(changes, c)
        
        while len(c)>len(changes):
            c.pop()
        
        
    if run:
        if b == a:
            copy_to_c = deepcopy(b)
            c.append(copy_to_c)
            question.continue_assume(changes)
               

                    
    
    
