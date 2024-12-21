import sys # Needed to quit the game
import pygame # Needed to run the game

class AlienInvaion:
    """Main class to manage game game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        # Creates a clock instance that is used to ensure a steady frame rate 
        self.clock = pygame.time.Clock()
        
        # Sets the game window size and caption 
        self.screen = pygame.display.set_mode((900,700))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                # Fires if the user clicks the game windows exit button
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visable.
            pygame.display.flip()
            # Sets the desired frame rate, 
            # should work well on most systems but may needed to be left out 
            # completely on select systems 
            self.clock.tick(60)
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvaion()
    ai.run_game()