import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x  #koordinat x
        self.y = y  #koordinat y
        self.width = width      #lebar player
        self.height = height    #tinggi player
        self.color = color      #warna player
        self.rect = (x,y,width,height)  #set ukuran dan lokasi player
        self.vel = 3    #set kecepatan gerak

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)    #desain player ke game

    def move(self):
        keys = pygame.key.get_pressed()     #terima inputan clik keyboard

        if keys[pygame.K_LEFT]:     #jika keyboad tekan arah kiri
            self.x -= self.vel      #Koordinat x dikurang vel

        if keys[pygame.K_RIGHT]:    #jika keyboad tekan arah kanan
            self.x += self.vel      #Koordinat x ditambah vel

        if keys[pygame.K_UP]:       #jika keyboad tekan arah atas
            self.y -= self.vel      #Koordinat y dikurang vel

        if keys[pygame.K_DOWN]:     #jika keyboad tekan arah bawah
            self.y += self.vel      #Koordinat y ditambah vel

        self.update()       #update player

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)   #set ukuran dan lokasi player