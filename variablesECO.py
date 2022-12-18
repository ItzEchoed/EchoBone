import pygame
pygame.init()
clock = pygame.time.Clock()
Frate = 60
Swide = 840
Shgt = 760
#ig i m blocked with this res caz of online images idk its the good thing or the worst thing
TTF = pygame.font.Font('SomeRandomCoolFont.ttf', 60)
white = (255, 255, 255)
ground_scroll = 0
scroll_speed = 4
flying = False
GameState = False
pipe_gap = 180
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')
button_img = pygame.image.load('img/restart.png')