"""
File    : sudoku_Algorithm.py
purpose : 1.Contain main algorithm

Bactracking Algorithm 
-> Time complexity: O(9^(n*n)). For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)).
-> Space Complexity: O(n*n). To store the output array a matrix is needed.

Better Algorithms : 
Best First Search (greedy heuristic)
Peter Norvig (http://norvig.com/sudoku.html)
"""

def print_board(board):
    print('')
    flag = 1;flag1 = 0
    for i in board:
        if flag1 == 3:
            print('-'*34)
            flag1=0
        for val in i:
            if flag != 3:
                print(val,end="  ")
            else:
                print(val," |",end="  ")
                flag=0
            flag += 1
        flag1+=1
        print('')
    print('')

# Check for empty position
def check_for_empty(board):  
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None

def check_validation(board,val,position):
    # Check for row
    for i in board[position[0]]:
        if i == val:
            return 0
    
    # Check for col
    for i in range(len(board)):
        if board[i][position[1]] == val:
            return 0
            
    # Check in local square
    box=[]
    temp=[]
    for i in range(len(board)):
        if i%3 == 0:
            temp=[]
            box.append(temp)
        temp.append(i)

    for i in box[position[0]//3]:
        for j in box[position[1]//3]:
            if board[i][j] == val:
                return 0
    return 1

# Main backtracking algorithm
def solve(board):   
    find = check_for_empty(board)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if check_validation(board,i,(row,col)):
            board[row][col] = i
            if solve(board) :
                return True
            board[row][col]=0
    return False