from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from main import Main
import pygame


pygame.mixer.init()
class RPS:
    def __init__(self,root) :
        self.root = root
        self.root.geometry('1280x700')
        self.root.configure(bg ='white')
        self.root.title('RPS Game HOME')
        self.root.iconbitmap('52761videogame_109402.ico')
  

        img1 = Image.open(r"rpslogo4.jpg")
        img1 = img1.resize((1278,690))
        self.photoimg1 = ImageTk.PhotoImage(img1)


        f_lbl1 = Label(self.root, image=self.photoimg1,bd =4)
        f_lbl1.place(x=0,y =0, width =1278, height = 690)   

        img2 = Image.open(r"button1.jpg")
        img2 = img2.resize((200,50))
        self.photoimg2 = ImageTk.PhotoImage(img2)  

        start_button = Button(self.root,image =self.photoimg2,bd =4,highlightbackground='black',highlightcolor='black',bg='black',command=self.start)
        start_button.place(x=880,y =500, width =200, height = 50)

        img3 = Image.open(r"exit.jpg")
        img3 = img3.resize((200,50))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        exit_button = Button(self.root,image =self.photoimg3,bd =4,highlightbackground='black',highlightcolor='black',bg='black',command=self.exit)
        exit_button.place(x=880,y =555, width =200, height = 50)

        img4 = Image.open(r"about.png")
        img4 = img4.resize((100,50))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        about_button = Button(self.root, image=self.photoimg4,bd =0,highlightbackground='black',highlightcolor='black',bg='black',command=self.show_about)
        about_button.place(x =1150,y=10,width = 100,height =50)


    def show_about(self):
        about_window = Toplevel(self.root)
        about_window.geometry('400x120+{}+{}'.format(self.root.winfo_x() + 870, self.root.winfo_y() + 90))
        about_window.title('About RPS Game')
        about_window.resizable(0,0)
        about_window.transient(self.root)
        
        

        about_label = Label(about_window, text='Rules of the Rock-Paper-Scissors Game:\n'
                                               '1. Rock beats Scissors.\n'
                                               '2. Scissors beats Paper.\n'
                                               '3. Paper beats Rock.',
                            font=('Arial', 14))
        about_label.pack(pady=20)


    def exit(self):
        exit = messagebox.askyesno("Exit", "Do You Want to Exit") 
        if exit >0:
            return root.destroy()
        else:
            return
    

    def start(self):
        self.new_window = Toplevel(self.root)
        self.app = Main(self.new_window)
        self.button_click_sound = pygame.mixer.Sound("welcome.mp3")
        self.button_click_sound.play()


if __name__  == "__main__":
    root = Tk()
    obj = RPS(root)
    root.mainloop()