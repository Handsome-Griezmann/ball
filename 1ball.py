import sys

from item import *

pygame.init()

size = width, height = 1080, 720
faceSpeed = [1, 1]
ballSpeed = [2, 1]
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 120)
backgroundColor = (100, 100, 100)

screen = pygame.display.set_mode(size)

ball = Item("intro_ball.gif", size, ballSpeed)
face = Item("smileyTiny.png", size, faceSpeed)

testSurface = pygame.Surface((50, 50))
testRect = pygame.Rect(0, 0, 50, 50)
test = pygame.draw.rect(testSurface, blue, testRect)

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEMOTION:
            if event.buttons [0] == 1:
                print("left")
            if event.buttons [1] == 1:
                print("middle")
            if event.buttons [2] == 1:
                print("right")
                if pygame.mouse.get_pressed():
                    mouse_position = pygame.mouse.get_pos()
                if (ball.rect.collidepoint(mouse_position)):
                    mouse_position = pygame.mouse.get_rel()

                    ball.move()
                    face.move()

    screen.fill(backgroundColor)
    ball.blit(screen)
    face.blit(screen)
    screen.blit(testSurface, testRect)
    pygame.display.flip()
