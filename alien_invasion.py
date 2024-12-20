import sys # Needed so we can quit the game
import pygame # Needed to run the game

class AlienInvaion:
    """Main class to manage game game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        
        # Sets the game window size and caption 
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                # Fires if the user clicks the game windows exit button
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make the most recently drawn screen visable.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvaion()
    ai.run_game()