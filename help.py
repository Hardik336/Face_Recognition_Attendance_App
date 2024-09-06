from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2  # (Open Source Computer Vision Library)


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="WHITE",fg="blue");
        title_lbl.place(x=0,y=0,width=1530,height=45);
        
        img2_top=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img2_top=img2_top.resize((1530,720),Image.LANCZOS);
        self.photoimg_top=ImageTk.PhotoImage(img2_top);
        
        f_lbl2=Label(self.root,image=self.photoimg_top);
        f_lbl2.place(x=0,y=55,width=1530,height=720);
        
        dev_label=Label(f_lbl2,text="Email:valahardik336@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white");
        dev_label.place(x=550,y=200);
        
        
if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()