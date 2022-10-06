import pygame

# Importation and Initialization
pygame.init()
window = pygame.display.set_mode((1250, 750))
pygame.display.set_caption('Pong')
running = True

# Main variables

P1 = pygame.image.load('player.png')

P2 = pygame.image.load('player.png')

Ball = pygame.image.load('ball.png')

P1Y = 400

P2Y = 400

BallSlope = 1
BallX = 0

Direction = 1

BallIntercept = 0

# Main game loop

while running:

    # Quit detection

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pygame checks if any keys are pressed. Assigns all pressed keys to a list and does an if chain.

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and P1Y > 0:
        P1Y -= 2
    if keys[pygame.K_s] and P1Y < 650:
        P1Y += 2
    if keys[pygame.K_UP] and P2Y > 0:
        P2Y -= 2
    if keys[pygame.K_DOWN] and P2Y < 650:
        P2Y += 2

    # The basic math:

    # Adds (or removes) one on the x scale so the balls moves left or right.
    BallX += Direction

    # Calculates the Y value of the ball with the slope * x value, then add the y intercept.
    BallY = (BallSlope * BallX) + BallIntercept

    # This calculation fixes the Ball coordinates, so they will match correctly on our screen.
    # It adjusts it with the pixel size of the ball and so its origin is centered in the screen.
    BallXDisplayed = BallX + 600
    BallYDisplayed = BallY + 350

    # This is our main if statements, checking if the ball has collided with anything.

    # It first checks the ball's y value; if it collided with the roof or floor.
    if BallYDisplayed <= 0 or BallYDisplayed >= 700:

        # Calculates the new slope via gaining the current slope's negative reciprocal.
        BallSlope = (1 / BallSlope) * -1

        # Just a print statement used when troubleshooting.
        print('Roof/Floor')

        # Calculates the new y intercept needed. This is very necessary as otherwise, with the slope being
        # completely different, the y value equation will bring a completely new y value.
        # So, we compensate with a y value that will make sure the ball continues in the location
        # it was in, before the slope change.
        BallIntercept = BallY - (BallX * BallSlope)

    # Now it check the ball's x value; if it either collided or went past a paddle.
    elif BallXDisplayed <= 150 or BallXDisplayed >= 1050:

        # First it assigns, depending on which side of the screen it hit, if it needs to check
        # Player 1's paddle or Player 2's paddle.
        # It then creates a y coord range from where if the ball hit, can bounce away.
        # Otherwise, the game (currently) just ends.
        if BallXDisplayed <= 150:
            BottomPY = P1Y - 50
            TopPY = P1Y + 150
        else:
            BottomPY = P2Y - 50
            TopPY = P2Y + 150
        # If statement for if the ball hit a paddle.
        if BottomPY < BallYDisplayed < TopPY:

            # Reverses the direction, by changing which way the x value is changed each loop.
            Direction *= -1

            # Calculates the new slope via gaining the current slope's negative reciprocal.
            BallSlope = (1 / BallSlope) * -1

            # Just a print statement used when troubleshooting.
            print('Paddle')

            # Same explanation as before for why we update the ball's y intercept.
            BallIntercept = BallY - (BallX * BallSlope)
        else:
            # If the ball hit a player side but didn't hit a paddle, the game ends (with break statement).
            break

    # Loading statements; load background and other objects based on the coordinates we calculated.
    window.fill((0, 0, 0))
    window.blit(Ball, (BallXDisplayed, BallYDisplayed))
    window.blit(P1, (100, P1Y))
    window.blit(P2, (1100, P2Y))

    # Update the pygame display.
    pygame.display.update()

# If the game loop ends, just prints 'Game Over'
print('GAME OVER')
