import os
import pygame


class Interface:
    """ Pygame interface for training TAMER """

    def __init__(self, action_map, state=0):
        self.action_map = action_map
        pygame.init()
        self.font = pygame.font.Font("freesansbold.ttf", 32)

        # set position of pygame window (so it doesn't overlap with gym)
        os.environ["SDL_VIDEO_WINDOW_POS"] = "1000,100"
        os.environ["SDL_VIDEO_CENTERED"] = "0"

        self.screen = pygame.display.set_mode((200, 100))
        area = self.screen.fill((0, 0, 0))
        pygame.display.update(area)

    def get_scalar_feedback(self):
        """
        Get human input. 'W' key for positive, 'A' key for negative.
        Returns: scalar reward (1 for positive, -1 for negative)
        """
        reward = 0
        area = None
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    area = self.screen.fill((0, 255, 0))
                    reward = 1
                    break
                elif event.key == pygame.K_a:
                    area = self.screen.fill((255, 0, 0))
                    reward = -1
                    break
        pygame.display.update(area)
        return reward

    def show_choice(self, state = 0):
        """
        Show agent's action on pygame screen
        Args:
            action: numerical action (for MountainCar environment only currently)
        """
        choice = True
        action = 0
        while choice : 
            area = None
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        action = 0
                    elif event.key == pygame.K_t:
                        action = 1
                    elif event.key == pygame.K_y:
                        action = 2
                        
                    elif event.key == pygame.K_m:
                        area = self.screen.fill((0, 255, 0))
                        choice = False
                        pygame.display.update(area)
                        pygame.time.wait(1000)

            pygame.display.update(area)

            area = self.screen.fill((0, 0, 0))
            pygame.display.update(area)
            text = self.font.render(self.action_map[action], True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (100, 50)
            area = self.screen.blit(text, text_rect)
            pygame.display.update(area)

            # if choice == False:
            #     pygame.

        return self.action_map[action]


### test 
MOUNTAINCAR_ACTION_MAP = {0: 'left', 1: 'none', 2: 'right'}
disp = Interface(MOUNTAINCAR_ACTION_MAP)
act = disp.show_choice()

print(act)

