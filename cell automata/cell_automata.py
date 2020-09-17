import pygame, sys, random, time
import cell_automata_creater as cac

cell_size = 10
cellW = cell_size
cellH = cell_size

width = 1500 
height= 750 

cols = width //cell_size
rows = height//cell_size

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
grey = (123, 154, 123)
green = (0, 255, 0)
back_ground = (56,12,30)
rowT = [+0, -1, -1, -1, +0, +1, +1, +1]
colT = [+1, +1, +0, -1, -1, -1, +0, +1]
global gen
frame_rate = 30
gen = 0

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('AUTOMATES_3 CELL FPS ' + str(frame_rate) + ' GEN ' + str(gen))


cac.init(cell_size, cellW, cellH, width, height, screen, pygame, rows, cols)
screen.fill(back_ground)
pygame.display.update()


def show1(colour, x, y):
    x = x%cols
    y = y%rows
    pygame.draw.rect(screen, colour, (x * cellW, y * cellH, cellW, cellH), 0)
    pygame.display.update()


def around(x, y):
    temp = 0
    for k in range(8):
        cur_x = x + rowT[k]
        cur_y = y + colT[k]
        if grid[ cur_y % rows ][ cur_x % cols ]:
            temp += 1
    return temp


grid = []
point_stack = []

for y in range(rows):
    temp = []
    for x in range(cols):
        temp.append(False)
    grid.append(temp)


def mousePress(point):
    t = point[0]
    w = point[1]
    g2 = t // (width // cols)
    g1 = w // (height // rows)

    if cols > g2 >= 0 and rows > g1 >=0:
        if not grid[g1][g2]:
            grid[g1][g2] = True
            point_stack.append((g1,g2))
            show1(grey, g2, g1)


loop = True
while loop:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            loop = False
            pygame.quit()
            exit()

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            mousePress(pos)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(point_stack) > 0:
                    y,x = point_stack.pop()
                    grid[y][x] = False
                    show1(back_ground,x,y)
            elif event.key == pygame.K_r:
                while len(point_stack) > 0:
                    y,x = point_stack.pop()
                    grid[y][x] = False
                    show1(back_ground,x,y)

            elif event.key == pygame.K_SPACE:
                loop = False
                break
            else: 
                pos = pygame.mouse.get_pos()
                print(pos)
                t = pos[0]
                w = pos[1]
                g2 = t // (width // cols)
                g1 = w // (height // rows)
                if cols > g2 >= 0 and rows > g1 >=0:
                    if event.key == pygame.K_1:
                        cac.space_ship(grid,g2, g1, grey)
                    elif event.key == pygame.K_2:
                        cac.glider(grid, g2, g1, grey)
                    elif event.key == pygame.K_3:
                        cac.galaxy(grid, g2, g1, grey)
                    elif event.key == pygame.K_4:
                        cac.glider_shooter(grid, g2, g1, grey)
                    #---------------------------------------------------------------------------------------#
                        # elif event.key == pygame.K_5 
                        #     cac.fun_name(grid, g2, g1, grey)
                    #---------------------------------------------------------------------------------------#


def main():
    global grid
    global gen
    gen += 1
    print(gen)
    temp_grid = []
    for y in range(rows):
        temp = []
        for x in range(cols):
            temp_num = around(x, y)
            flag = grid[y][x]
            if temp_num < 2:
                if flag:
                    flag = False
                    pygame.draw.rect(screen, black, (x * cellW, y * cellH, cellW, cellH), 0)
            elif temp_num == 3:
                if flag is False:
                    flag = True
                    pygame.draw.rect(screen, grey, (x * cellW, y * cellH, cellW, cellH), 0)
            elif temp_num > 3:
                if flag:
                    flag = False
                    pygame.draw.rect(screen, black, (x * cellW, y * cellH, cellW, cellH), 0)
            temp.append(flag)
        temp_grid.append(temp)
    grid = temp_grid


while True:
    ev = pygame.event.poll()
    pos = pygame.mouse.get_pos()
    if ev.type == pygame.QUIT:
        pygame.quit()
        quit()
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
        elif ev.key == pygame.K_UP:
            if frame_rate < 60:
                frame_rate += 5
                
        elif ev.key == pygame.K_DOWN:
            if frame_rate > 10:
                frame_rate -= 5
                

    
    pygame.display.set_caption('AUTOMATES_3 CELL FPS ' + str(frame_rate) + ' GEN ' + str(gen))
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(frame_rate)
    main()
    


