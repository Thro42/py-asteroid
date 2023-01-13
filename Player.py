import pygame
import pygame.math
from Config import *
import Game


class Player:
    def __init__(self, game: Game, img: str, pos: pygame.math.Vector2, size: pygame.math.Vector2):
        self.game = game
        self.life = True
        self.draw_center = False
        self.dx = 0
        self.angle = 0
        self.posistion = pos
        self.size = size
        self.player_image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.player_image, size)
        self.player = pygame.Rect(pos.x - (size.x/2), pos.y - (size.y/2), size.x, size.y)

    def rotate(self):
        if self.angle > 0:
            loc = self.image.get_rect().center
            self.image = pygame.transform.rotate(self.image,self.angle)
            self.image.get_rect().center = loc
            self.player = self.image.get_rect().center

    def draw(self):
        self.game.fenster.blit(self.image, self.player)

    def loop(self):
        self.draw()
        self.rotate()