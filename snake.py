import pygame
import time
import random

pygame.init()

bgcolor = (56,128,4)
red = (255,0,0)
black = (0,0,0)
white = (250,250,250)
snkae = (182,180,40)
purple= (128,0,128)

display_width = 800
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('')

clock = pygame.time.Clock()

block_size = 10
FPS = 30
direction = "right"

font = pygame.font.SysFont(None, 25)
smallfont = pygame.font.SysFont("Comicsansms",25)
medfont = pygame.font.SysFont("Comicsansms",40)
largefont = pygame.font.SysFont("Comicsansms",80)

def game_intro():
    intro = True
    while True:
        gameDisplay.fill(black)
        message_to_screen("Welcome",purple,-100,size="large")
        message_to_screen("I Hope You Will Like It","White",10)
        message_to_screen("Press Space To Play And Q To Quit",  "White",100)
        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    gameLoop()

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, snkae, [XnY[0],XnY[1],block_size,block_size])

def text_Objects(text,color,size):
    if size == 'small':
        textSurface = smallfont.render(text,True,color)
    elif size == 'medium':
        textSurface = medfont.render(text,True,color)
    elif size == 'large':
        textSurface = largefont.render(text,True,color)

    return textSurface,textSurface.get_rect()


def message_to_screen(msg,color,y_displace=0,size="small"):
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2, display_height/2])

    textSurf , textRect = text_Objects(msg,color,size)
    textRect.center = (display_width/2),(display_height/2) + y_displace
    gameDisplay.blit(textSurf,textRect)

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0
    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game over",  red, -50,size = "large" )
            message_to_screen("Press Space To Play and Q To Quit",white,50, size ="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(bgcolor)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size,block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        snake(block_size, snakeList)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        score(snakeLength - 1)

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
            snakeLength = snakeLength + 1

        clock.tick(FPS)

    pygame.quit()
    quit()

def score(score):
    text = smallfont.render("Your Score is : "+str(score),True,"White")
    gameDisplay.blit(text,[0,0])

game_intro()
gameLoop()
