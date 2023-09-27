import pygame
from network import Network
from player import Player

width = 500     #Lebar Game
height = 500    #Tinggi Game
win = pygame.display.set_mode((width, height))  #set tampilan
pygame.display.set_caption("Client")    #set judul


def redrawWindow(win,player, player2):
    win.fill((255,255,255))     #set warna latar
    player.draw(win)    #set player 1
    player2.draw(win)   #set player 2
    pygame.display.update()     #update tampilan game


def main():
    run = True      #program berjalan
    n = Network()   #Network
    p = n.getP()    #Player Connect to server
    clock = pygame.time.Clock()     #untuk melacak object

    while run:
        clock.tick(60)  #set pergerakan 60 per frame
        p2 = n.send(p)  #mengirim data player ke player 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #Jika client di quit
                run = False     #program client berhenti
                pygame.quit()   #game berhenti

        p.move()    #Player gerak
        redrawWindow(win, p, p2)    #update tampilan

main()