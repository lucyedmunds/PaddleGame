import pygame


class Paddle:

    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.width = 100
        self.height = 10
        self.coordinates = (self.x, self.y, self.width, self.height)

    def draw(self, display):
        pygame.draw.rect(display, self.colour, self.coordinates)

    def moveLeft(self, move_left):
        if move_left and self.x > 0:
            self.x = self.x - 5
            self.coordinates = (self.x, self.y, self.width, self.height)

    def moveRight(self, move_right):
        if move_right and self.x < 700:
            self.x = self.x + 5
            self.coordinates = (self.x, self.y, self.width, self.height)

    def banana_image(self, display):
        banana = pygame.image.load('Banana Paddle.png')
        img_x_pos = self.x - 30
        img_y_pos = self.y - 25

        display.blit(banana, (img_x_pos, img_y_pos))
