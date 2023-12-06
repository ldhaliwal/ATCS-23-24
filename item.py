import pygame
import random
from fsm import FSM

# Code generated by ChatGPT and edited by Liliana Dhaliwal
# Some code written by Liliana Dhaliwal
# Comments by Liliana Dhaliwal
class Item(pygame.sprite.Sprite):
    MOVE_RANDOMLY = "m_r"
    CAUGHT = "c"
    RUN_AWAY = "r_a"

    MAX_SPEED = 4

    def __init__(self, screen_width, screen_height):
        super().__init__()

        # Intializes the item
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 30)
        self.rect.y = random.randint(0, screen_height - 30)

        self.x_change = self.MAX_SPEED - random.randint(0, 2 * self.MAX_SPEED)
        self.y_change = self.MAX_SPEED - random.randint(0, 2 * self.MAX_SPEED) 

        self.visible = True

        self.speed = 3
        self.direction = random.choice([-1, 1])  

        self.fsm = FSM(self.MOVE_RANDOMLY)
        self.init_fsm()

    # Code writen by Liliana Dhaliwal
    def init_fsm(self):
        self.fsm.add_transition("caught", self.MOVE_RANDOMLY, self.caught, self.CAUGHT)
        self.fsm.add_transition(None, self.MOVE_RANDOMLY, self.move_randomly, self.MOVE_RANDOMLY)
        # self.fsm.add_transition('??', self.MOVE_RANDOMLY, None, self.RUN_AWAY)
        # self.fsm.add_transition('??', self.RUN_AWAY, None, self.CAUGHT)

    # Code writen by Liliana Dhaliwal  
    def get_state(self):
        return self.fsm.current_state
    
    # Code writen by Liliana Dhaliwal
    def update(self, input = None):   
        if self.get_state() != "c":
            self.fsm.process(input)

    def caught(self):
        self.visible = False

    # Code written by Liliana Dhaliwal
    def move_randomly(self):
        # Creates a 1-in-7 probability that the direction is changed.
        if random.randint(0, 6) == 1:
            self.x_change += random.randint(-self.MAX_SPEED, self.MAX_SPEED)

            self.x_change = min(self.x_change, self.MAX_SPEED)
            self.x_change = max(self.x_change, -self.MAX_SPEED)
            
            self.y_change += random.randint(-self.MAX_SPEED, self.MAX_SPEED)

            self.y_change = min(self.y_change, self.MAX_SPEED)
            self.y_change = max(self.y_change, -self.MAX_SPEED)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        if (self.rect.x <= 0 and self.x_change < 0) or (self.rect.x  >= 800 - 30):
            self.x_change = -self.x_change

        if (self.rect.y <= 0 and self.y_change < 0) or (self.rect.y >= 600 - 30):
            self.y_change = -self.y_change

    def run_away(self):
        pass
