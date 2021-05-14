import pygame
import random

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # Ball: basic attributes
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [random.randint(4, 8), random.randint(-8, 8)]  # randomly selected x,y coordinates

        # Get the dimensions of the image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8, 8)
