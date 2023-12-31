import pygame

# Code generated by ChatGPT and edited by Liliana Dhaliwal
# Comments by Liliana Dhaliwal
class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        # Intializes the player
        self.image = pygame.image.load("Assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed = 5

    # Moves the player based on user input and keeps player within the bounds of the window
    def update(self, keys):
        if keys[pygame.K_LEFT] and (self.rect.x - self.speed) > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and (self.rect.x + self.speed + 50) < self.screen_width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and (self.rect.y - self.speed - 150) > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and (self.rect.y + self.speed + 75) < self.screen_height:
            self.rect.y += self.speed
