from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2  # (Open Source Computer Vision Library)
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        
        # ============= Variables ==============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        # Image 1
        img=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\smart-attendance.jpg")
        img=img.resize((800,200),Image.LANCZOS);
        self.photoimg=ImageTk.PhotoImage(img);
        
        f_lbl=Label(self.root,image=self.photoimg);
        f_lbl.place(x=0,y=0,width=800,height=200);
        
        # Image 2
        img1=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\iStock-182059956_18390_t12.jpg")
        img1=img1.resize((800,200),Image.LANCZOS);
        self.photoimg1=ImageTk.PhotoImage(img1);
        
        f_lbl1=Label(self.root,image=self.photoimg1);
        f_lbl1.place(x=800,y=0,width=800,height=200);
        
        # Background Image
        img3=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\un.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS);
        self.photoimg3=ImageTk.PhotoImage(img3);
        
        bg_img=Label(self.root,image=self.photoimg3);
        bg_img.place(x=0,y=200,width=1530,height=710);
       
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMNET SYSTEM",font=("times new roman",35,"bold"),bg="pink",fg="DARKGREEN");
        title_lbl.place(x=0,y=0,width=1530,height=45);
        
        main_frame=Frame(bg_img,bd=2,bg="pink");
        main_frame.place(x=13,y=55,width=1500,height=520);
        
        # Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="lightblue",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"));
        Left_frame.place(x=5,y=10,width=740,height=480)
        
        img2_left=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\face-recognition.png")
        img2_left=img2_left.resize((730,150),Image.LANCZOS);
        self.photoimg_left=ImageTk.PhotoImage(img2_left);
        
        f_lbl2=Label(Left_frame,image=self.photoimg_left);
        f_lbl2.place(x=3,y=0,width=730,height=150);
        
        # Left inside frame
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="palegreen");
        left_inside_frame.place(x=7,y=155,width=722,height=295);
        
        # Labels and Entry
        
        # Attendance id label
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",13,"bold"),bg="white");
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W);
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"));
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W);
        
        # Roll label
        rollLabel=Label(left_inside_frame,text="Roll:",font="comicsansns 11 bold");
        rollLabel.grid(row=0,column=2,padx=4,pady=8);
        
        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font="comicsansns 11 bold");
        atten_roll.grid(row=0,column=3,pady=8);
        
        # Name label
        nameLabel=Label(left_inside_frame,text="Name:",font="comicsansns 11 bold");
        nameLabel.grid(row=1,column=0);
        
        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold");
        atten_name.grid(row=1,column=1,pady=8);
        
        # Department label
        depLabel=Label(left_inside_frame,text="Department:",font="comicsansns 11 bold");
        depLabel.grid(row=1,column=2);
        
        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold");
        atten_dep.grid(row=1,column=3,pady=8);
        
        # time label
        timeLabel=Label(left_inside_frame,text="Time:",font="comicsansns 11 bold");
        timeLabel.grid(row=2,column=0);
        
        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold");
        atten_time.grid(row=2,column=1,pady=8);
        
        # Date label
        dateLabel=Label(left_inside_frame,text="Date:",font="comicsansns 11 bold");
        dateLabel.grid(row=2,column=2);
        
        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold");
        atten_date.grid(row=2,column=3,pady=8);
        
        # Attendance label
        attendanceLabel=Label(left_inside_frame,text="Attendance Status",font="comicsansns 11 bold");
        attendanceLabel.grid(row=3,column=0);
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        # buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white");
        btn_frame.place(x=0,y=200,width=718,height=38);
        
        # Buttons
        # Import button
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white");
        save_btn.grid(row=0,column=0);
        
        # Export button
        update_btn = Button(btn_frame,text="Export csv",command=self.exportCsv,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        
        # Update Button
        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white");
        delete_btn.grid(row=0,column=2);
        
        # Reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white");
        reset_btn.grid(row=0,column=3);
        
        
        
        
        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="lightblue",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"));
        Right_frame.place(x=747,y=10,width=730,height=480);
        
        # Right inside frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white");
        table_frame.place(x=5,y=5,width=715,height=445);
        
        # ========= Scroll Bar ==========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendannceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendannceReportTable.xview)
        scroll_y.config(command=self.AttendannceReportTable.yview)
        
        self.AttendannceReportTable.heading("id",text="Attendance ID")
        self.AttendannceReportTable.heading("roll",text="Roll")
        self.AttendannceReportTable.heading("name",text="Name")
        self.AttendannceReportTable.heading("department",text="Department")
        self.AttendannceReportTable.heading("time",text="Time")
        self.AttendannceReportTable.heading("date",text="Date")
        self.AttendannceReportTable.heading("attendance",text="Attendance")
        
        self.AttendannceReportTable["show"]="headings"
        
        self.AttendannceReportTable.column("id",width=100)
        self.AttendannceReportTable.column("roll",width=100)
        self.AttendannceReportTable.column("name",width=100)
        self.AttendannceReportTable.column("department",width=100)
        self.AttendannceReportTable.column("time",width=100)
        self.AttendannceReportTable.column("date",width=100)
        self.AttendannceReportTable.column("attendance",width=100)
        
        self.AttendannceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendannceReportTable.bind("<ButtonRelease>",self.get_cursor)
    
    # =============== Fatch Data ===============
    
    def fetchData(self,rows):
        self.AttendannceReportTable.delete(*self.AttendannceReportTable.get_children())
        for i in rows:
            self.AttendannceReportTable.insert("",END,values=i)
    
    # Import csv 
    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                ccsvread=csv.reader(myfile,delimiter=",")
                for i in ccsvread:
                    mydata.append(i)
                self.fetchData(mydata)
        
    # Export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=s=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root);
    
    
    def get_cursor(self,event=""):
        cursor_row=self.AttendannceReportTable.focus()
        content=self.AttendannceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    # Reset data function
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
           
        
if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()