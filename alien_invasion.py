import sys # Needed to quit the game.
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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
        # To be used in a future update to allow the game to be played in fullscreen
        # Note: Pygame does not have a default method of exiting the game 
        # while in full screen, so ensure there is at least one working method 
        # of exiting the game before uncommenting the code below 
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Get rid of bullets that have disappeared.
            # Note: A copy of the bullet group is created in the for loop 
            # so that the bullets can be removed from the bullet group while 
            # the loop is running otherwise the the bullets will not be able 
            # to be removed using this method.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)   

            self._update_screen()
            
            # Set the desired frame rate, 
            # should work well on most systems but may need to be removed 
            # on select systems to improve game performance. 
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            # Fires if the user clicks the game windows exit button.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # Make the most recently drawn screen visable.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvaion()
    ai.run_game()