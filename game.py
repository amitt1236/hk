import pygame
import random
import sys

# 0 == NONE, 1 == RIGHT, 2 == LEFT, 3 ==  ENTER

# TODO: get actual stress level (AMIT&ARIEL!). In the meantime it is number, can be turned into a bool.
def get_stress_level():
    return 10

class renderer():
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Menu Example")
        self.font = pygame.font.Font(None, 36)

        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.WHITE = (255, 255, 255)

        stress_threshold = 50
        stress_level = get_stress_level()
        self.is_stressed = stress_level > stress_threshold

        # TODO: change option names of the menus
        self.option_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
        options = [
            [(0, 0, self.screen_width // 2, self.screen_height // 2), self.option_names[0], self.RED],
            [(self.screen_width // 2, 0, self.screen_width // 2, self.screen_height // 2), self.option_names[1], self.GREEN],
            [(0, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), self.option_names[2], self.BLUE],
            [(self.screen_width // 2, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), self.option_names[3], self.YELLOW]
        ]

        self.current_menu = options
        self.current_pos = 0
        self.is_ENTER = 0

    def render_gui(self, gaze_input):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if gaze_input != 3:
            self.current_pos = (self.current_pos + gaze_input) % 4
        else:
            self.is_ENTER = 1 if gaze_input == 3 else 0

        if self.is_ENTER:
            if self.option_names[self.current_pos] == self.option_names[0]:
                if self.is_stressed:
                    is_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                    self.current_menu = [
                        [(0, 0, self.screen_width // 2, self.screen_height // 2), is_stress_names[0], self.RED],
                        [(self.screen_width // 2, 0, self.screen_width // 2, self.screen_height // 2), is_stress_names[1], self.GREEN],
                        [(0, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), is_stress_names[2], self.BLUE],
                        [(self.screen_width // 2, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), is_stress_names[3], self.YELLOW]
                    ]
                else:
                    no_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                    self.current_menu = [
                        [(0, 0, self.screen_width // 2, self.screen_height // 2), no_stress_names[0], self.RED],
                        [(self.screen_width // 2, 0, self.screen_width // 2, self.screen_height // 2), no_stress_names[1], self.GREEN],
                        [(0, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), no_stress_names[2], self.BLUE],
                        [(self.screen_width // 2, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), no_stress_names[3], self.YELLOW]
                    ]
            elif self.option_names[self.current_pos] == self.option_names[1]:
                if self.is_stressed:
                    is_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                    self.current_menu = [
                        [(0, 0, self.screen_width // 2, self.screen_height // 2), is_stress_names[0], self.RED],
                        [(self.screen_width // 2, 0, self.screen_width // 2, self.screen_height // 2), is_stress_names[1], self.GREEN],
                        [(0, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), is_stress_names[2], self.BLUE],
                        [(self.screen_width // 2, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), is_stress_names[3], self.YELLOW]
                    ]
                else:
                    no_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                    self.current_menu = [
                        [(0, 0, self.screen_width // 2, self.screen_height // 2), no_stress_names[0], self.RED],
                        [(self.screen_width // 2, 0, self.screen_width // 2, self.screen_height // 2), no_stress_names[1], self.GREEN],
                        [(0, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), no_stress_names[2], self.BLUE],
                        [(self.screen_width // 2, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), no_stress_names[3], self.YELLOW]
                    ]
            elif self.option_names[self.current_pos] == self.option_names[2]:
                if self.is_stressed:
                    is_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                    self.current_menu = [
                        [(0, 0, self.screen_width // 2, self.screen_height // 2), is_stress_names[0], self.RED],
                        [(self.screen_width // 2, 0, self.screen_width // 2, self.screen_height // 2), is_stress_names[1], self.GREEN],
                        [(0, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), is_stress_names[2], self.BLUE],
                        [(self.screen_width // 2, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), is_stress_names[3], self.YELLOW]
                    ]
                else:
                    no_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                    self.current_menu = [
                        [(0, 0, self.screen_width // 2, self.screen_height // 2), no_stress_names[0], self.RED],
                        [(self.screen_width // 2, 0, self.screen_width // 2, self.screen_height // 2), no_stress_names[1], self.GREEN],
                        [(0, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), no_stress_names[2], self.BLUE],
                        [(self.screen_width // 2, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), no_stress_names[3], self.YELLOW]
                    ]
            elif self.option_names[self.current_pos] == self.option_names[3]:
                if self.is_stressed:
                    is_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                    self.current_menu = [
                        [(0, 0, self.screen_width // 2, self.screen_height // 2), is_stress_names[0], self.RED],
                        [(self.screen_width // 2, 0, self.screen_width // 2, self.screen_height // 2), is_stress_names[1], self.GREEN],
                        [(0, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), is_stress_names[2], self.BLUE],
                        [(self.screen_width // 2, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), is_stress_names[3], self.YELLOW]
                    ]
                else:
                    no_stress_names = ["Option 0", "Option 1", "Option 2", "Option 3"]
                    self.current_menu = [
                        [(0, 0, self.screen_width // 2, self.screen_height // 2), no_stress_names[0], self.RED],
                        [(self.screen_width // 2, 0, self.screen_width // 2, self.screen_height // 2), no_stress_names[1], self.GREEN],
                        [(0, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), no_stress_names[2], self.BLUE],
                        [(self.screen_width // 2, self.screen_height // 2, self.screen_width // 2, self.screen_height // 2), no_stress_names[3], self.YELLOW]
                    ]

        self.screen.fill(self.BLACK)

        for i, (rect, text, color) in enumerate(self.current_menu):
            pygame.draw.rect(self.screen, color, rect)
            if i == self.current_pos:
                pygame.draw.rect(self.screen, self.BLACK, rect, 20)
            text_surface = self.font.render(text, True, self.BLACK)
            text_rect = text_surface.get_rect(center=(rect[0] + rect[2] / 2, rect[1] + rect[3] / 2))
            self.screen.blit(text_surface, text_rect)

        pygame.display.flip()
