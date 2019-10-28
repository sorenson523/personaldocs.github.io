### Welcome

Welcome to my blog. This blog serves to document my works on programming the microbit microcontroller. The programming language is micropython, a programming language that is a subset of python. The program I am creating is a game - whereby the player controls a spaceship that is under attack by aliens. The aliens will drop a bomb and the play must move the spaceship away from the bomb. The player will lose the game if the bomb touches the player's spaceship.

### Docuumentations

I managed to get the spaceship to move left or right when button A or button B is pressed respectively. One of the issue I faced is when the user exceeds the game boundary when he presses too much in one direction which cuases the microbit to crash. To solve this issue, I insert a condition to reset the counter in a particular direction when it exceeds a certain direction. For example, if the user presses too much to the right, the ship will appear at the left.

Next, I tried to incoperate the alien into the code. I faced the same issue as coding the spaceship which i solve using similar methods excepts this time it will also randomly generate a x direction as it resets the y direction

After solving these 2 hurdles, I combined the elements together to form the game.

I managed to get them to work together but the functionality is not intended. I could not get the alien to move down on its own without freezing the button inputs. So, the alien only moves when the button is pressed which takes the fun out of it.

Solving the above issue, a while loop that breaks when the button is pressed was inserted. Although there is a time lag till the spaceship responds to the button inputs, it at least resembles the intended functionality of the game.

### Code

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

    display.scroll("GAME OVER", loop = True)

### Thonny videos



### Beginner python videos



### References

https://microbit-micropython.readthedocs.io/en/latest/index.html - microbit documentations