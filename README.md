# Rock-Paper-Scissor-Game
This  is  a simple Rock, Paper, Scissors (RPS) game implemented using the tkinter library for the graphical user interface (GUI) and the pygame library for sound effects. Here's a breakdown of the key components and functionalities of the code:

Importing Libraries:

The code begins by importing necessary libraries, including tkinter, PIL (Pillow for image handling), messagebox from tkinter for message pop-ups, and randint from the random library for generating random choices.
Initializing Pygame:

Pygame is initialized to handle sound effects during the game.
Main Class:

The code defines a class named Main, which serves as the main application for the RPS game.
The __init__ method initializes the game window, sets its dimensions, title, and icon.
It also creates the top logo image and labels for "YOU" and "COMP" displayed on the GUI.
Labels for displaying the user's and computer's scores are created.
Images for the game choices (rock, paper, scissor), result images (win, lose, tie), and initial user and computer choices are loaded.
GUI Components:

The code creates labels to display the user and computer choices, which initially show "rock" images.
Buttons are provided for the user to select their choice (rock, paper, scissor).
A label for displaying the game result (win, lose, tie) is also created.
Updating Choices:

The update_choice method is used to update the user's choice based on the button pressed and generate a random computer choice.
The user and computer choice images are updated accordingly.
Sound effects (click.wav) are played when a choice is made.
Updating Score:

The update_score method determines the game result and updates the scores accordingly.
If it's a tie, the tie image is displayed.
If the user wins, their score is incremented, and the win image is displayed with a win sound effect (win.wav).
If the computer wins, the computer's score is incremented, and the lose image is displayed with a lose sound effect (lose.wav).
Main Function:

The main function creates a Tkinter window and initializes an instance of the Main class.
The game starts when the mainloop() is called, and the GUI becomes interactive.
