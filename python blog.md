### Welcome

Welcome to my blog. This blog serves to document my works on programming the microbit microcontroller. The programming language is micropython, a programming language that is a subset of python. The program I am creating is a game - whereby the player controls a spaceship that is under attack by aliens. The aliens will drop a bomb and the play must move the spaceship away from the bomb. The player will lose the game if the bomb touches the player's spaceship.

### docuumentations

I managed to get the spaceship to move left or right when button A or button B is pressed respectively. One of the issue I faced is when the user exceeds the game boundary when he presses too much in one direction which cuases the microbit to crash. To solve this issue, I insert a condition to reset the counter in a particular direction when it exceeds a certain direction. For example, if the user presses too much to the right, the ship will appear at the left.

Next, I tried to incoperate the alien into the code. I faced the same issue as coding the spaceship which i solve using similar methods excepts this time it will also randomly generate a x direction as it resets the y direction

After solving these 2 hurdles, I combined the elements together to form the game.

I managed to get them to work together but the functionality is not intended. I could not get the alien to move down on its own without freezing the button inputs. So, the alien only moves when the button is pressed which takes the fun out of it.

### thonny videos

