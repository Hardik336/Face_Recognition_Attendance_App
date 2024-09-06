from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser  # To open the default web browser

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="WHITE", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img2_top = Image.open(r"C:\Users\hardik\OneDrive\Documents\Desktop\Face_Recognition_System\1628243597666college-images\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img2_top = img2_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img2_top)

        f_lbl2 = Label(self.root, image=self.photoimg_top)
        f_lbl2.place(x=0, y=55, width=1530, height=720)

        # Create a button that opens Gmail
        email_button = Button(f_lbl2, text="Send Mail on valahardik336@gmail.com", font=("times new roman", 20, "bold"), fg="blue", bg="white", command=self.send_email)
        email_button.place(x=500, y=200)

    def send_email(self):
        # Opens the default web browser with Gmail compose URL
        webbrowser.open("https://mail.google.com/mail/?view=cm&fs=1&to=valahardik336@gmail.com")

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
