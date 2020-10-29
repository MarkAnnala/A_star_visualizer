import pygame
import a_star

def create_grid(rows, cols):
    grid = []
    for x in range(rows): 
        grid.append([])
        for y in range(cols): 
            grid[x].append(0) # 0 is no obstacle, 1 is an obstacle 
    return grid


def init():
    #make some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    #define height and width of cells 
    WIDTH = 30 
    HEIGHT = 30 
    MARGIN = 5
    #choose amount of rows and cols 
    rows, cols = 20, 20
    #define a window size
    WINDOW_SIZE = [rows*(WIDTH+MARGIN)+MARGIN ,cols*(WIDTH+MARGIN)+MARGIN]
    #make the grid..
    grid = create_grid(rows,cols)
    

    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    clock = pygame.time.Clock()
    done = False 
    state = 0
    while not done: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done= True
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                #create obstacles 
                if state == 0:
                    pos = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    if click[0] == True: 
                        col = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        if grid[row][col] == 1:
                            grid[row][col] = 0
                        else: 
                            grid[row][col] = 1 
            elif event.type == pygame.KEYDOWN:
                if event.key == 13: 
                    if state == 0:
                        state = 1 
                    else:
                        state = 2
                        a_star.aStar(grid, (0,0), (19,19))
                        #done = True

        for row in range(rows):
            for col in range(cols): 
                color = WHITE
                if grid[row][col] == 1: 
                    color = RED
                elif grid[row][col] == 2:
                    color = GREEN
                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * col + MARGIN , (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()

g = create_grid(5,5)

path = a_star.aStar(g, (0,0), (4,4))
print(path)
init()