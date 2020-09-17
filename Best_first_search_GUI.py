import pygame
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

width = 800
height = 800
cols = 50
rows = 50
cellW = width // cols
cellH = height // rows
red = (225, 0, 0)
green = (0, 225, 0)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (225, 8, 127)
electric = (126, 249, 255)
teal = (0, 128, 129)

global start
global end
grid = []
openSet = []
closedSet = []
cameFrom = []

pygame.init()
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('BFS PATH FINDER')


class cell:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.h = 0
        self.neighbours = []
        self.previous = None
        self.obs = False
        self.closed = False
        self.open = True
        self.value = 1
        self.rowT = [+0, -1, -1, -1, +0, +1, +1, +1]
        self.colT = [+1, +1, +0, -1, -1, -1, +0, +1]

    def show(self, color, st):
        pygame.draw.rect(screen, color, (self.i * cellW, self.j * cellH, cellW, cellH), st)  # drawing rectangle
        pygame.display.update()


    def addNeighbours(self, cells):
        cur_i, cur_j = self.i, self.j
        for k in range(0, 8):
            x, y = self.colT[k], self.rowT[k]
            if cols > x + cur_i >= 0 and rows > y + cur_j >= 0 and not cells[cur_i + x][cur_j + y].obs:
                self.neighbours.append(cells[cur_i + x][cur_j + y])


for iy in range(cols):
    temp = []
    for jx in range(rows):
        temp.append(cell(iy, jx))
    grid.append(temp)
    for jx in range(rows):
        grid[iy][jx].show(white, 0)


def mousePress(x):
    t = x[0]
    w = x[1]
    g1 = t // (width // cols)
    g2 = w // (height // rows)
    access = grid[g1][g2]
    if access != start and access != end:
        if not access.obs:
            access.obs = True
            access.show(black, 0)


def mousePressSpecial(x):
    global start
    global end
    t = x[0]
    w = x[1]
    g1 = t // (width // cols)
    g2 = w // (height // rows)
    if mouse_clicked == 0:
        start = grid[g1][g2]
        start.show(pink, 0)
        openSet.append(start)
        start.previous = start
        return True
    elif mouse_clicked == 1:
        end = grid[g1][g2]
        if start == end:
            return False
        else:
            end.show(pink, 0)
            return True


loop = True
mouse_clicked = 0

while loop:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if mouse_clicked > 1:
                mousePress(pos)
            else:
                if mousePressSpecial(pos):
                    mouse_clicked = mouse_clicked + 1

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break

for i in range(cols):
    for j in range(rows):
        grid[i][j].addNeighbours(grid)


def heuristic(n, e):
    d = math.sqrt((n.i - e.i) ** 2 + (n.j - e.j) ** 2)
    # d = abs(n.i - e.i) + abs(n.j - e.j)
    return d


def main():
    start.show(pink, 0)
    end.show(pink, 0)

    if len(openSet) > 0:
        lowestIndex = 0
        # ----------------------------------- #
        for op_i in range(len(openSet)):
            if openSet[op_i].h < openSet[lowestIndex].h:
                lowestIndex = op_i
        # ----------------------------------- #
        current = openSet[lowestIndex]
        

        if current == end:
            temp_h = 0
            
            start.show(pink, 0)

            while current.previous != current:
                current.show(green, 0)
                current = current.previous
                temp_h = temp_h + 1

            end.show(pink, 0)
            print('done', current.h)
            Tk().wm_withdraw()
            messagebox.showinfo('Program Finished','Destination is '+ str(temp_h) + ' blocks away.')
            pygame.quit()
            quit()

        openSet.pop(lowestIndex)
        closedSet.append(current)
        current.open = False

        neighbours = current.neighbours
        # ----------------------------------- #
        for ne_i in range(len(neighbours)):
            neighbor = neighbours[ne_i]
            if neighbor.open: 
                tempH = heuristic(neighbor, end)
                if neighbor in openSet:
                    if neighbor.h > tempH:
                        neighbor.h = tempH
                else:
                    neighbor.h = tempH
                    openSet.append(neighbor)
        # ----------------------------------- #
            if neighbor.previous is None:
                neighbor.previous = current
    else:
        Tk().wm_withdraw()
        messagebox.showinfo('Program Finished', 'Path does not exist.')
        pygame.quit()
        quit()
        
    for cell_i in openSet:
        cell_i.show(electric, 0)
    for cell_i in closedSet:
        if cell_i != start:
            cell_i.show(teal, 0)


while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
        quit()
    pygame.display.update()
    main()
