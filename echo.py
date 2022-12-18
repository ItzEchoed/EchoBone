
import pygame
from pygame.locals import *
import random
import variablesECO as var
import FandC as fc

TTF = var.TTF
screen = pygame.display.set_mode((var.Swide, var.Shgt))
pygame.display.set_caption('EchoBone')
PLR = pygame.sprite.Group()
Pipes = pygame.sprite.Group()
chr = fc.Player(100, int(var.Shgt / 2))
PLR.add(chr)
button = fc.Button(var.Swide // 2 - 50, var.Shgt // 2 - 100, var.button_img)

def reset_game():
    Pipes.empty()
    chr.rect.x = 100
    chr.rect.y = int(var.Shgt / 2)
    var.score = 0
    return var.score


run = True

while run:
    var.clock.tick(var.Frate)
    screen.blit(var.bg, (0,0))
    PLR.draw(screen)
    PLR.update()
    Pipes.draw(screen)
    if len(Pipes) > 0:
        if PLR.sprites()[0].rect.left > Pipes.sprites()[0].rect.left\
            and PLR.sprites()[0].rect.right < Pipes.sprites()[0].rect.right\
            and var.pass_pipe == False:
            var.pass_pipe = True
        if var.pass_pipe == True:
            if PLR.sprites()[0].rect.left > Pipes.sprites()[0].rect.right:
                var.score += 1
                var.pass_pipe = False
    fc.draw_text(str(var.score), var.TTF, var.white, int(var.Swide / 2), 20)
    if pygame.sprite.groupcollide(PLR, Pipes, False, False) or chr.rect.top < 0:
        var.GameState = True
    if chr.rect.bottom >= 768:
        var.GameState = True
        var.flying = False
    if var.GameState == False and var.flying == True:
        time_now = pygame.time.get_ticks()
        if time_now - var.last_pipe > var.pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = fc.Pipe(var.Swide, int(var.Shgt / 2) + pipe_height, -1)
            top_pipe = fc.Pipe(var.Swide, int(var.Shgt / 2) + pipe_height, 1)
            Pipes.add(btm_pipe)
            Pipes.add(top_pipe)
            var.last_pipe = time_now
        var.ground_scroll -= var.scroll_speed
        if abs(var.ground_scroll) > 35:
            var.ground_scroll = 0
        Pipes.update()
    if var.GameState == True:
        if button.draw() == True:
            var.GameState = False
            score = reset_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and var.flying == False and var.GameState == False:
            var.flying = True

    pygame.display.update()

pygame.quit()