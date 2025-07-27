from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from mysql.connector import (connection)
from time import strftime
from datetime import datetime
import cv2
import os







class Face_Recgnition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x800+0+0")
        self.root.title(" Face Recognition System") 
        
        title_lbl = Label(self.root,text="FACE RECOGNITION SYSTEM",font=(" times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0, width=1400,height=45)
        # First Image 
        img_top = Image.open(r"Images\final_face_112.jpg")
        img_top = img_top.resize((700,700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
         
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=600,height=650)
        # Second Image
        img_buttom = Image.open(r"Images\final_face_2.webp")
        img_buttom = img_buttom.resize((900,700))
        self.photoimg_buttom = ImageTk.PhotoImage(img_buttom)
        f_lbl = Label(self.root,image=self.photoimg_buttom)
        f_lbl.place(x=600,y=50,width=800,height=650)

        b1_1 = Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor='hand2',font=(" times new roman",14,
        "bold"),bg="darkgreen",fg="white")
        b1_1.place(x=300,y=595,width=190,height=40)

        # ===================== Attendance ==========================================
    def mark_attendance(self,i,n,r,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i) not in name_list) and ((n) not in name_list) and ((r) not in name_list) and ((d) not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{d},{dtString},{d1},Present")
                messagebox.showinfo("Attendance","Attendance marked successfully")
            else:
                messagebox.showerror("Error","Attendance already marked")


        # ============================== Face Recognition =======================================
    def face_recog(self):
        marked_ids = set()  # Track attendance in current session

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Database connection
                conn = connection.MySQLConnection(user='root', password='Ravi9731@',
                                                  host='127.0.0.1', database='Student_db')
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT id, Roll_no, Name, Department FROM student WHERE id=%s", (id,))
                result = my_cursor.fetchone()
                conn.close()

                if result:
                    i, r, n, d = map(str, result)
                    if confidence > 77:
                        cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll No: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        # Mark attendance only once per session
                        if i not in marked_ids:
                            self.mark_attendance(i, n, r, d)
                            marked_ids.add(i)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        # Load the face cascade and trained model
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # Start video capture
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 27:  # Press 'Esc' key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recgnition(root)
    root.mainloop()