from random import randrange
from tracemalloc import start
import pygame

start = True
blue = (0,0,255)
red = (255,0,0)
white = (255, 255, 255)
green = (0, 100, 0)
width = 100
height = 100
x = width / 2
y = height / 2
step = 10
game_over = False
clock = pygame.time.Clock()
snake = [[x,y]]
foodx = -10
foody = -10

pygame.init()
dis = pygame.display.set_mode((width,height))
 
pygame.display.set_caption('Python Plays Python')

def getFood():
    global snake
    global foodx
    global foody
    if (foodx == -10 and foody == -10):
        foodx = randrange(0, width, 10)
        foody = randrange(0, height, 10)

    for s in snake:
        if foodx == s[0] and foody == s[1]:
            print('food spawned on snake')
            foodx = -10
            foody = -10
            getFood()
            return
    
    pygame.draw.rect(dis, blue, [foodx, foody, step, step])

def getSnake():
    global snake
    num = 0;
    for s in snake:
        color = green if num == 0 else red
        pygame.draw.rect(dis, color, [s[0], s[1], step, step])
        num += 1


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('user quit')
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - step == foody and x == foodx:
                    snake.insert(0, [x, y - step])
                y -= step
            elif event.key == pygame.K_DOWN:
                if y + step == foody and x == foodx:
                    snake.insert(0, [x, y + step])
                y += step
            elif event.key == pygame.K_LEFT:
                if y == foody and x - step == foodx:
                    snake.insert(0, [x - step, y])
                x -= step
            elif event.key == pygame.K_RIGHT:
                if y == foody and x + step == foodx:
                    snake.insert(0, [x + step, y])
                x += step

            if x < 0 or x-10 > width or y < 0 or y-10 >= height:
                print('boundary issue')
                print(x)
                print(width)
                print(y)
                print(height)
                game_over = True
                break 

            #print('Snake: ',snake,' Food: ',foodx,' ',foody)

            if snake[0][0] == foodx and snake[0][1] == foody:
                foodx = -10
                foody = -10
                getFood()
            else:
                tempSnake = [[x,y]]
                for i, s in list(enumerate(snake)):
                    if (i > 0):
                        tempSnake.insert(i, [snake[i-1][0],snake[i-1][1]])
                
                for s in snake:
                    if s == [x,y]:
                        print(tempSnake)
                        game_over = True
                        break 

                snake = tempSnake

        dis.fill(white)
        getFood()
        getSnake()
    
    pygame.display.update()

    clock.tick(30)
    
pygame.quit()
quit()