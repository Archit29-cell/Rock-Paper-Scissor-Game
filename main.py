from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from random import randint
import pygame

pygame.mixer.init()
class Main:
    def __init__(self,root):
        self.root =  root
        self.root.geometry('1280x700')
        self.root.configure(bg ='black')
        self.root.title('RPS Game')
        self.root.iconbitmap('52761videogame_109402.ico')

        # LOGO IMAGE WHICH  SHOW AT TOP OF THE PAGE
        img1 = Image.open(r"rpslogo.jpg")
        img1 = img1.resize((1278, 150))
        self.photo_img1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photo_img1,bd =2 )
        f_lbl1.place(x =0, y =0, height =150, width =1278)


        # YOU LABEL WHICH SHOW THE USER'S SIDE
        you = Label(self.root,text ='YOU',font =('game over font ',40),bg ='black', fg='white' )
        you.place(x=1000 ,y = 170)

        # COMPUTER LABEL WHICH SHOW THE COMPUTER'S SIDE
        comp = Label(self.root,text ='COMP',font =('game over font ',40),bg ='black', fg='white' )
        comp.place(x= 180,y = 170)


        # SCORE LABELS WHICH UPDATE ACCORDING TO THE RESULT(IF USER WIN, ONE POINT ADD IN THE SCORE OF USER OTHERWISE IN THE SCORE OF COMPUTER )
        self.comp_score = Label(self.root, text =0,font =('game over font ',40),bg ='black', fg='white')
        self.comp_score.place(x= 360, y =170)


        self.player_score = Label(self.root,text =0,font =('game over font ',40),bg ='black', fg='white' )
        self.player_score.place(x=940, y=170)


        # PICTURES WHICH ARE USED AND CHANGE ACCORDING TO RULES

        # USER'S CHOICE IMAGE
        self.rock_image = ImageTk.PhotoImage(Image.open(r"rock_user.jpg").resize((220,100)))
        self.paper_image =ImageTk.PhotoImage(Image.open(r"paper_user.jpg").resize((220,100)))
        self.scissor_image = ImageTk.PhotoImage(Image.open(r"scissor_user.jpg").resize((220,100)))

        # COMPUTER'S CHOICE IMAGE
        self.rock_image_comp = ImageTk.PhotoImage(Image.open(r"rock_comp.jpg").resize((220,100)))
        self.paper_image_comp =ImageTk.PhotoImage(Image.open(r"paper_comp.jpg").resize((220,100)))
        self.scissor_image_comp = ImageTk.PhotoImage(Image.open(r"scissor_comp.jpg").resize((220,100)))

        # RESULT IMAGES
        self.won = ImageTk.PhotoImage(Image.open(r"youwon.jpg").resize((200,100)))
        self.lose = ImageTk.PhotoImage(Image.open(r"lose.jpg").resize((200,100)))
        self.tie = ImageTk.PhotoImage(Image.open(r"tie.png").resize((200,100)))

        # INITIAL USER AND COMPUTER'S CHOICE PICTURES

        self.user_label = Label(self.root,image=self.rock_image)
        self.user_label.place(x=940,y=260,width =220,height = 100)
        self.comp_label = Label(self.root,image=self.rock_image_comp)
        self.comp_label.place(x=180, y = 260,width = 220, height=100)

        # BUTTONS TO CHOOSE THEIR CHOICE(ROCK, PAPER, SCISSOR)
        rock_button = Button(self.root, text= 'ROCK',font =("game over font",15,"bold","italic"), bd =4, bg="green",fg="black",relief="ridge",command=lambda:self.update_choice("ROCK"))
        rock_button.place(x =400+30, y=380, width=150, height= 50)
        
        paper_button = Button(self.root, text ="PAPER",font =("game over font",15,"bold","italic"), bd =4, bg="red",fg="black",relief ="ridge",command=lambda:self.update_choice("PAPER") )
        paper_button.place(x=560+30,y=380,width = 150, height=50)

        scissor_button = Button(self.root, text ="SCISSOR",font =("game over font",15,"bold","italic"), bd =4, bg="Blue",fg="black",relief ="ridge",command = lambda:self.update_choice("SCISSOR")) 
        scissor_button.place(x=720+30,y=380,width = 150, height=50)

        # RESULT LABEL WHICH SHOW THE RESULT THAT USER WILL WIN OR LOSS OR TIE
        self.result_label = Label(self.root,bd=0,bg= "black",fg ='white',font = ("game over font",20) )
        self.result_label.place(x=580,y=260,width=200, height= 100 )

        self.x = None
        self.choices =["ROCK","PAPER","SCISSOR"]


    def update_choice(self, x):

        # COMPUTER CHOICE WHICH CHANGES RANDOMLY AND AUTOMATICALLY
        choice = self.choices[randint(0,2)]
        if choice =="ROCK":
            self.comp_label.configure(image=self.rock_image_comp)
        elif choice =="PAPER":
            self.comp_label.configure(image = self.paper_image_comp)
        elif choice =="SCISSOR":
            self.comp_label.configure(image=self.scissor_image_comp)

        # USER CHOICE WHICH CHANGE ON PRESSING THE BUTTON OF ROCK, PAPER, SCICCOR
        self.x =x 
        if x == "ROCK":
            self.user_label.configure(image =self.rock_image) 
            
            self.button_click_sound = pygame.mixer.Sound("click.wav").play()
        elif x =="PAPER":
            self.user_label.configure(image =self.paper_image)
            
            self.button_click_sound = pygame.mixer.Sound("click.wav").play()
        elif x =="SCISSOR":
            self.user_label.configure(image= self.scissor_image)
            self.button_click_sound = pygame.mixer.Sound("click.wav").play()
        self.update_score(x,choice)

    #  UPDATE SCORE FUNCTION WHICH UPDATE THE SCORE OF USER AND COMPUTER
    def update_score(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            self.result_label.configure(image=self.tie)

        # USER WINS AND UPDATE THE SCORE OF USER BY ONE

        elif (
            (user_choice == "ROCK" and comp_choice == "SCISSOR")
            or (user_choice == "PAPER" and comp_choice == "ROCK")
            or (user_choice == "SCISSOR" and comp_choice == "PAPER")):
            user_score = int(self.player_score.cget("text")) + 1
            self.player_score.config(text=user_score)
            self.result_label.configure(image=self.won)
            self.win_click_sound = pygame.mixer.Sound("win.wav").play()

        # COMPUTER WINS AND UPDATE THE SCORE OF COMPUTER BY ONE

        else:
            comp_score = int(self.comp_score.cget("text")) + 1
            self.comp_score.config(text=comp_score)
            self.result_label.configure(image=self.lose)
            self.lose_click_sound = pygame.mixer.Sound("lose.wav").play()
    
# MAIN FUNCTION
if __name__=="__main__":
    root = Tk()
    obj =Main(root)
    root.mainloop()
