from random import randint
import pygame
import pygame.math
from Config import *
import Player

class Game:
    bullets = []
    enemys = []

    def __init__(self, breite: int, hoehe: int):
        self.game_over = False
        self.player = None
        size = (breite, hoehe)
        self.fenster = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()


    def initPlayer(self):
        # Init the Player
        p_pos = pygame.math.Vector2(self.fenster.get_width()/2,self.fenster.get_height()/2)
        p_size = pygame.math.Vector2(40, 40)
        
        self.player = Player.Player(self, "images/space-ship.png", p_pos, p_size)
        self.player.enableCenter(True)