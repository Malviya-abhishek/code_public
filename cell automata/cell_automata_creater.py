# NOTE ---------------------------------------------#
    # def fun_name(grid, x, y, colour):
    #     grid[y][x] = True
    #     show1(colour, x, y)
# NOTE ---------------------------------------------#

def init(size, cellw, cellh, Width, Height,Screen, Pygame, Rows, Cols):
    global cell_size; cell_size = size
    global cellW; cellW = cellw
    global cols; cols = Cols
    global rows; rows = Rows
    global cellH; cellH = cellh
    global width; width = Width
    global height; height= Height
    global screen; screen = Screen 
    global pygame; pygame = Pygame




def show1(colour, x, y):
    x = x%cols
    y = y%rows
    pygame.draw.rect(screen, colour, (x * cellW, y * cellH, cellW, cellH), 0)
    pygame.display.update()


def galaxy(grid, x, y, colour):
    
    for i in range(6):
        grid[y%rows][(x+i)%cols] = True ; grid[(y+1)%rows][(x+i)%cols] = True
        show1(colour,x+i, y)  ; show1(colour,x+i, y+1)

        grid[(y+7)%rows][(x+i+3)%cols] = True ; grid[(y+8)%rows][(x+i+3)%cols] = True
        show1(colour,x+i+3, y+7)  ; show1(colour,x+i+3, y+8)

        grid[(y+i)%rows][(x+7)%cols] = True; grid[(y+i)%rows][(x+8)%cols] = True
        show1(colour,x+7, y+i) ; show1(colour,x+8, y+i)

        grid[(y+3+i)%rows][x%cols] = True; grid[(y+3+i)%rows][(x+1)%cols] = True
        show1(colour,x, y+3+i) ; show1(colour,x+1, y+3+i)


def glider(grid, x, y, colour):
    grid[y%rows][x%cols] = True  
    show1(colour,x, y)
    y += 1
    grid[y%rows][(x+1)%cols]= True
    show1(colour, x+1, y)
    y+=1
    grid[y%rows][(x+1)%cols]= True ; grid[y%rows][x] = True  ; grid[y%rows][(x-1)%cols] = True
    show1(colour, x+1,y)  ; show1(colour, x, y)   ; show1(colour, x-1, y)


def space_ship(grid, x, y, colour):
    grid[y][x] = True  ; grid[y][x+1]=True
    show1(colour, x, y)  ; show1(colour, x+1, y)
    y += 1
    grid[y][x-1]=True  ; grid[y][x+2]=True
    show1(colour, x-1, y); show1(colour, x+2, y)
    y += 1
    grid[y][x-1]=True  ; grid[y][x-2]=True  ; grid[y][x+2]=True  ; grid[y][x+3]=True
    show1(colour, x-1, y); show1(colour, x-2, y); show1(colour, x+2, y); show1(colour, x+3, y)
    y += 1
    grid[y][x-1]=True  ; grid[y][x-2]=True  ; grid[y][x+2]=True  ; grid[y][x+3]=True
    show1(colour, x-1, y); show1(colour, x-2, y); show1(colour, x+2, y); show1(colour, x+3, y)
    y += 1
    grid[y][x]=True    ; grid[y][x+1]=True  ; grid[y][x-2]=True  ; grid[y][x+3]=True
    show1(colour, x, y)  ; show1(colour, x+1, y); show1(colour, x-2, y); show1(colour, x+3, y)
    y += 1
    grid[y][x]=True    ; grid[y][x+1]=True  ; 
    show1(colour, x, y)  ; show1(colour, x+1, y)
    y += 1
    grid[y][x-2]=True  ; grid[y][x+3]=True
    show1(colour, x-2, y); show1(colour, x+3, y)
    y += 1
    grid[y][x-2]=True  ; grid[y][x+3]=True  ; grid[y][x-3]=True  ; grid[y][x+4]=True
    show1(colour, x-2, y); show1(colour, x+3, y); show1(colour, x-3, y); show1(colour, x+4, y)
    y += 3
    grid[y][x]=True    ; grid[y][x+1]=True
    show1(colour, x, y)  ; show1(colour, x+1, y)
    y += 1
    grid[y][x-1]=True  ; grid[y][x+2]=True
    show1(colour, x-1, y); show1(colour, x+2, y)
    y += 1
    grid[y][x-1]=True  ; grid[y][x+2]=True
    show1(colour, x-1, y); show1(colour, x+2, y)


def glider_shooter(grid, x, y, colour):

	for i in range(6):
		grid[y%rows][(x-i)%cols] = True  ; grid[y%rows][(x+1+i)%cols] = True
		show1(colour, x-i, y); show1(colour, x+1+i, y)

	for i in range(4):
		grid[(y+2)%rows][(x-i)%cols] = True  ; grid[(y+2)%rows][(x+1+i)%cols] = True
		show1(colour, x-i, y+2); show1(colour, x+1+i, y+2)
		grid[(y-2)%rows][(x-i)%cols] = True  ; grid[(y-2)%rows][(x+1+i)%cols] = True
		show1(colour, x-i, y-2); show1(colour, x+1+i, y-2)

	for i in range(2):
		grid[(y+4)%rows][(x-i)%cols] = True  ; grid[(y+4)%rows][(x+1+i)%cols] = True
		show1(colour, x-i, y+4); show1(colour, x+1+i, y+4)
		grid[(y-4)%rows][(x-i)%cols] = True  ; grid[(y-4)%rows][(x+1+i)%cols] = True
		show1(colour, x-i, y-4); show1(colour, x+1+i, y-4)

