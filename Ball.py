import pygame


class Ball:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        self.color = color
        self.radius = radius
        self.speed_x = 2
        self.speed_y = 5

    def draw(self, display):
        pygame.draw.circle(display, self.color, self.coordinates, self.radius)

    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        self.coordinates = (self.x, self.y)

    def collisionCheck(self, disp_width):
        if self.x >= disp_width - self.radius:
            self.speed_x = self.speed_x * -1
        elif self.x < self.radius:
            self.speed_x = self.speed_x * -1
        elif self.y < self.radius:
            self.y = self.radius
            self.speed_y = self.speed_y * -1

    def gravity(self, disp_height):
        cutOff = 200
        if self.y < cutOff:
            self.speed_y = self.speed_y * -1

    def miss(self, disp_height):
        if self.y - self.radius >= disp_height:
            print("You Lose")
            self.y = disp_height//2
            return True
        else:
            return False

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0

    def animate_chameleon(self, display):
        jump = [pygame.image.load('C0.png'), pygame.image.load('C1.png'), pygame.image.load('C2.png'),
                pygame.image.load('C3.png'), pygame.image.load('C4.png'), pygame.image.load('C5.png'),
                pygame.image.load('C6.png')]
        img_x_pos = self.x - 40
        img_y_pos = self.y - 40

        if self.speed_x > 0:  # Chameleon looks in the direction he is travelling
            if self.y >= 680 < 750:
                display.blit(jump[6], (img_x_pos, img_y_pos))
            elif self.y >= 640 < 680:
                display.blit(jump[5], (img_x_pos, img_y_pos))
            elif self.y >= 605 < 640:
                display.blit(jump[4], (img_x_pos, img_y_pos))
            elif self.y >= 570 < 605:
                display.blit(jump[3], (img_x_pos, img_y_pos))
            elif self.y >= 535 < 570:
                display.blit(jump[2], (img_x_pos, img_y_pos))
            elif self.y >= 500 < 535:
                display.blit(jump[1], (img_x_pos, img_y_pos))
            elif self.y >= 200 < 500:
                display.blit(jump[0], (img_x_pos, img_y_pos))
        else:
            if self.y >= 680 < 750:
                display.blit((pygame.transform.flip(jump[6], True, False)), (img_x_pos, img_y_pos))
            elif self.y >= 640 < 680:
                display.blit((pygame.transform.flip(jump[5], True, False)), (img_x_pos, img_y_pos))
            elif self.y >= 605 < 640:
                display.blit((pygame.transform.flip(jump[4], True, False)), (img_x_pos, img_y_pos))
            elif self.y >= 570 < 605:
                display.blit((pygame.transform.flip(jump[3], True, False)), (img_x_pos, img_y_pos))
            elif self.y >= 535 < 570:
                display.blit((pygame.transform.flip(jump[2], True, False)), (img_x_pos, img_y_pos))
            elif self.y >= 500 < 535:
                display.blit((pygame.transform.flip(jump[1], True, False)), (img_x_pos, img_y_pos))
            elif self.y >= 200 < 500:
                display.blit((pygame.transform.flip(jump[0], True, False)), (img_x_pos, img_y_pos))



