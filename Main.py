from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
import os
from tkinter import messagebox
from Student import Student_Management_System
from train import Train_data
from face_recognition import Face_Recgnition
from attendance import Attendance
from devleoper import create_developer_page
from help import HelpDeskChatbot

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x650+0+0")
        self.root.title("Face Recognition System")
        # First Image
        

        img=Image.open(r"Images\main_header.jpg")
        img = img.resize((500,110))
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        # Second Image
        
        img1 = Image.open(r"Images\main_hader1.webp")
        img1 = img1.resize((500,110))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        # Third image
     
        # 
        img2 = Image.open(r"Images\main_hader2.jpg")
        img2 = img2.resize((500,110))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        # 
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        # =================================== Bg Image =======================================
        # 
        img3 = Image.open(r"Images\background.jpeg")
        img3 = img3.resize((1400,510))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        # 
        bg_image = Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=130,width=1400,height=600)
        #
         
       # ================================== Inside the bg Title =========================================
        # 
        title_lbl = Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=(" times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0, width=1400,height=45)
       
       
        # ====================================== Student Button ====================================================
        
        img4 = Image.open(r"Images\student.png")
        img4 = img4.resize((230,150))
        self.photoimg4 = ImageTk.PhotoImage(img4)
         
        b1 = Button(bg_image,image=self.photoimg4,command=self.Student_details,cursor='hand2')
        b1.place(x=150,y=80,width=220,height=150)
         
        
        b1_1 = Button(bg_image,text="Student Details",command=self.Student_details,cursor='hand2',font=(" times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=220,width=220,height=40)
        # 
        # ================================== Detect Face Second Button =========================================================
        img5 = Image.open(r"Images\face1.jpg")
        img5 = img5.resize((220,150))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        # 
        b1 = Button(bg_image,image=self.photoimg5,cursor='hand2',command=self.face_data)
        b1.place(x=450,y=80,width=220,height=150)
        # 
        # 
        b1_1 = Button(bg_image,text="Face Detector",cursor='hand2',command=self.face_data,font=(" times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=220,width=220,height=40)
        # 
        # ========================================== Attendance Button ========================================
        img6 = Image.open(r"Images\attendance.jpg")
        img6 = img6.resize((230,150))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        # 
        b1 = Button(bg_image,image=self.photoimg6,cursor='hand2',command=self.attendance_data)
        b1.place(x=750,y=80,width=220,height=150)
        # 
        # 
        b1_1 = Button(bg_image,text="Attenndance",cursor='hand2',command=self.attendance_data,font=(" times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=750,y=220,width=220,height=40)
        # 
        # ============================================ help desk Button ========================================
        # 
        img7 = Image.open(r"Images\helpdesk.jpg")
        img7 = img7.resize((230,150))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        # 
        b1 = Button(bg_image,image=self.photoimg7,command=self.help,cursor='hand2')
        b1.place(x=1050,y=80,width=220,height=150)
        # 
        # 
        b1_1 = Button(bg_image,text="Help Desk",command=self.help,font=(" times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=220,width=220,height=40)
        # 
        # 
        # ===============================================  Train Button ============================================
        # 
        img8 = Image.open(r"Images\train.jpeg")
        img8 = img8.resize((230,150))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        # 
        b1 = Button(bg_image,image=self.photoimg8,cursor='hand2',command=self.train_data)
        b1.place(x=150,y=300,width=220,height=150)
        # 
        # 
        b1_1 = Button(bg_image,text="Train Data",cursor='hand2',command=self.train_data,font=(" times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=450,width=220,height=40)
        # 
        # ================================================== Photos Button ==============================================
        # 
        img9 = Image.open(r"Images\photo.jpg")
        img9 = img9.resize((230,150))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        # 
        b1 = Button(bg_image,image=self.photoimg9,cursor='hand2',command=self.open_img)
        b1.place(x=450,y=300,width=220,height=150)
        # 
        #   
        b1_1 = Button(bg_image,text="Photos ",cursor='hand2',command=self.open_img,font=(" times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=450,width=220,height=40)
        # 
        # ====================================================== Developer Button =============================================
        # 
        img10 = Image.open(r"Images\deve.png")
        img10 = img10.resize((230,150))
        self.photoimg10 = ImageTk.PhotoImage(img10)
        # 
        b1 = Button(bg_image,image=self.photoimg10,cursor='hand2',command=self.Developer)
        b1.place(x=750,y=300,width=220,height=150)  
        # 
        # 
        b1_1 = Button(bg_image,text="Developer",cursor='hand2',command=self.Developer,font=(" times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=750,y=450,width=220,height=40)
        # 
        # ====================================================== Exits Button ==============================================
        # 
        img11 = Image.open(r"C:\Users\1990p\desktop\Programming\Machine_learing_Projects\Major_Projects\Images\exits.jpg")
        img11 = img11.resize((230,150))
        self.photoimg11 = ImageTk.PhotoImage(img11)
        # 
        b1 = Button(bg_image,image=self.photoimg11,cursor='hand2',command=self.exit_data)
        b1.place(x=1050,y=300,width=220,height=150)
        # 
        # 
        b1_1 = Button(bg_image,text="Exits",cursor='hand2',command=self.exit_data,font=(" times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=450,width=220,height=40)

    def open_img(self):
        os.startfile("data")
        
        # =========================================== Function Button ================================================
        
    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Management_System(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_data(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recgnition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def exit_data(self):
        confirm_exit_b = messagebox.askyesno("Exit","Are you sure you want to exit?",parent=self.root)
        if confirm_exit_b:
            self.root.destroy()
        exit()

    def Developer(self):
        self.new_window = Toplevel(self.root)
        self.app = create_developer_page(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = HelpDeskChatbot(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

