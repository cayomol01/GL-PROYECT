import pygame
from pygame.locals import *

from shaders import *

from gl import Renderer, Model
import math

width = 960
height = 540
prueba = 90
deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)

face = Model("model.obj", "model.bmp")



rend.scene.append( face )

radio = 10
isRunning = True
face.position.z -= 5
rend.camPosition.z = 2
radio = max(face.position)

def distancePoints(obj1, rendeer):
    distance = ((obj1.position.x - rendeer.camPosition.x)**2 + (obj1.position.y - rendeer.camPosition.y)**2 + (obj1.position.z - rendeer.camPosition.z)**2)**(0.5)
    return distance

radio = distancePoints(face, rend)

def radians(angle):
    return math.radians(angle)

radio = 5

rend.camPosition.x = 0
rend.camPosition.y = 2
rend.camPosition.z = radio

while isRunning:
    pygame.draw.circle(screen, (255,0,0), (0,0), 1)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    
    if keys[K_LEFT]:
    
        rend.camPosition.x -= 2*deltaTime
        


        

    elif keys[K_RIGHT]:
        if rend.camPosition.y != 0:
            rend.camPosition.y = 0
        rend.camPosition.x = radio*math.cos(radians(prueba))
        rend.camPosition.z = radio*math.sin(radians(prueba))
        rend.camRotation.y -= 50*deltaTime
        prueba += 50*deltaTime


    elif keys[K_UP]:
        rend.camPosition.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.camPosition.y -= 10 * deltaTime

    deltaTime = clock.tick(60) / 1000
    #print(deltaTime)

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()