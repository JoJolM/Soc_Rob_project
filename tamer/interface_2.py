import os
import pygame

white = (255, 255, 255)
red = (255,0,0)
green = (0,255,0)

class Interface:
    """ Pygame interface for training TAMER """

    def __init__(self, action_map):
        self.action_map = action_map
        pygame.init()
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.font2 = pygame.font.Font("freesansbold.ttf", 14)

        # set position of pygame window (so it doesn't overlap with gym)
        os.environ["SDL_VIDEO_WINDOW_POS"] = "1000,100"
        os.environ["SDL_VIDEO_CENTERED"] = "0"

        self.screen = pygame.display.set_mode((400, 100))
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

    action = 0
    def show_choice(self, last_action, state = 0):
        """
        Show agent's action on pygame screen
        Args:
            action: numerical action (for MountainCar environment only currently)
        """
        action = last_action
        choice = True
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
                        #pygame.time.wait(1000)

            pygame.display.update(area)

            area = self.screen.fill((0, 0, 0))
            # pygame.display.update(area)
            text = self.font.render(self.action_map[action], True, white)
            text_rect = text.get_rect()
            text_rect.center = (100, 50)
            area = self.screen.blit(text, text_rect)


            if state[1] < 0:
                dire = "going left"
                color = red

            elif state[1] > 0:
                dire = "going right"
                color = green

            elif state[1] == 0:
                dire = "No speed"
                color = white

            spd = str(state[1])

            text_2 = self.font2.render(dire, True, color)
            text_2_rect = text.get_rect()
            text_2_rect.center = (300, 25)
            area = self.screen.blit(text_2,text_2_rect)

            text_3 = self.font2.render(spd, True, color)
            text_3_rect = text.get_rect()
            text_3_rect.center = (300, 75)
            area = self.screen.blit(text_3,text_3_rect)

            pygame.display.flip()

            # if choice == False:
            #     pygame.

        return action