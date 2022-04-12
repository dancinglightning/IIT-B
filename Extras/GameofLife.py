import copy
import matplotlib.pyplot as plt
from matplotlib import colors
from IPython.display import display, clear_output
import numpy as np
import time

class Solution:
    def neigh(self, i, j, m, n, board):
        c = 0
        if i>0 and i<m-1 and j>0 and j<n-1:
            c += board[i-1][j-1]
            c += board[i-1][j]
            c += board[i-1][j+1]
            c += board[i][j-1]
            c += board[i][j+1]
            c += board[i+1][j-1]
            c += board[i+1][j]
            c += board[i+1][j+1]
        if i==0 and i<m-1 and j>0 and j<n-1:
            c += board[i][j-1]
            c += board[i][j+1]
            c += board[i+1][j]
            c += board[i+1][j-1]
            c += board[i+1][j+1]
        if i>0 and i==m-1 and j>0 and j<n-1:
            c += board[i][j-1]
            c += board[i][j+1]
            c += board[i-1][j]
            c += board[i-1][j-1]
            c += board[i-1][j+1]
        if j==0 and j<n-1 and i>0 and i<m-1:
            c += board[i-1][j]
            c += board[i+1][j]
            c += board[i+1][j+1]
            c += board[i][j+1]
            c += board[i-1][j+1]
        if j>0 and j==n-1 and i>0 and i<m-1:
            c += board[i-1][j]
            c += board[i+1][j]
            c += board[i+1][j-1]
            c += board[i][j-1]
            c += board[i-1][j-1]
        if i==0 and i<m-1 and j==0 and j<n-1:
            c += board[i+1][j]
            c += board[i][j+1]
            c += board[i+1][j+1]
        if i>0 and i==m-1 and j>0 and j==n-1:
            c += board[i-1][j]
            c += board[i][j-1]
            c += board[i-1][j-1]
        if i>0 and i==m-1 and j==0 and j<n-1:
            c += board[i-1][j]
            c += board[i][j+1]
            c += board[i-1][j+1]
        if i==0 and i<m-1 and j>0 and j==n-1:
            c += board[i+1][j]
            c += board[i][j-1]
            c += board[i+1][j-1]
            
        return c

    def gameOfLife(self, board):
        state = copy.deepcopy(board)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                n1 = self.neigh(i, j, m, n, board)
                if n1<2:
                    state[i][j] = 0
                if n1==3:
                    state[i][j] = 1
                if n1>3:
                    state[i][j] = 0         
        return state

s = Solution()
plt.ion()
cmap = colors.ListedColormap(['red', 'blue'])
bounds = [0,1,2]
norm = colors.BoundaryNorm(bounds, cmap.N)
fig, ax = plt.subplots()
data = [[0,0,0],[1,1,1],[0,0,0]]

for i in range(100):
    data = s.gameOfLife(data)
    ax.imshow(data, cmap=cmap, norm=norm)
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, 10, 1))
    ax.set_yticks(np.arange(-.5, 10, 1))
    display(fig)    
    clear_output(wait = True)
    plt.pause(0.2)
    