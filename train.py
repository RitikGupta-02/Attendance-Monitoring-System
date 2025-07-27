from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np







class Train_data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x650+0+0")
        self.root.title(" Train Data Management System")



        title_lbl = Label(self.root,text="TRAIN DATA SET",font=(" times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0, width=1400,height=45)

        # ============================================ Image Top ============================================================
        img_top = Image.open(r"Images\train_final11.jpeg")
        img_top = img_top.resize((1400,225))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
 
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1400,height=230)

        # ============================================ BUTTON ================================================================

        b1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor='hand2',font=(" times new roman",20,
        "bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=260,width=1400,height=40)
        
                
        # ============================================= image Buttom ========================================================

        img_buttom = Image.open(r"Images\train_final.webp")
        img_buttom = img_buttom.resize((1400,325))
        self.photoimg_buttom = ImageTk.PhotoImage(img_buttom)
        f_lbl = Label(self.root,image=self.photoimg_buttom)
        f_lbl.place(x=0,y=300,width=1400,height=325)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            # cv2.imread(imageNp)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 27
        ids = np.array(ids)
        # Train the classifier and save it to the file system
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed successfully")











if __name__ == "__main__":
    root=Tk()
    obj=Train_data(root)
    root.mainloop()