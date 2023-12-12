import pygame
from player import Player
from item import Item

# Code generated by ChatGPT and edited by Liliana Dhaliwal
# Some code written by Liliana Dhaliwal
# Comments by Liliana Dhaliwal
class Game:
    def __init__(self):
        pygame.init()
        
        # Initializes the game
        self.screen_width = 800
        self.screen_height = 600
        
        self.image = pygame.image.load("Assets/background.png")

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Packing Game")

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(self.screen_width, self.screen_height)
        self.items = pygame.sprite.Group()

        self.score = 0

        # Creates items
        for i in range(10):
            self.items.add(Item(self, self.player, self.screen_width, self.screen_height))

    # Runs the game
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        self.player.update(keys)

    # Updates the items' states and positions
    def update(self):
        # Checks if the game is over and acts accordingly
        game_over = True
        for item in self.items:
            if item.get_state() != "c":
                game_over = False

        if game_over is True:
            self.image = pygame.image.load("Assets/gameover.png")
            self.running = False
        
        # Updates items
        for item in self.items:
            item.update()

        # Checks which items have been caught by the player
        collided_items = pygame.sprite.spritecollide(self.player, self.items, False)

        # Updates the state for all caught items
        for item in collided_items:
            item.update("caught")

    # Draws the game
    def render(self):
        # Draws background 
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.image, (0, 0))
        
        # Draws player
        self.screen.blit(self.player.image, self.player.rect)

        # Draws all items that are still visible  
        for item in self.items:
            if item.visible == True:
                self.screen.blit(item.image, item.rect)

        pygame.display.flip()
        self.clock.tick(30)

    # Quits the game
    def cleanup(self):
        pygame.time.wait(3000)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
    game.cleanup()
