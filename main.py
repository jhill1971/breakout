# Breakout
#  Import and initialize Pygame
import pygame
# Import necessary modules
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()

#  Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (50, 205, 50)
BLUE = (0, 0, 255)

# Game Variables
score = 0
lives = 3

# Open a game window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")

# List of sprites to be used in the game
all_sprites = pygame.sprite.Group()

# Create Paddle Object
paddle = Paddle(BLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# Create ball object
ball = Ball(WHITE, 10, 10)
ball.rect.x = 355
ball.rect.y = 195

# Create the brick objects
bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 60
    all_sprites.add(brick)
    bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 100
    all_sprites.add(brick)
    bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 140
    all_sprites.add(brick)
    bricks.add(brick)
for i in range(7):
    brick = Brick(GREEN, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 180
    all_sprites.add(brick)
    bricks.add(brick)

# Add objects to list of sprites
all_sprites.add(paddle)  # Add paddle to list of sprites
all_sprites.add(ball)  # Add ball to list of sprites

# Set up main program loop
""" 
The main program loop has three main sections:
Capturing keyboard or mouse events
Executing the game logic
Refreshing the screen - redrawing sprites and the game field
"""
gameplay = True  # Loop is active until exit.

clock = pygame.time.Clock()  # Clock determines the refresh rate

# Main Loop Begins
while gameplay:
    # Event Loop
    for event in pygame.event.get():  # Player did something
        if event.type == pygame.QUIT:  # If user selects close
            gameplay = False  # Flags that game is finished and exits loop

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # pressing x quits the game
                gameplay = False  # Flags that game is finished and exits loop

    # Using the arrow keys to control the paddle movement.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left(5)
    if keys[pygame.K_RIGHT]:
        paddle.move_right(5)

    # GAME LOGIC HERE
    all_sprites.update()

    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            # Game Over
            font = pygame.font.SysFont("OCR A Extended", 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            gameplay = False

    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    # Detect ball/paddle collision
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    # Detect ball/wall collision
    brick_collisions = pygame.sprite.spritecollide(ball, bricks, False)
    for brick in brick_collisions:
        ball.bounce()
        score += 1
        brick.kill()
        if len(bricks) == 0:
            font = pygame.font.SysFont("OCR A Extended", 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            gameplay = False

    # DRAWING CODE HERE

    # Color fill the game field.
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [0, 40], [800, 40], 2)

    # Display Current Score and Lives
    font = pygame.font.SysFont("OCR A Extended", 34)
    text = font.render("SCORE: " + str(score), 1, WHITE)
    screen.blit(text, (20, 8))
    text = font.render("LIVES: " + str(lives), 1, WHITE)
    screen.blit(text, (610, 8))

    # Draw sprites
    all_sprites.draw(screen)

    # Screen Update
    pygame.display.flip()

    # Refresh Rate 60FPS
    clock.tick(60)

# Stop game engine at exit from game loop
pygame.quit()

