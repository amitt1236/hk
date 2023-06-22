import pygame
import random
import sys

# 0 == NONE, 1 == RIGHT, 2 == LEFT, 3 ==  ENTER

# TODO: get actual input from eye control (AMIT!)
def get_amit_input():
    x = random.randint(1, 1)
    print(x)
    return x


# TODO: get actual stress level (AMIT&ARIEL!). In the meantime it is number, can be turned into a bool.
def get_stress_level():
    return 10


def update_pos(current_pos):
    amit_input = get_amit_input()
    new_pos = current_pos
    is_ENTER = False
    if current_pos == 0:
        if amit_input == 0:
            new_pos = 0
        if amit_input == 1:
            new_pos = 1
        if amit_input == 2:
            new_pos = 3
        if amit_input == 3:
            new_pos = current_pos
            is_ENTER = True

    if current_pos == 1:
        if amit_input == 0:
            new_pos = 1
        if amit_input == 1:
            new_pos = 2
        if amit_input == 2:
            new_pos = 0
        if amit_input == 3:
            new_pos = current_pos
            is_ENTER = True

    if current_pos == 2:
        if amit_input == 0:
            new_pos = 2
        if amit_input == 1:
            new_pos = 3
        if amit_input == 2:
            new_pos = 1
        if amit_input == 3:
            new_pos = current_pos
            is_ENTER = True

    if current_pos == 3:
        if amit_input == 0:
            new_pos = 3
        if amit_input == 1:
            new_pos = 0
        if amit_input == 2:
            new_pos = 2
        if amit_input == 3:
            new_pos = current_pos
            is_ENTER = True

    return new_pos, is_ENTER


pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu Example")
font = pygame.font.Font(None, 36)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

stress_threshold = 50
stress_level = get_stress_level()
is_stressed = stress_level > stress_threshold


# TODO: change option names of the menus
option_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
options = [
    [(0, 0, screen_width // 2, screen_height // 2), option_names[0], RED],
    [(screen_width // 2, 0, screen_width // 2, screen_height // 2), option_names[1], GREEN],
    [(0, screen_height // 2, screen_width // 2, screen_height // 2), option_names[2], BLUE],
    [(screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2), option_names[3], YELLOW]
]

current_menu = options
current_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    new_pos, is_ENTER = update_pos(current_pos)

    if is_ENTER:
        if option_names[current_pos] == option_names[0]:
            if is_stressed:
                is_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                current_menu = [
                    [(0, 0, screen_width // 2, screen_height // 2), is_stress_names[0], RED],
                    [(screen_width // 2, 0, screen_width // 2, screen_height // 2), is_stress_names[1], GREEN],
                    [(0, screen_height // 2, screen_width // 2, screen_height // 2), is_stress_names[2], BLUE],
                    [(screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2), is_stress_names[3], YELLOW]
                ]
            else:
                no_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                current_menu = [
                    [(0, 0, screen_width // 2, screen_height // 2), no_stress_names[0], RED],
                    [(screen_width // 2, 0, screen_width // 2, screen_height // 2), no_stress_names[1], GREEN],
                    [(0, screen_height // 2, screen_width // 2, screen_height // 2), no_stress_names[2], BLUE],
                    [(screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2), no_stress_names[3], YELLOW]
                ]
        elif option_names[current_pos] == option_names[1]:
            if is_stressed:
                is_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                current_menu = [
                    [(0, 0, screen_width // 2, screen_height // 2), is_stress_names[0], RED],
                    [(screen_width // 2, 0, screen_width // 2, screen_height // 2), is_stress_names[1], GREEN],
                    [(0, screen_height // 2, screen_width // 2, screen_height // 2), is_stress_names[2], BLUE],
                    [(screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2), is_stress_names[3], YELLOW]
                ]
            else:
                no_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                current_menu = [
                    [(0, 0, screen_width // 2, screen_height // 2), no_stress_names[0], RED],
                    [(screen_width // 2, 0, screen_width // 2, screen_height // 2), no_stress_names[1], GREEN],
                    [(0, screen_height // 2, screen_width // 2, screen_height // 2), no_stress_names[2], BLUE],
                    [(screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2), no_stress_names[3], YELLOW]
                ]
        elif option_names[current_pos] == option_names[2]:
            if is_stressed:
                is_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                current_menu = [
                    [(0, 0, screen_width // 2, screen_height // 2), is_stress_names[0], RED],
                    [(screen_width // 2, 0, screen_width // 2, screen_height // 2), is_stress_names[1], GREEN],
                    [(0, screen_height // 2, screen_width // 2, screen_height // 2), is_stress_names[2], BLUE],
                    [(screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2), is_stress_names[3], YELLOW]
                ]
            else:
                no_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                current_menu = [
                    [(0, 0, screen_width // 2, screen_height // 2), no_stress_names[0], RED],
                    [(screen_width // 2, 0, screen_width // 2, screen_height // 2), no_stress_names[1], GREEN],
                    [(0, screen_height // 2, screen_width // 2, screen_height // 2), no_stress_names[2], BLUE],
                    [(screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2), no_stress_names[3], YELLOW]
                ]
        elif option_names[current_pos] == option_names[3]:
            if is_stressed:
                is_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                current_menu = [
                    [(0, 0, screen_width // 2, screen_height // 2), is_stress_names[0], RED],
                    [(screen_width // 2, 0, screen_width // 2, screen_height // 2), is_stress_names[1], GREEN],
                    [(0, screen_height // 2, screen_width // 2, screen_height // 2), is_stress_names[2], BLUE],
                    [(screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2), is_stress_names[3], YELLOW]
                ]
            else:
                no_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                current_menu = [
                    [(0, 0, screen_width // 2, screen_height // 2), no_stress_names[0], RED],
                    [(screen_width // 2, 0, screen_width // 2, screen_height // 2), no_stress_names[1], GREEN],
                    [(0, screen_height // 2, screen_width // 2, screen_height // 2), no_stress_names[2], BLUE],
                    [(screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2), no_stress_names[3], YELLOW]
                ]

    current_pos = new_pos

    screen.fill(BLACK)

    for i, (rect, text, color) in enumerate(current_menu):
        pygame.draw.rect(screen, color, rect)
        if i == current_pos:
            pygame.draw.rect(screen, BLACK, rect, 20)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(rect[0] + rect[2] / 2, rect[1] + rect[3] / 2))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()
