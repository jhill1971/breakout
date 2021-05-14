import pygame

BLACK = (0, 0, 0)


class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        # Basic brick attributes
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the brick
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # get the dimensions of the image
        self.rect = self.image.get_rect()
