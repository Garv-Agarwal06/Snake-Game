import pygame

x = pygame.init()
import random
import os
import pygame.mixer

pygame.mixer.init()

eat_sound = pygame.mixer.Sound("eating.mp3")
gameover_sound = pygame.mixer.Sound("gameover1.mp3")

# x is used just for checking all modules imported
# print(x)
# giving colour
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
light_grey = (211, 211, 211)
screen_x = 1200
screen_y = 700
light_blue=(87, 185, 255)
Exit_game = False
cell_size = 35

apple_img=pygame.image.load("apple.png")
apple_img=pygame.transform.scale(apple_img,(cell_size,cell_size))

head_img = pygame.image.load("head.png")
head_img = pygame.transform.scale(head_img,(cell_size,cell_size))

middle_img = pygame.image.load("middle.png")
middle_img = pygame.transform.scale(middle_img,(cell_size,cell_size))

tail_img = pygame.image.load("tail.png")
tail_img = pygame.transform.scale(tail_img,(cell_size,cell_size))




clock = pygame.time.Clock()

gamewindow = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Snake Game")

pygame.display.update()

# function for display
font = pygame.font.SysFont("comicsans", 55)


def display_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gamewindow.blit(screen_text, (x, y))


# function for mouse
def draw_button(text, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(gamewindow, active_color, [x, y, w, h])
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(gamewindow, inactive_color, [x, y, w, h])

    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(x + w // 2, y + h // 2))
    gamewindow.blit(text_surface, text_rect)


# defing buttions
def start_game():
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1)
    game_loop()


def quit_game():
    pygame.quit()
    quit()


def welcome_screen():
    global Exit_game, screen_x, screen_y

    info = pygame.display.Info()
    screen_x = info.current_w
    screen_y = info.current_h
    gamewindow = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE)


    # background image
    original_bg = pygame.image.load("background.png")
    bgimage = pygame.transform.scale(original_bg, (screen_x, screen_y)).convert_alpha()
    global gameover_img
    original_gameover_img = pygame.image.load("gameover.png")
    gameover_img=pygame.transform.scale(original_gameover_img, (screen_x, screen_y)).convert_alpha()
    while not Exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit_game = True
            elif event.type == pygame.VIDEORESIZE:
                screen_x, screen_y = event.w, event.h
                gamewindow = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE)
                bgimage = pygame.transform.scale(original_bg, (screen_x, screen_y))
                gameover_img=pygame.transform.scale(pygame.image.load("gameover.png"), (screen_x, screen_y)).convert_alpha()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    while True:
                        pygame.mixer.music.load("background.mp3")
                        pygame.mixer.music.play(-1)
                        game_loop()
        gamewindow.blit(bgimage, (0, 0))
        draw_button("Play", screen_x // 2 -250, screen_y // 2 +175, 200, 60, green, (0, 200, 0), start_game)
        draw_button("Quit", screen_x // 2 , screen_y // 2 + 175, 200, 60, red, (200, 0, 0), quit_game)
        grid_x = screen_x // cell_size
        grid_y = screen_y // cell_size

        pygame.display.update()
        clock.tick(60)


def game_loop():
    # game variables

    global grid_x, grid_y
    screen_x, screen_y = pygame.display.get_surface().get_size()
    grid_x = screen_x // cell_size
    grid_y = screen_y // cell_size
    snake_x = grid_x // 2
    snake_y = grid_y // 2
    velocity_x = 1
    velocity_y = 0
    food_x = random.randint(0, grid_x - 1)
    food_y = random.randint(0, grid_y - 1)
    snake_size = cell_size
    food_size = cell_size
    fps = 60
    move_delay = 6
    move_counter = 0
    score = 0
    snake_list = [[snake_x - 1, snake_y], [snake_x, snake_y]]
    snake_length = 2
    Game_over = False

    # high score
    if (not os.path.exists('hi.txt')):
        with open('hi.txt', 'w') as file:
            file.write("0")
    with open("hi.txt", "r") as f:
        high_s = f.read()

    # increasing snake
    def plot_snake(gamewindow, snake_list):
        for i, (x, y) in enumerate(snake_list):
            pos=(x*cell_size,y*cell_size)
            if i==len(snake_list)-1:
                gamewindow.blit(head_img, pos)
            elif i==0:
                next_x, next_y = snake_list[1]

                dx=next_x-x
                dy=next_y-y
                if dx==1:
                    rotate_tail=pygame.transform.rotate(tail_img,180)
                elif dy==1:
                    rotate_tail=pygame.transform.rotate(tail_img,90)
                elif dy==-1:
                    rotate_tail=pygame.transform.rotate(tail_img,270)
                elif dx==-1:
                    rotate_tail=tail_img
                else:
                    rotate_tail=tail_img
                gamewindow.blit(rotate_tail, pos)
            else:
                gamewindow.blit(middle_img, pos)

    global Exit_game

    # main game loop
    while not Exit_game:

        # game over
        if Game_over:
            screen_x, screen_y = pygame.display.get_surface().get_size()
            resized_gameover_img = pygame.transform.scale(gameover_img, (screen_x, screen_y))
            gamewindow.blit(resized_gameover_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return game_loop()

        else:
            for event in pygame.event.get():
                # for quit
                if event.type == pygame.QUIT:
                    Exit_game = True

                # for pressing arrow key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and not velocity_x == -1:
                        velocity_x = +1
                        velocity_y = 0
                    if event.key == pygame.K_LEFT and not velocity_x == 1:
                        velocity_x = -1
                        velocity_y = 0
                    if event.key == pygame.K_UP and not velocity_y == 1:
                        velocity_y = -1
                        velocity_x = 0
                    if event.key == pygame.K_DOWN and not velocity_y == -1:
                        velocity_y = +1
                        velocity_x = 0
                    
                    if event.key == pygame.K_d and not velocity_x == -1:
                        velocity_x = +1
                        velocity_y = 0
                    if event.key == pygame.K_a and not velocity_x == 1:
                        velocity_x = -1
                        velocity_y = 0
                    if event.key == pygame.K_w and not velocity_y == 1:
                        velocity_y = -1
                        velocity_x = 0
                    if event.key == pygame.K_s and not velocity_y == -1:
                        velocity_y = +1
                        velocity_x = 0
                    # cheatcode
                    if event.key == pygame.K_q:
                        score += 10
            base_delay=5
            move_delay = max(2, base_delay- score // 90)
            move_counter += 1

            if move_counter >= move_delay:
                move_counter = 0
                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y

                head = [snake_x, snake_y]
                snake_list.append(head)

                if len(snake_list) > snake_length:
                    del snake_list[0]
                if head in snake_list[:-1]:
                    Game_over = True
                    gameover_sound.play()

                if snake_x < 0 or snake_y < 0 or snake_x >= grid_x or snake_y >= grid_y:
                    Game_over = True
                    gameover_sound.play()

            # giving bg colour
            gamewindow.fill(light_blue)
            for x in range(0, screen_x, cell_size):
                pygame.draw.line(gamewindow, light_grey, (x, 0), (x, screen_y))
            for y in range(0, screen_y, cell_size):
                pygame.draw.line(gamewindow, light_grey, (0, y), (screen_x, y))

            # food property
            gamewindow.blit(apple_img, (food_x*cell_size, food_y*cell_size))
            # making food eat
            if snake_x == food_x and snake_y == food_y:
                score += 10
                # print(score)
                food_x = random.randint(0, grid_x - 1)
                food_y = random.randint(0, grid_y - 1)
                snake_length += 1
                eat_sound.play()

            # adding score
            if score > int(high_s):
                high_s = score
            display_screen("Score: " + str(score), green, 100, 5)
            display_screen("HIGH SCORE: " + str(high_s), green, 700, 5)

            # increase length






            plot_snake(gamewindow, snake_list)

            if len(snake_list) > snake_length:
                del snake_list[0]


            # making of snake
        with open("hi.txt", "w") as f:
            f.write(str(high_s))
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome_screen()