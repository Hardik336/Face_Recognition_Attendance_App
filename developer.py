from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2  # (Open Source Computer Vision Library)


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="WHITE",fg="blue");
        title_lbl.place(x=0,y=0,width=1530,height=45);
        
        img2_top=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\dev.jpg")
        img2_top=img2_top.resize((1530,720),Image.LANCZOS);
        self.photoimg_top=ImageTk.PhotoImage(img2_top);
        
        f_lbl2=Label(self.root,image=self.photoimg_top);
        f_lbl2.place(x=0,y=55,width=1530,height=720);
        
        
        # Frame
        main_frame=Frame(f_lbl2,bd=2,bg="white");
        main_frame.place(x=1000,y=0,width=500,height=600);
        
        
        img2_top1=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\hardik.jpg")
        img2_top1=img2_top1.resize((200,200),Image.LANCZOS);
        self.photoimg_top1=ImageTk.PhotoImage(img2_top1);
        
        f_lbl2=Label(main_frame,image=self.photoimg_top1);
        f_lbl2.place(x=295,y=0,width=200,height=200);
        
        # Developer info
        dev_label=Label(main_frame,text="Hello my name,Hardik",font=("times new roman",20,"bold"),fg="blue",bg="white");
        dev_label.place(x=0,y=5);
        
        dev_label=Label(main_frame,text="I am full stack developer",font=("times new roman",20,"bold"),fg="blue",bg="white");
        dev_label.place(x=0,y=40);

        # Image 3
        img2=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2=img2.resize((500,390),Image.LANCZOS);
        self.photoimg2=ImageTk.PhotoImage(img2);
        
        f_lbl2=Label(main_frame,image=self.photoimg2);
        f_lbl2.place(x=0,y=210,width=500,height=390);



if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()