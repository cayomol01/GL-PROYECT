from pickle import TRUE
import pygame
from pygame import mixer
from pygame.locals import *
import glm
from shaders import *

from gl import Renderer, Model

from math import cos, sin, radians

width = 960
height = 540

deltaTime = 0.0

mixer.init()
pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)

rend.target.z =-2
rend.target.y =2


available_models = ["face", "wolf", "skull", "tree", "stone"]


models = {"wolf": {"model": "models/Wolf.obj", 
                   "texture": "models/Wolf.jpg", 
                   "position":glm.vec3(0,-5,-3),
                   "scale":glm.vec3(5,5,5)
                   },
          "face":{"model": "models/model.obj", 
                  "texture": "models/model.bmp", 
                  "position":glm.vec3(0,0,-2),
                  "scale":glm.vec3(2,2,2),
                  },
          "skull":{"model": "models/Skull.obj", 
                  "texture": "models/Skull.jpg", 
                  "position":glm.vec3(0,-5,-5),
                  "scale":glm.vec3(0.15,0.15,0.15)
                  },
          "tree":{"model": "models/Tree.obj", 
                  "texture": "models/Skull.jpg", 
                  "position":glm.vec3(0,-3,-3),
                  "scale":glm.vec3(0.3,0.3,0.3)
                  },
          "stone":{"model": "models/Stone.obj", 
                  "texture": "models/Skull.jpg", 
                  "position":glm.vec3(0,-5,-10),
                  "scale":glm.vec3(1.5,1.5,1.5)
                  },
          
          }


ch = available_models[0]
ch = models[ch]



rend.camPosition.y = 0


rend.scene.append( Model(ch["model"], ch["texture"]) )

rend.scene[0].position.z = ch["position"].z
rend.scene[0].scale = ch["scale"]

mixer.music.load("audio/Wind.mp3")
mixer.music.set_volume(0.1)
mixer.music.play()

isRunning = True


def changeModel(choice):
    rend.scene.clear()
    model = Model(models[choice]["model"], models[choice]["texture"])
    model.position.z = models[choice]["position"].z
    model.scale.x = models[choice]["scale"].x
    model.scale.y = models[choice]["scale"].y
    model.scale.z = models[choice]["scale"].z
    rend.scene.append(model)

while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_z:
                rend.filledMode()
                rend.setShaders(vertex_shader, fragment_shader)
            elif event.key == pygame.K_x:
                rend.wireframeMode()
            elif event.key == pygame.K_y:
                rend.filledMode()
                rend.setShaders(vertex_shader, fragment_shader)
            elif event.key == pygame.K_c:
                rend.filledMode()
                rend.setShaders(glow_vertex_shader, glow_fragment_shader)
            elif event.key == pygame.K_v:
                rend.filledMode()
                rend.setShaders(toon_r_glow_vertex_shader, toon_r_glow_fragment_shader)
            elif event.key == pygame.K_b:
                rend.filledMode()
                rend.setShaders(toon_vertex_shader, toon_fragment_shader)
            elif event.key == pygame.K_n:
                rend.filledMode()
                rend.setShaders(negative_vertex_shader, negative_fragment_shader)
            elif event.key == pygame.K_1:
                changeModel("face")
            elif event.key == pygame.K_2:
                changeModel("wolf")
            elif event.key == pygame.K_3:
                changeModel("skull")
                rend.scene[0].rotation.x = -90
            elif event.key == pygame.K_4:
                changeModel("tree")
                rend.scene[0].rotation.y = -45
            elif event.key == pygame.K_5:
                changeModel("stone")





    if keys[K_q]:
        if rend.camDistance > 2:
            rend.camDistance -= 2 * deltaTime
    elif keys[K_e]:
        if rend.camDistance < 10:
            rend.camDistance += 2 * deltaTime

    if keys[K_a]:
        rend.angle -= 30 * deltaTime
    elif keys[K_d]:
        rend.angle += 30 * deltaTime


    if keys[K_w]:
        if rend.camPosition.y < 10:
            rend.camPosition.y += 5 * deltaTime
            if rend.camPosition.y >0:
                rend.target.z += 5*deltaTime
            else:
                rend.target.z -=5*deltaTime

    elif keys[K_s]:
        if rend.camPosition.y > -10:
            rend.camPosition.y -= 5 * deltaTime
            if rend.camPosition.y < 0:
                rend.target.z += 5*deltaTime
            else:
                rend.target.z -=5*deltaTime




    rend.target.y = rend.camPosition.y

    rend.camPosition.x = rend.target.x + sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle)) * rend.camDistance
    
    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime
    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime


    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
