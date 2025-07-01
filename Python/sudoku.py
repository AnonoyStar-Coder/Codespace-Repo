import pygame
pygame.font.init()

# Initialize the window
Window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("SUDOKU GAME")

# Title Screen Function
def title_screen():
    Window.fill((255, 182, 193))  # Background color for the title screen

    # Title Text
    title_font = pygame.font.SysFont("Segoe UI", 60)
    title_text = title_font.render("SUDOKU GAME", True, (0, 0, 0))
    Window.blit(title_text, (600 // 2 - title_text.get_width() // 2, 100))

    # Button Texts
    button_font = pygame.font.SysFont("Segoe UI", 40)
    
    easy_button = button_font.render("Easy", True, (0, 0, 0))
    medium_button = button_font.render("Medium", True, (0, 0, 0))
    hard_button = button_font.render("Hard", True, (0, 0, 0))
    
    # Button Rectangles
    easy_rect = pygame.Rect(200, 250, 200, 50)
    medium_rect = pygame.Rect(200, 350, 200, 50)
    hard_rect = pygame.Rect(200, 450, 200, 50)
    
    pygame.draw.rect(Window, (255, 255, 255), easy_rect)
    pygame.draw.rect(Window, (255, 255, 255), medium_rect)
    pygame.draw.rect(Window, (255, 255, 255), hard_rect)
    
    Window.blit(easy_button, (300 - easy_button.get_width() // 2, 250))
    Window.blit(medium_button, (300 - medium_button.get_width() // 2, 350))
    Window.blit(hard_button, (300 - hard_button.get_width() // 2, 450))
    
    pygame.display.update()
    
    return easy_rect, medium_rect, hard_rect

def handle_title_screen():
    while True:
        easy_rect, medium_rect, hard_rect = title_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if easy_rect.collidepoint(pos):
                    return "easy"
                if medium_rect.collidepoint(pos):
                    return "medium"
                if hard_rect.collidepoint(pos):
                    return "hard"

# Initialize the game and display the title screen
pygame.init()

difficulty = handle_title_screen()

if difficulty == "easy":
    defaultgrid = [
        [8, 9, 0, 5, 7, 4, 0, 6, 3],
        [0, 4, 6, 0, 1, 0, 0, 5, 2],
        [5, 0, 0, 6, 0, 2, 0, 9, 7],
        [9, 6, 5, 7, 4, 0, 3, 0, 1],
        [3, 8, 0, 0, 2, 0, 6, 7, 5],
        [2, 0, 4, 9, 0, 3, 0, 4, 8],
        [0, 0, 8, 0, 9, 1, 7, 0, 6],
        [1, 7, 3, 4, 6, 0, 2, 8, 0],
        [6, 0, 9, 8, 3, 7, 0, 1, 4],
    ]
elif difficulty == "medium":
    defaultgrid = [
        [8, 9, 0, 5, 7, 4, 0, 6, 3],
        [0, 4, 6, 0, 0, 0, 0, 5, 2],
        [5, 0, 0, 6, 0, 2, 0, 0, 0],
        [9, 6, 0, 7, 0, 0, 3, 0, 1],
        [3, 8, 0, 0, 2, 0, 6, 7, 0],
        [2, 0, 4, 9, 0, 3, 0, 4, 8],
        [0, 0, 0, 0, 0, 1, 7, 0, 6],
        [1, 7, 3, 4, 0, 0, 2, 8, 0],
        [6, 0, 0, 8, 3, 7, 0, 1, 4],
    ]
elif difficulty == "hard":
    defaultgrid = [
        [8, 0, 0, 5, 7, 4, 0, 6, 3],
        [0, 0, 6, 0, 0, 0, 0, 5, 2],
        [5, 0, 0, 6, 0, 2, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 3, 0, 1],
        [0, 8, 0, 0, 2, 0, 6, 7, 0],
        [2, 0, 4, 9, 0, 0, 0, 4, 8],
        [0, 0, 0, 0, 0, 1, 7, 0, 6],
        [1, 0, 3, 0, 0, 0, 0, 8, 0],
        [6, 0, 0, 8, 3, 7, 0, 1, 4],
    ]
else:
    print("wrong choice.. :(")
    pygame.quit()
    exit()

# Solved grid corresponding to the new default grid
solved_grid = [
    [8, 9, 2, 5, 7, 4, 1, 6, 3],
    [7, 4, 6, 3, 1, 9, 8, 5, 2],
    [5, 3, 1, 6, 8, 2, 4, 9, 7],
    [9, 6, 5, 7, 4, 8, 3, 2, 1],
    [3, 8, 7, 1, 2, 6, 9, 7, 5],
    [2, 1, 4, 9, 5, 3, 7, 4, 8],
    [4, 5, 8, 2, 9, 1, 7, 3, 6],
    [1, 7, 3, 4, 6, 5, 2, 8, 9],
    [6, 2, 9, 8, 3, 7, 5, 1, 4],
]

font = pygame.font.SysFont("Segoe UI", 40)
font1 = pygame.font.SysFont("Segoe UI", 20)

x = 0
y = 0
diff = 600 / 9
value = 0
mistake_count = 0
game_over = False

def cord(pos):
    global x
    x = pos[0] // diff
    global y
    y = pos[1] // diff

def highlightbox():
    for k in range(2):
        pygame.draw.line(Window, (0, 0, 0), (x * diff - 3, (y + k) * diff), (x * diff + diff + 3, (y + k) * diff), 7)
        pygame.draw.line(Window, (0, 0, 0), ((x + k) * diff, y * diff), ((x + k) * diff, y * diff + diff), 7)

def drawlines():
    for i in range(9):
        for j in range(9):
            if defaultgrid[i][j] != 0:
                pygame.draw.rect(Window, (255, 255, 0), (j * diff, i * diff, diff + 1, diff + 1))
                text1 = font.render(str(defaultgrid[i][j]), True, (0, 0, 0))
                Window.blit(text1, (j * diff + (diff - text1.get_width()) // 2, i * diff + (diff - text1.get_height()) // 2))

    for l in range(10):
        thick = 7 if l % 3 == 0 else 1
        pygame.draw.line(Window, (0, 0, 0), (0, l * diff), (600, l * diff), thick)
        pygame.draw.line(Window, (0, 0, 0), (l * diff, 0), (l * diff, 600), thick)

def drawvalue(val):
    text1 = font.render(str(val), True, (0, 0, 0))
    Window.blit(text1, (x * diff + (diff - text1.get_width()) // 2, y * diff + (diff - text1.get_height()) // 2))

def raiseerror1():
    text1 = font1.render("WRONG!!!", True, (0, 0, 0))
    Window.blit(text1, (20, 570))

def raiseerror2():
    text1 = font1.render("Wrong Not a valid Key", True, (0, 0, 0))
    Window.blit(text1, (20, 570))

def valid(m, k):
    if k not in defaultgrid[m] and all(row[k] != defaultgrid[m][k] for row in defaultgrid):
        return True
    return False

def finish():
    text1 = font.render("Game over", True, (0, 0, 0))
    Window.blit(text1, (600 // 2 - text1.get_width() // 2, 610))

def gameresult():
    for i in range(9):
        for j in range(9):
            if defaultgrid[i][j] == 0:
                return False
    return True

def checkerrors():
    global mistake_count, game_over
    if defaultgrid[int(y)][int(x)] == 0:
        defaultgrid[int(y)][int(x)] = value
        if value != solved_grid[int(y)][int(x)]:
            mistake_count += 1
            if mistake_count == 3:
                game_over = True
            raiseerror1()
            defaultgrid[int(y)][int(x)] = 0
        else:
            drawvalue(value)
            if gameresult():
                finish()
    else:
        raiseerror2()

def gameloop():
    global x, y, value, mistake_count, game_over
    run = True
    flag1 = 0
    flag2 = 0
    flag3 = 0
    while run:
        if game_over:
            finish()
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            return
        
        Window.fill((255, 182, 193))
        drawlines()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = 1
                pos = pygame.mouse.get_pos()
                cord(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 1
                    flag1 = 1
                if event.key == pygame.K_RIGHT:
                    x += 1
                    flag1 = 1
                if event.key == pygame.K_UP:
                    y -= 1
                    flag1 = 1
                if event.key == pygame.K_DOWN:
                    y += 1
                    flag1 = 1
                if event.key == pygame.K_1:
                    value = 1
                if event.key == pygame.K_2:
                    value = 2
                if event.key == pygame.K_3:
                    value = 3
                if event.key == pygame.K_4:
                    value = 4
                if event.key == pygame.K_5:
                    value = 5
                if event.key == pygame.K_6:
                    value = 6
                if event.key == pygame.K_7:
                    value = 7
                if event.key == pygame.K_8:
                    value = 8
                if event.key == pygame.K_9:
                    value = 9
                flag2 = 1 if value != 0 else 0
                flag3 = 1
        if flag1:
            highlightbox()
            flag1 = 0
        if flag2:
            drawvalue(value)
            checkerrors()
            flag2 = 0
        if flag3:
            drawlines()
            flag3 = 0
        pygame.display.update()

gameresult()
gameloop()
pygame.quit()

