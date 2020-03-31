import pygame
import Paddle
import Ball
import math
from create_serial import CreateSerial

def unpackSerialAcc(msg):
    # return the acc x seperated from the list
    acc_x_value = 0
    for item in msg:
        string_value = item.split(" ")
        acc_x_value = float(string_value[0])
        acc_y_value = float(string_value[1])
        acc_z_value = float(string_value[2])
        return acc_x_value


def paddleCheck(paddle, ball):
    paddle_surface = range(paddle.x, paddle.x + paddle.width)
    bottom_impact = ball.y + ball.radius
    if ball.speed_y > 0:
        if bottom_impact >= paddle.y and ball.x in paddle_surface:
            ball.speed_y = ball.speed_y * -1
        lx1 = paddle.x
        ly1 = paddle.y + (paddle.height * 0.66)
        lx2 = ball.x + ball.radius
        ly2 = ball.y
        ldist = math.sqrt(((ly2 - ly1) ** 2) + ((lx2 - lx1) ** 2))
        if ldist < 10:
            ball.speed_y = ball.speed_y * -1
            ball.speed_x = ball.speed_x * -1
        rx1 = paddle.x + paddle.width
        ry1 = paddle.y + (paddle.height * 0.66)
        rx2 = ball.x - ball.radius
        ry2 = ball.y
        rdist = math.sqrt(((ry2 - ry1) ** 2) + ((rx2 - rx1) ** 2))
        if rdist < 10:
            ball.speed_y = ball.speed_y * -1
            ball.speed_x = ball.speed_x * -1


def respawnBall(paddle,ball, disp_height, disp_width):
    if ball.y - ball.radius >= disp_height:

        # update position
        ball.y = disp_height // 2
        ball.x = disp_width // 2

        return True
    else:
        return False


def countLives(numLives):
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render('%d' % numLives, True, green, blue)
    textRect = text.get_rect()
    textRect.center = (780, 20)
    display.blit(text, textRect)

    if numLives == 0:
        font1 = pygame.font.Font('freesansbold.ttf', 35)
        text1 = font1.render("You lose!", True, green, blue)
        textRect1 = text1.get_rect()
        textRect1.center = (DISPLAY_HEIGHT // 2, DISPLAY_WIDTH // 2)
        display.blit(text1, textRect1)


# Setup
pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()
pygame.mixer.init()

# Display Setup
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
display = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('Paddleball')
background_image = pygame.image.load("BackgroundImg.png").convert()

# Music Setup
pygame.mixer.music.load("Off Limits.wav")
pygame.mixer.music.set_volume(0.5)  # between 0 and 1
pygame.mixer.music.play(-1)  # -1 to loop (2 to play it twice)


# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)

# Clock Setup for FPS
clock = pygame.time.Clock()

# Paddle Setup
start_x = 450
start_y = 750
myPaddle = Paddle.Paddle(start_x, start_y, black)
leftFlag = False
rightFlag = False

# Ball Setup
ballSize = 30
myBall = Ball.Ball(DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2+30, green, ballSize)

# Circuit playground setup
serial_1 = CreateSerial("/dev/cu.usbmodem1421") # init the serial port
serial_1.openPort()
line = ""
msg_filtered = ""

# Lives Setup
lives = 3

# Score Setup
wins = 0


# Game loop
run_game = True
while run_game:
    display.blit(background_image, [0, 0])

    # Text
    countLives(lives)

    # Paddle
    # myPaddle.draw(display)  # This is commented out so it is invisible
    myPaddle.moveLeft(leftFlag)
    myPaddle.moveRight(rightFlag)

    # Ball
    # myBall.draw(display)  # This is commented out so it is invisible
    myBall.move()
    myBall.collisionCheck(DISPLAY_WIDTH)
    myBall.gravity(DISPLAY_HEIGHT)

    # Animation
    myPaddle.banana_image(display)
    myBall.animate_chameleon(display)

    # Interactions
    paddleCheck(myPaddle, myBall)
    bottomCheck = respawnBall(myPaddle,myBall,DISPLAY_HEIGHT, DISPLAY_WIDTH)

    # Controller
    if serial_1.ser.name in CreateSerial.ports_available:  # if circuit playground not connected
        line = serial_1.read()
        if line != None:
            msg_filtered = line
        x_value = unpackSerialAcc(msg_filtered)
        print(x_value)

        if x_value != None:
            if x_value > -1 and x_value < 1:
                leftFlag = False
                rightFlag = False
            if x_value < -1:
                leftFlag = True
            else:
                leftFlag = False
            if x_value > 1:
                rightFlag = True
            else:
                rightFlag = False


    # Lives
    if bottomCheck:
        lives -= 1

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run_game = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftFlag = True
            if event.key == pygame.K_RIGHT:
                rightFlag = True

        elif event.type == pygame.KEYUP:
            leftFlag = False
            rightFlag = False

        elif event.type == pygame.K_a:
            respawnBall(myPaddle, myBall, DISPLAY_HEIGHT, DISPLAY_WIDTH)

    if lives == 0:
        countLives(lives)
        run_game = False

    pygame.display.update()
    clock.tick(70)


# Close game
pygame.quit()
pygame.time.delay(3000)
quit()