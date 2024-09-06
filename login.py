from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import smtplib

# from main import Face_Recognition_System

def main():
    win=Tk()
    app=Loin_Window(win)
    win.mainloop()



class Loin_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.var_email = StringVar()
        self.var_pass = StringVar()

        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\312976-free-download-log-on-to-your-bank-account-on-a-laptop-logging.png")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        # =========== Label ===========
        
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.txtpassword=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpassword.place(x=40,y=250,width=270)
        
        # ===== Icon Images =====
        # username
        img2=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        # password
        img3=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=394,width=25,height=25)
        
        # Login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        # Register Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        # forgot password
        Fpasswordbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        Fpasswordbtn.place(x=10,y=370,width=160)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    # def login(self):
    #     if self.txtuser.get()=="" or self.txtpassword.get()=="":
    #         messagebox.showerror("Error","ALl field required !!")
    #     elif self.txtuser.get()=="Hardik" and self.txtpassword.get()=="Hardik50":
    #         messagebox.showinfo("Success","Welcome to Face Recognition Project")
    #     else:
    #         conn = mysql.connector.connect(host="localhost", user="root", password="Hardik50", database="face_recognizer")
    #         my_cursor = conn.cursor()
    #         my_cursor.execute("select * from register where email=%s and password=%s",(
    #                                                                                 self.txtuser.get(),
    #                                                                                 self.txtpassword.get()
    #                                                                             ))
    #         row=my_cursor.fetchone()
    # def login(self):
    # # Check if any fields are empty
    #     if self.txtuser.get() == "" or self.txtpassword.get() == "":
    #         messagebox.showerror("Error", "All fields are required!")
    #     else:
        
    #         # Connect to the database
    #         conn = mysql.connector.connect(
    #             host="localhost",
    #             user="root",
    #             password="Hardik50",  # Your MySQL root password
    #             database="face_recognizer"
    #         )
    #         my_cursor = conn.cursor()

    #         # Query to check if the username (email) and password match
    #         query = "SELECT * FROM register WHERE email=%s AND password=%s"
    #         my_cursor.execute(query, (self.txtuser.get(), self.txtpassword.get()))
            
    #         row = my_cursor.fetchone()

    #         if row == None:
    #             messagebox.showerror("Error","Invalid Username & password")
    #         else:
    #             open_main=messagebox.askyesno("YesNo","Access only admin")
    #             if open_main>0:
    #                 self.new_window=Toplevel(self.new_window)
    #                 self.app=Face_Recognition_System(self.new_window)
    #             else:
    #                 if not open_main:
    #                     return
    #         conn.commit()
    #         conn.close()
    
    # new Chat GPT
    from main import Face_Recognition_System  # Import the Face Recognition class from main.py

    def login(self):
        # Check if any fields are empty
        if self.txtuser.get() == "" or self.txtpassword.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                # Connect to the database
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Hardik50",  # Your MySQL root password
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
    
                # Query to check if the username (email) and password match
                query = "SELECT * FROM register WHERE email=%s AND password=%s"
                my_cursor.execute(query, (self.txtuser.get(), self.txtpassword.get()))
                
                row = my_cursor.fetchone()
    
                if row is None:
                    messagebox.showerror("Error", "Invalid Username & password")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main > 0:
                        self.new_window = Toplevel(self.root)  # Create a new top-level window
                        self.app = Face_Recognition_System(self.new_window)  # Open the Face Recognition System
                    else:
                        return
    
                conn.commit()
    
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")
            
            finally:
                conn.close()


# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import smtplib

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        # ======== Variables ========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        
        # ========== bg image ===========
        image = Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\iStock-1163542789-945x630.jpg")
        resized_image = image.resize((1600, 900), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(resized_image)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ============ left image ============
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # Main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        # Labels
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # ======= Labels and Entry =======
        # First Name
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        self.fname = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        self.fname.place(x=50, y=130, width=250)

        # Last Name
        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # Contact
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        # Email
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # Security Question ComboBox
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Friend's name", "Your favorite book")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        # Security Answer
        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # Password
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)
        self.txt_pass = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pass.place(x=50, y=340, width=250)

        # Confirm Password
        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)
        self.txt_confpass = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confpass.place(x=370, y=340, width=250)

        # ======= Check Button =======
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree to the Terms & Conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # ========== Buttons =========
        img = Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\register-now-button1.jpg")
        img = img.resize((200, 55), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2")
        b1.place(x=50, y=420, width=200)

        img1 = Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\loginpng.png")
        img1 = img1.resize((200, 45), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b2.place(x=400, y=420, width=200)

    # ======= Function Declaration =========
    def send_email(self, to_email, name, password):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("valahardik336@gmail.com", "obac gwce wupc lrdn")  # Use your app-specific password here
            subject = "Registration Successful"
            body = f"Hello {name},\n\nYour registration is successfully completed. Your password is: {password}."
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail("valahardik336@gmail.com", to_email, message)
            server.quit()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {str(e)}")

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and confirm password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Hardik50", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is not None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_SecurityA.get(),
                    self.var_pass.get()
                ))
                conn.commit()
                conn.close()
                
                # Send email after successful registration
                self.send_email(self.var_email.get(), self.var_fname.get(), self.var_pass.get())
                messagebox.showinfo("Success", "Registered successfully. A confirmation email has been sent.")

# main.py
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from Email import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        
        # Image 1
        img=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.LANCZOS);
        self.photoimg=ImageTk.PhotoImage(img);
        
        f_lbl=Label(self.root,image=self.photoimg);
        f_lbl.place(x=0,y=0,width=500,height=130);
        
        # Image 2
        img1=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.LANCZOS);
        self.photoimg1=ImageTk.PhotoImage(img1);
        
        f_lbl1=Label(self.root,image=self.photoimg1);
        f_lbl1.place(x=500,y=0,width=500,height=130);
        
        # Image 3
        img2=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\images.jpg")
        img2=img2.resize((500,130),Image.LANCZOS);
        self.photoimg2=ImageTk.PhotoImage(img2);
        
        f_lbl2=Label(self.root,image=self.photoimg2);
        f_lbl2.place(x=1000,y=0,width=550,height=130);
        
        
        # # Background Image
        img3=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\bjimg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS);
        self.photoimg3=ImageTk.PhotoImage(img3);
        
        bg_img=Label(self.root,image=self.photoimg3);
        bg_img.place(x=0,y=130,width=1530,height=710);
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE  SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="GREEN");
        title_lbl.place(x=0,y=0,width=1530,height=45);
        
        # ======= Time =========
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
            
        lbl= Label(title_lbl,font=("times new roman",14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        
        # Student button
        img4=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\student.jpg")
        img4=img4.resize((220,220),Image.LANCZOS);
        self.photoimg4=ImageTk.PhotoImage(img4);
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2");
        b1.place(x=200,y=100,width=220,height=220);
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white");
        b1_1.place(x=200,y=300,width=220,height=40);
        
        # Detect Face Button
        img5=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS);
        self.photoimg5=ImageTk.PhotoImage(img5);
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data);
        b1.place(x=500,y=100,width=220,height=220);
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white");
        b1_1.place(x=500,y=300,width=220,height=40);
        
        # Attendance button
        img6=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\report.jpg")
        img6=img6.resize((220,220),Image.LANCZOS);
        self.photoimg6=ImageTk.PhotoImage(img6);
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data);
        b1.place(x=800,y=100,width=220,height=220);
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white");
        b1_1.place(x=800,y=300,width=220,height=40);
        
        # Help Button
        img7=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,220),Image.LANCZOS);
        self.photoimg7=ImageTk.PhotoImage(img7);
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data);
        b1.place(x=1100,y=100,width=220,height=220);
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white");
        b1_1.place(x=1100,y=300,width=220,height=40);
        
        # Train Button
        img8=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS);
        self.photoimg8=ImageTk.PhotoImage(img8);
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data);
        b1.place(x=200,y=380,width=220,height=220);
        
        b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white");
        b1_1.place(x=200,y=580,width=220,height=40);
        
        # Photos Button
        img9=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.LANCZOS);
        self.photoimg9=ImageTk.PhotoImage(img9);
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img);
        b1.place(x=500,y=380,width=220,height=220);
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white");
        b1_1.place(x=500,y=580,width=220,height=40);
        
        
         # Developer Button
        img10=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.LANCZOS);
        self.photoimg10=ImageTk.PhotoImage(img10);
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data);
        b1.place(x=800,y=380,width=220,height=220);
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white");
        b1_1.place(x=800,y=580,width=220,height=40);
        
        # Exit Button
        img11=Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS);
        self.photoimg11=ImageTk.PhotoImage(img11);
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.IExit);
        b1.place(x=1100,y=380,width=220,height=220);
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.IExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white");
        b1_1.place(x=1100,y=580,width=220,height=40);
        
    def open_img(self):
        os.startfile("data");
    
    def IExit(self):
        self.IExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.IExit >0:
            self.root.destroy()
        else:
            return
    
    # ======== Functions buttons ========
        
    def student_details(self):
        self.new_window=Toplevel(self.root);
        self.app=Student(self.new_window);
            
            
            
    # ======== Functions Train buttons ========
        
    def train_data(self):
        self.new_window=Toplevel(self.root);
        self.app=Train(self.new_window);
        
    def face_data(self):
        self.new_window=Toplevel(self.root);
        self.app=Face_Recognition(self.new_window);
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root);
        self.app=Attendance(self.new_window);
    
    # Function for developer.py
    def developer_data(self):
        self.new_window=Toplevel(self.root);
        self.app=Developer(self.new_window);
    
    # Function for help.py
    def help_data(self):
        self.new_window=Toplevel(self.root);
        self.app=Help(self.new_window);
        
# if __name__== "__main__":
#     root=Tk()
#     obj=Face_Recognition_System(root)
#     root.mainloop()

if __name__ == "__main__":
    main()