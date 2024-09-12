from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2.face
import mysql.connector
import cv2  # (Open Source Computer Vision Library)
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="WHITE",fg="red");
        title_lbl.place(x=0,y=0,width=1530,height=45);
        
        img2_top=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\face-recognition-1024x630.jpg")
        img2_top=img2_top.resize((1530,325),Image.LANCZOS);
        self.photoimg_top=ImageTk.PhotoImage(img2_top);
        
        f_lbl2=Label(self.root,image=self.photoimg_top);
        f_lbl2.place(x=0,y=55,width=1530,height=325);
        
         # Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white");
        b1_1.place(x=0,y=380,width=1530,height=60);
        
        img2_bottom=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\face_det.png")
        img2_bottom=img2_bottom.resize((1530,325),Image.LANCZOS);
        self.photoimg_bottom=ImageTk.PhotoImage(img2_bottom);
        
        f_lbl2=Label(self.root,image=self.photoimg_bottom);
        f_lbl2.place(x=0,y=440,width=1530,height=325);
        
    
    def train_classifier(self):
        data_dir=("data");
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)];
        
        faces=[];
        ids=[];
        
        for image in path:
            img=Image.open(image).convert('L'); # Gray scale image
            imageNp=np.array(img,'uint8');
            id=int(os.path.split(image)[1].split('.')[1]);
            
            faces.append(imageNp);
            ids.append(id);
            cv2.imshow("Training",imageNp);
            cv2.waitKey(1)==13;
        ids=np.array(ids);

        # ========= Tryain the classifier and save ==========
        clf=cv2.face.LBPHFaceRecognizer_create();
        clf.train(faces,ids);
        clf.write("classifier.xml");
        cv2.destroyAllWindows();
        messagebox.showinfo("Result","Training datasets completed!!");
        
        
            
        
        
if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()