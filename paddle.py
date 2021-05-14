import pygame

BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    """ This class represents the player's paddle. It derives from pygame's Sprite class"""

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass the color of the paddle and its x,y position, width, and height
        # Set the background color and set it to transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw a rectangular paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Get the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def move_left(self, pixels):
        self.rect.x -= pixels
        # Check that paddle is not leaving the play area
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pixels):
        self.rect.x += pixels
        # Check that paddle is not leaving the play area
        if self.rect.x > 700:
            self.rect.x = 700
