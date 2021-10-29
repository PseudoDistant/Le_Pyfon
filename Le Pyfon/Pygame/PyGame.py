from time import sleep
import pygame

# Initialize le Pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Welcome to my very short PyGame! ^^")
isGameRunning = True
scene0 = pygame.image.load("Scene0.png")
scene1 = pygame.image.load("Scene1.png")
scene1key = pygame.image.load("Scene1Key.png")
scene2 = pygame.image.load("Scene2.png")
scene3 = pygame.image.load("Scene3.png")
scene3win = pygame.image.load("Scene3Open.png")
currentScene = scene0
font = pygame.font.SysFont("Arial", 16)
timer = pygame.time.Clock()

Location = 0
hasShovel = False
hasKey = False

sleep(2)

def refreshScreen():
    # Renders text in white color
    text = font.render(string, True, (255, 255, 255))
    text2 = font.render(string2, True, (255, 255, 255))
    text_rect = text.get_rect()
    text2_rect = text2.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text2_rect.centerx = screen.get_rect().centerx
    text_rect.y = 550
    text2_rect.y = 575
    screen.fill((0, 0, 0))
    screen.blit(currentScene, (0, 0))
    screen.blit(text, text_rect)
    screen.blit(text2, text2_rect)
    pygame.display.update()

while isGameRunning:
    string = "default"
    string2 = "default"
    # Makes the game close if the Pygame window closes.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
    if Location == 0:
        string = "You are at some unknown place in the middle of nowhere."
        string2 = "To your left is a patch of dirt, to your right is a pile of tools, and in front of you is a door..."
        currentScene = scene0
        refreshScreen()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            doorrect = pygame.rect.Rect((275, 100), (475, 325))
            dirtrect = pygame.rect.Rect((0, 300), (275, 525))
            toolrect = pygame.rect.Rect((425, 330), (800, 600))
            if dirtrect.collidepoint(mousePos):
                Location = 1
                pygame.time.wait(500)
            elif toolrect.collidepoint(mousePos):
                Location = 2
                pygame.time.wait(500)
            elif doorrect.collidepoint(mousePos):
                Location = 3
                pygame.time.wait(500)
            else:
                break
    elif Location == 1:
        string = "You see a patch of dirt."
        string2 = "Dig it up?"
        currentScene = scene1
        refreshScreen()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            digRect = pygame.rect.Rect((25, 75), (175, 175))
            noDigRect = pygame.rect.Rect((575, 75), (800, 225))
            if digRect.collidepoint(mousePos):
                if hasShovel:
                    string = "You found a key!"
                    currentScene = scene1key
                    hasKey = True
                    string2 = ""
                    refreshScreen()
                    pygame.time.wait(2000)
                    Location = 0
                else:
                    string = "There's too much dirt here, maybe you should try finding a shovel first..."
                    string2 = ""
                    refreshScreen()
                    pygame.time.wait(2000)
                    Location = 0
            elif noDigRect.collidepoint(mousePos):
                string = "Maybe come back to it later..."
                string2 = ""
                refreshScreen()
                pygame.time.wait(2000)
                Location = 0
    elif Location == 2:
        string = "You found a shovel in the pile of tools!"
        string2 = "Take the shovel?"
        currentScene = scene2
        refreshScreen()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            yesRect = pygame.rect.Rect((25, 60), (125, 185))
            noRect = pygame.rect.Rect((25, 225), (225, 350))
            if yesRect.collidepoint(mousePos):
                string = "You took the shovel!"
                hasShovel = True
                string2 = ""
                refreshScreen()
                pygame.time.wait(2000)
                Location = 0
            elif noRect.collidepoint(mousePos):
                string = "You put the shovel down."
                string2 = ""
                refreshScreen()
                pygame.time.wait(2000)
                Location = 0
    elif Location == 3:
        string = "You found a door, but it's locked..."
        string2 = "Try to open it?"
        currentScene = scene3
        refreshScreen()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            yesRect = pygame.rect.Rect((0, 0), (200, 600))
            noRect = pygame.rect.Rect((550, 0), (800, 600))
            if yesRect.collidepoint(mousePos):
                if hasKey:
                    currentScene = scene3win
                    string = "YOU WIN!"
                    string2 = ""
                    refreshScreen()
                    pygame.time.wait(5000)
                    isGameRunning = False
                else:
                    string = "You couldn't get it open..."
                    string2 = ""
                    refreshScreen()
                    pygame.time.wait(2000)
                    Location = 0
            elif noRect.collidepoint(mousePos):
                string = "You gave up on opening the door for now..."
                string2 = ""
                refreshScreen()
                pygame.time.wait(2000)
                Location = 0

    timer.tick(60)




