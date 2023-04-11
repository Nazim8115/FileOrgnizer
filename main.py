from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import PIL.ImageTk
import PIL.Image


class FileOrganizer:
    def __init__(self):
        self.window=Tk()

        self.width=self.window.winfo_screenwidth()
        self.height=self.window.winfo_screenheight()

        # print(f"{self.width} {self.height}")  # for check height and  width 

        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False,False)
        self.window.title("File Organizer")
        self.window.iconbitmap("icon.ico")
        self.window.protocol("WM_DELETE_WINDOW",self.closeWindow)
        self.backgroundImage=PIL.Image.open(r"lib\background.jpg")# for image 
        self.backgroundImage.resize((self.width,self.height))     #for size
        self.backgroundImage=PIL.ImageTk.PhotoImage(self.backgroundImage) # for convert in photoimage 
        self.backgroundLabel=Label(self.window,image=self.backgroundImage)
        self.backgroundLabel.image=self.backgroundImage
        self.backgroundLabel.pack()

        



        self.window.mainloop()
    def closeWindow(self):
        if messagebox.askyesnocancel("Quit","Are you sure you want to quit ?"):
            self.window.destroy()
           
if __name__=='__main__':
    Organizer=FileOrganizer()


