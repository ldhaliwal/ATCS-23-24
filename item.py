import pygame
import random
import math
from fsm import FSM

# Code generated by ChatGPT and edited by Liliana Dhaliwal
# Some code written by Liliana Dhaliwal
# Comments by Liliana Dhaliwal
class Item(pygame.sprite.Sprite):
    # Constants
    MOVE_RANDOMLY = "m_r"
    CAUGHT = "c"
    RUN_AWAY = "r_a"

    MAX_SPEED = 4

    def __init__(self, game, player, screen_width, screen_height):
        super().__init__()

        # Intializes the item
        image_num = random.randint(0, 4) + 1
        self.image = pygame.image.load("Assets/items/item_" + str(image_num) + ".png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 30)
        self.rect.y = random.randint(0, screen_height - 30)

        self.x_change = self.MAX_SPEED - random.randint(0, 2 * self.MAX_SPEED)
        self.y_change = self.MAX_SPEED - random.randint(0, 2 * self.MAX_SPEED) 

        self.visible = True

        self.game = game
        self.player = player

        self.speed = 3
        self.direction = random.choice([-1, 1])  

        self.fsm = FSM(self.MOVE_RANDOMLY)
        self.init_fsm()

    # Code writen by Liliana Dhaliwal
    # Adds all transitions to the items' FSM
    def init_fsm(self):
        self.fsm.add_transition("caught", self.MOVE_RANDOMLY, self.caught, self.CAUGHT)
        self.fsm.add_transition(None, self.MOVE_RANDOMLY, self.move_randomly, self.MOVE_RANDOMLY)
        self.fsm.add_transition("run away", self.MOVE_RANDOMLY, self.run_away, self.RUN_AWAY)
        self.fsm.add_transition("run away", self.RUN_AWAY, self.run_away, self.RUN_AWAY)
        self.fsm.add_transition("caught", self.RUN_AWAY, self.caught, self.CAUGHT)

    # Code writen by Liliana Dhaliwal 
    # Returns the current state of the item
    def get_state(self):
        return self.fsm.current_state
    
    # Code writen by Liliana Dhaliwal
    # Sends the current state of the item into the FSM to update the state accordingly 
    def update(self, input = None):   
        if self.game.score >= 5 and input != "caught":
            input = "run away"
        if self.get_state() != "c":
            self.fsm.process(input)

    # Code written by Liliana Dhaliwal
    # Increase the score and hide the item when it is caught
    def caught(self):
        self.game.score += 1
        self.visible = False

    # Code written by Liliana Dhaliwal
    # Changes the item's x and y coordinates to move randomly 
    def move_randomly(self):
        # Creates a 1 in 7 chance that the direction is changed
        if random.randint(0, 6) == 1:
            self.x_change += random.randint(-self.MAX_SPEED, self.MAX_SPEED)

            self.x_change = min(self.x_change, self.MAX_SPEED)
            self.x_change = max(self.x_change, -self.MAX_SPEED)
            
            self.y_change += random.randint(-self.MAX_SPEED, self.MAX_SPEED)

            self.y_change = min(self.y_change, self.MAX_SPEED)
            self.y_change = max(self.y_change, -self.MAX_SPEED)

        # Updates the items' x and y values
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        # Keeps the items within the dimensions of the screen
        if (self.rect.x <= 0 and self.x_change < 0) or (self.rect.x  >= 800 - 30):
            self.x_change = -self.x_change

        if (self.rect.y <= 150 and self.y_change < 0) or (self.rect.y >= 600 - 30):
            self.y_change = -self.y_change

    
    # Changes the item's x and y coordinates to move away from the player
    def run_away(self):
        # Calculates the distance between the item and the player
        distance = math.sqrt((self.player.rect.x - self.rect.x) ** 2 + (self.player.rect.y - self.rect.y) ** 2)

        # Calculates the direction to move away from the player
        dx = (self.rect.x - self.player.rect.x) / distance
        dy = (self.rect.y - self.player.rect.y) / distance

        # Keeps the items within the dimensions of the screen
        if (self.rect.x <= 0 and dx < 0) or (self.rect.x  >= 800 - 30):
            dx = -dx

        if (self.rect.y <= 150 and dy < 0) or (self.rect.y >= 600 - 30):
            dy = -dy 
        
        # Updates the item's position based on the direction and speed
        self.rect.x += self.speed * dx
        self.rect.y += self.speed * dy
