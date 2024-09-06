from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import smtplib

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

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
