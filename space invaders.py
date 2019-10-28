#Engineering Realisation Tutorial Week 2
#Space invaders game
#Programming Language: Micropython
#Microcontroller platform: Microbit

from microbit import *
import random

random.seed()

spaceship_x = 2
display.set_pixel(spaceship_x, 4, 9)
alien_x = random.randint(0, 4)
alien_y=0
display.set_pixel(alien_x, alien_y, 9)

while True:
    while button_b.is_pressed() == False and button_a.is_pressed() == False and alien_y < 4:
        sleep(300)
        alien_y = alien_y + 1
        display.clear()
        display.set_pixel(alien_x, alien_y, 9)
        display.set_pixel(spaceship_x, 4, 9)
        if button_b.is_pressed() or button_a.is_pressed() or alien_y == 4:
            break
    if button_b.is_pressed() and spaceship_x < 4 and alien_y < 4:
        sleep(200)
        spaceship_x = spaceship_x + 1
        alien_y = alien_y + 1
        display.clear()
        display.set_pixel(alien_x, alien_y, 9)
        display.set_pixel(spaceship_x, 4, 9)
    elif button_b.is_pressed() and spaceship_x == 4 and alien_y < 4:
        sleep(200)
        spaceship_x = 0
        alien_y = alien_y + 1
        display.clear()
        display.set_pixel(alien_x, alien_y, 9)
        display.set_pixel(spaceship_x, 4, 9)
    elif button_a.is_pressed() and spaceship_x > 0 and alien_y < 4:
        sleep(200)
        spaceship_x = spaceship_x - 1
        alien_y = alien_y + 1
        display.clear()
        display.set_pixel(alien_x, alien_y, 9)
        display.set_pixel(spaceship_x, 4, 9)
    elif button_a.is_pressed() and spaceship_x == 0 and alien_y < 4:
        sleep(200)
        spaceship_x = 4
        alien_y = alien_y + 1
        display.clear()
        display.set_pixel(alien_x, alien_y, 9)
        display.set_pixel(spaceship_x, 4, 9)
    elif alien_y == 4:
        if alien_x == spaceship_x and alien_y ==4:
            sleep(200)
            break
        else:
            alien_y = 0
            alien_x = random.randint(0, 4)
            display.clear()
            display.set_pixel(alien_x, alien_y, 9)
            display.set_pixel(spaceship_x, 4, 9)

display.scroll("GAME OVER NOOBS", loop = True)
