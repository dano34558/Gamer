import pygame.math

class Transform:
    def __init__(self, x=0, y=0):
        self.position = pygame.math.Vector2(x, y)
        self.rotation = 0
        self.scale = pygame.math.Vector2(1, 1)

    @property
    def forward(self):
        return pygame.math.Vector2(0, -1).rotate(-self.rotation)

    @property
    def right(self):
        return pygame.math.Vector2(1, 0).rotate(-self.rotation)

    def translate(self, x, y):
        self.position += pygame.math.Vector2(x, y)

    def rotate(self, angle):
        self.rotation += angle

    def set_position(self, x, y):
        self.position = pygame.math.Vector2(x, y)

    def set_rotation(self, angle):
        self.rotation = angle

    def set_scale(self, x, y):
        self.scale = pygame.math.Vector2(x, y)

