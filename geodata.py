import numpy as np
import csv
import matplotlib.pyplot as plt
from read import *
import pygame

## OBJECTIVES
# 1. Make a pygame or tkinter gui to be able to plot the values of a dataset
# 2. Make an area clickable or hover over a point to obtain data
# 3. Make the data fetching done using a user def func
# 4. Later on, include different ways to visualize the data (color, contour maps, cluster, maybe 3d etc.)
# 5. use blit to make a background

### FUNCTIONS

def stats(data_points):
    n = float(len(data_points))
    x = 0
    y = 0
    sx = 0
    sy = 0
    for P in data_points:
        x += P[0]
        y += P[1]

    x /= n
    y /= n  

    for P in data_points:
        sx += (P[0]-x)**2
        sy += (P[1]-y)**2

    sx = (sx/n)**0.5
    sy = (sy/n)**0.5

    return (x, sx), (y, sy)

def display_points(screen, data_points):
    for P in data_points:
        pygame.draw.circle(screen, "RED", P, 1)


### DATA


data_points = read_data("data/2019.csv")
data_points = [(10*x, 10*y-500) for x, y in data_points]
SX, SY = stats(data_points)


### PYGAME ###

pygame.init()

w = 548
h = 612
window = pygame.display.set_mode((w, h))

pygame.display.flip()

bg = pygame.image.load("Map.jpg")
show_data = False

running = True
while running:
    window.blit(bg, (0, 0))

    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            running = False
            
        if Event.type == pygame.MOUSEBUTTONDOWN:
            show_data = not show_data        

    if show_data:
        display_points(window, data_points)

    pygame.display.flip()

pygame.quit()
quit()

pygame.init() 
  


