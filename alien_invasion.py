import sys # Needed to quit the game.
import pygame # Needed to run the game.
from settings import Settings
from ship import Ship

class AlienInvaion:
    """Main class to manage game game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        # Creates a clock instance that is used to ensure a steady frame rate. 
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        # Sets the game window size and caption 
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            # Sets the desired frame rate, 
            # should work well on most systems but may needed to be removed 
            # on select systems for the frame rate to run smoothly. 
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            # Fires if the user clicks the game windows exit button.
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visable.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvaion()
    ai.run_game()