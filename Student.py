from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2.data
from mysql.connector import (connection)
# import mysql.connector
import cv2
import os



class Student_Management_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x650+0+0")
        self.root.title(" Student Management System")
        
        # ================================ Variable +========================================================
        
        self.Department=StringVar()
        self.Course=StringVar()
        self.Year=StringVar()
        self.Semester=StringVar()
        self.id=StringVar()
        self.Name=StringVar()
        self.Division=StringVar()
        self.Roll_no=StringVar()
        self.Gender=StringVar()
        self.DOB=StringVar()
        self.Email=StringVar()
        self.Phone=StringVar()
        self.Address=StringVar()
        

        
        img = Image.open(r"Images\student_header.webp")
        img = img.resize((500,110))
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        # Second Image

        img1 = Image.open(r"Images\student_hader1.jpeg")
        img1 = img1.resize((500,110))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        # Third image
        
        
        img2 = Image.open(r"Images\student_hader2.jpeg")
        img2 = img2.resize((500,110))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        
        # =================================== Bg Image =======================================
        
        img3 = Image.open(r"Images\student_records1.jpg")
        img3 = img3.resize((1400,510))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_image = Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=130,width=1400,height=605)
        
        # ================================== Inside the bg Title =========================================
        
        title_lbl = Label(bg_image,text="STUDENT MANAGEMENT SYSTEM",font=(" times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0, width=1400,height=45)
        
        # ================================================ Main Frame ================================================
        
        main_frame = Frame(bg_image,bd=2,bg="light blue")
        main_frame.place(x=10,y=50,width=1340,height=500)
        
        # ================================================ Left  Frame ================================================
        left_frame = LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=1,width=650,height=495)
        
        img_left = Image.open(r"Images\student_records1.jpg")
        img_left = img_left.resize((650,90))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=635,height=90)
        
        # =========================================== Current course ===========================================
        
        Currnt_course_frame = LabelFrame(left_frame,bd=3,bg="white",relief=RIDGE,text="Corrent Course information",font=("times new roman",12,"bold"))
        Currnt_course_frame.place(x=10,y=90,width=630,height=115)
        
        # Department 
        
        dep_label_frame = Label(Currnt_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label_frame.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo =ttk.Combobox(Currnt_course_frame,textvariable=self.Department,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"] = ("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
        
        # Course
        
        dep_label_frame = Label(Currnt_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label_frame.grid(row=0,column=2,padx=10,sticky=W)
        
        dep_combo =ttk.Combobox(Currnt_course_frame,textvariable=self.Course,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"] = ("Select Course","MCA","B-Tech","B-Tech CS","BCA")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=8,sticky=W)
        
        # Year
        
        dep_label_frame = Label(Currnt_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        dep_label_frame.grid(row=1,column=0,padx=10,sticky=W)
        
        dep_combo =ttk.Combobox(Currnt_course_frame,textvariable=self.Year,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"] = ("Select Year","2020","2021","2022","2023","2024","2025")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=8,sticky=W)
        
        # semester
        
        dep_label_frame = Label(Currnt_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        dep_label_frame.grid(row=1,column=2,padx=10,sticky=W)
        
        dep_combo =ttk.Combobox(Currnt_course_frame,textvariable=self.Semester,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"] = ("Select Semester","First","Second","Third","Fourth","Five","Six")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=8,sticky=W)
        
        # ============================== Class Student Information =================================
        
        Class_Student_frame = LabelFrame(left_frame,bd=3,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=10,y=205,width=630,height=265)
        
        # ============================== Student Id Label ==========================================================
        # Student ID
        student_id_frame = Label(Class_Student_frame,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
        student_id_frame.grid(row=0,column=0,padx=8,pady=2,sticky=W)
        
        studentid_entry =ttk.Entry(Class_Student_frame,textvariable=self.id,width=20,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=8,pady=2,sticky=W)
        
        # Students name
        
        studentname_frame = Label(Class_Student_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        studentname_frame.grid(row=0,column=2,padx=8,pady=2,sticky=W)
        
        studentname_entry =ttk.Entry(Class_Student_frame,textvariable=self.Name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=8,pady=2,sticky=W)
        
        # Class Division
        
        class_div_frame = Label(Class_Student_frame,text="Class Division :",font=("times new roman",12,"bold"),bg="white")
        class_div_frame.grid(row=1,column=0,padx=8,pady=2,sticky=W)
        
        # class_div_entry =ttk.Entry(Class_Student_frame,textvariable=self.Division,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=8,pady=2,sticky=W)

        Class_div_combo =ttk.Combobox(Class_Student_frame,textvariable=self.Division,font=("times new roman",12,"bold"),
        state="readonly",width=18)
        Class_div_combo["values"] = ("A","B","C","D")
        Class_div_combo.current(0)
        Class_div_combo.grid(row=1,column=1,padx=8,pady=2,sticky=W)
        
        
        # Roll No
        
        roll_no_frame = Label(Class_Student_frame,text="Roll No :",font=("times new roman",12,"bold"),bg="white")
        roll_no_frame.grid(row=1,column=2,padx=8,pady=2,sticky=W)
        
        roll_no_entry =ttk.Entry(Class_Student_frame,textvariable=self.Roll_no,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=8,pady=2,sticky=W)
        
        # Gender
        
        Gender_frame = Label(Class_Student_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        Gender_frame.grid(row=2,column=0,padx=8,pady=2,sticky=W)
        
        # Gender_entry =ttk.Entry(Class_Student_frame,textvariable=self.Gender,width=20,font=("times new roman",12,"bold"))
        # Gender_entry.grid(row=2,column=1,padx=8,pady=2,sticky=W)

        Gender_combo =ttk.Combobox(Class_Student_frame,textvariable=self.Gender,font=("times new roman",12,"bold"),
        state="readonly",width=18)
        Gender_combo["values"] = ("Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=8,pady=2,sticky=W)
        
        # Date of Birth
        
        date_of_birth_frame = Label(Class_Student_frame,text="Date of Birth :",font=("times new roman",12,"bold"),bg="white")
        date_of_birth_frame.grid(row=2,column=2,padx=8,pady=2,sticky=W)
        
        date_of_birth_entry =ttk.Entry(Class_Student_frame,textvariable=self.DOB,width=20,font=("times new roman",12,"bold"))
        date_of_birth_entry.grid(row=2,column=3,padx=8,pady=2,sticky=W)
        
        # Email
        
        Email_frame = Label(Class_Student_frame,text="Email :",font=("times new roman",12,"bold"),bg="white")
        Email_frame.grid(row=3,column=0,padx=8,pady=2,sticky=W)
        
        Email_entry =ttk.Entry(Class_Student_frame,textvariable=self.Email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=3,column=1,padx=8,pady=2,sticky=W)
        
        # Phone
        
        Phone_frame = Label(Class_Student_frame,text="Phone :",font=("times new roman",12,"bold"),bg="white")
        Phone_frame.grid(row=3,column=2,padx=8,pady=2,sticky=W)
        
        Phone_entry =ttk.Entry(Class_Student_frame,textvariable=self.Phone,width=20,font=("times new roman",12,"bold"))
        Phone_entry.grid(row=3,column=3,padx=8,pady=2,sticky=W)
        
        # Address
        
        Adress_frame = Label(Class_Student_frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
        Adress_frame.grid(row=4,column=0,padx=8,pady=2,sticky=W)
        
        Adress_entry =ttk.Entry(Class_Student_frame,textvariable=self.Address,width=20,font=("times new roman",12,"bold"))
        Adress_entry.grid(row=4,column=1,padx=8,pady=2,sticky=W)
        
        # ============================================= Radio Button ===================================================
        self.PhotoSample=StringVar()
        radiobutton1 = Radiobutton(Class_Student_frame,variable=self.PhotoSample,text="Take Photo Sample",value="Yes",font=("times new roman",10,"bold"),bg="white")
        radiobutton1.grid(row=6,column=0,padx=2,pady=3) 
        
        radiobutton2 = Radiobutton(Class_Student_frame,variable=self.PhotoSample,text="No Photo Sample",value="No",font=("times new roman",10,"bold"),bg="white")
        radiobutton2.grid(row=6,column=1,padx=2,pady=3)
        
        # ============================================== Button Frame =========================================================
        
        btn_frame =Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=170,width=615,height=70)
        
        # save button
        save_btn = Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",10,"bold"),bg="green",fg="white",width=18)
        save_btn.grid(row=0,column=0,padx=8,pady=5,sticky=W)
        
        # Update button
        Update_btn = Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",10,"bold"),bg="green",fg="white",width=18)
        Update_btn.grid(row=0,column=1,padx=8,pady=5,sticky=W)
        
        # Delete button
        Delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",10,"bold"),bg="green",fg="white",width=18)
        Delete_btn.grid(row=0,column=2,padx=8,pady=5,sticky=W)
        
        # Reset button
        Reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",10,"bold"),bg="green",fg="white",width=18)
        Reset_btn.grid(row=0,column=3,padx=8,pady=5,sticky=W)
        
        btn_frame1 =Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=205,width=615,height=35)    
        # Take photo button
        Take_Photo_btn = Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,font=("times new roman",10,"bold"),bg="green",fg="white",width=40)
        Take_Photo_btn.grid(row=0,column=0,padx=8,pady=3,sticky=W)
        
        
        
        Upload_photo_btn = Button(btn_frame1,text="Upload Photo Sample",font=("times new roman",10,"bold"),bg="green",fg="white",width=40)
        Upload_photo_btn.grid(row=0,column=1,padx=8,pady=3,sticky=W)
        # ================================================ right  Frame ================================================
        right_frame = LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=675,y=1,width=650,height=490)
        
        img_right = Image.open(r"Images\photo.jpg")
        img_right = img_right.resize((650,100))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=635,height=90)
        
        
        
        
        
        
        # ============================================= Search System =======================================================
        
        Search_frame = LabelFrame(right_frame,bd=3,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=90,width=635,height=70)
        
        Search_label = Label(Search_frame,text="Search By :",font=("times new roman",12,"bold"),bg="white")
        Search_label.grid(row=0,column=0,padx=8,pady=2,sticky=W)
        
        serach_combo =ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=10)
        serach_combo["values"] = ("Select ","Roll_No","Phone_No")
        serach_combo.current(0)
        serach_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
        
        # Entry Field
        Search_entry =ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=2,pady=2,sticky=W)
        
        
        
        # Search button
        Search_btn = Button(Search_frame,text="Search",font=("times new roman",10,"bold"),bg="green",fg="white",width=15)
        Search_btn.grid(row=0,column=3,padx=8,pady=5,sticky=W)
        
        # Show All button
        showall_btn = Button(Search_frame,text="Show All",font=("times new roman",10,"bold"),bg="green",fg="white",width=15)
        showall_btn.grid(row=0,column=4,padx=8,pady=5,sticky=W)
        
        
        # ====================================================== Table Frame =================================================
        
        Table_frame =Frame(right_frame,bd=3,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=165,width=635,height=300)
        
        # ScrollBar
        scroll_x =ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.student_table =ttk.Treeview(Table_frame,columns=("Department","Course","Year","Semester","id","Name","Division","Roll_no","Gender","DOB","Email","Phone","Address","PhotoSample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # column Heading
        
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semster")
        self.student_table.heading("id",text="Student_ID")
        self.student_table.heading("Name",text="Student_Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll_no",text="Roll_no")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="Date_of_Birth")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("PhotoSample",text="PhotoSample")
        self.student_table["show"]="headings"

        # set column Width
        
        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("Roll_no",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("PhotoSample",width=100)
        
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cousor)
        self.fetch_data()
        
        # ========================================== Function Declaration & Insert data =====================================
        
    def add_data(self):
        if self.Department.get()=="Select Department" or self.id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            # messagebox.showinfo("Sccuess!","Welcome to addd field")
            try:
                conn = connection.MySQLConnection(user='root', password='Ravi9731@',
                host='127.0.0.1',
                database='Student_db')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",(
                                                                                                                    self.Department.get(),
                                                                                                                    self.Course.get(),
                                                                                                                    self.Year.get(),
                                                                                                                    self.Semester.get(),
                                                                                                                    self.id.get(),
                                                                                                                    self.Name.get(),
                                                                                                                    self.Division.get(),
                                                                                                                    self.Roll_no.get(),
                                                                                                                    self.Gender.get(),
                                                                                                                    self.DOB.get(),
                                                                                                                    self.Email.get(),
                                                                                                                    self.Phone.get(),
                                                                                                                    self.Address.get(),
                                                                                                                    self.PhotoSample.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    # ======================================================== Fetch Data ======================================================
    def fetch_data(self):
        conn = connection.MySQLConnection(user='root', password='Ravi9731@',
        host='127.0.0.1',
        database='Student_db')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    # ====================================================== get cursor ====================================================
    def get_cousor(self,event=""):
        cousor_focus=self.student_table.focus()
        content=self.student_table.item(cousor_focus)
        data=content["values"]

        self.Department.set(data[0]),
        self.Course.set(data[1]),
        self.Year.set(data[2]),
        self.Semester.set(data[3]),
        self.id.set(data[4]),
        self.Name.set(data[5]),
        self.Division.set(data[6]),
        self.Roll_no.set(data[7]),
        self.Gender.set(data[8]),
        self.DOB.set(data[9]),
        self.Email.set(data[10]),
        self.Phone.set(data[11]),
        self.Address.set(data[12]),
        self.PhotoSample.set(data[13])
        # self.usertype.set(data[14])

    # =========================================== Update Function ============================================
    def update_data(self):
        if self.Department.get()=="Select Department" or self.id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn = connection.MySQLConnection(user='root', password='Ravi9731@',
                    host='127.0.0.1',
                    database='Student_db')
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where id=%s", (
                                                                                                        self.Department.get(),
                                                                                                        self.Course.get(),
                                                                                                        self.Year.get(),
                                                                                                        self.Semester.get(),
                                                                                                        self.Name.get(),
                                                                                                        self.Division.get(),
                                                                                                        self.Roll_no.get(),
                                                                                                        self.Gender.get(),
                                                                                                        self.DOB.get(),
                                                                                                        self.Email.get(),
                                                                                                        self.Phone.get(),
                                                                                                        self.Address.get(),
                                                                                                        self.PhotoSample.get(),
                                                                                                        self.id.get()
                                                                                                    ))
                    
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details have been updated successfully.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    # ================================================ delete function ====================================================
    def delete_data(self):
        if self.id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do You want to delete this student",parent=self.root)
                if delete>0:
                    conn = connection.MySQLConnection(user='root', password='Ravi9731@',
                    host='127.0.0.1',
                    database='Student_db')
                    my_cursor = conn.cursor()
                    sql = "delete from student where id = %s"
                    val = (self.id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student detials",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ==================================================== reset function ==================================================
    def reset_data(self):
        self.Department.set("Select Department")
        self.Course.set("Select Course")
        self.Year.set("Select Year")
        self.Semester.set("Select Semester")
        self.id.set("")
        self.Name.set("")
        self.Division.set("Select Division")
        self.Roll_no.set("")
        self.Gender.set("Gender")
        self.DOB.set("")
        self.Email.set("")
        self.Phone.set("")
        self.Address.set("")
        self.PhotoSample.set("")


    #================================ Generate data set or Take a photo sample ====================================            



    def generate_dataset(self):
        if self.Department.get()=="Select Department" or self.id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = connection.MySQLConnection(user='root', password='Ravi9731@',
                host='127.0.0.1',
                database='Student_db')
                my_cursor = conn.cursor()
                
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id = 0
                for i in myresult:
                    id += 1
                my_cursor.execute("UPDATE student SET Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where id=%s",(
                                                                                                        self.Department.get(),
                                                                                                        self.Course.get(),
                                                                                                        self.Year.get(),
                                                                                                        self.Semester.get(),
                                                                                                        self.Name.get(),
                                                                                                        self.Division.get(),
                                                                                                        self.Roll_no.get(),
                                                                                                        self.Gender.get(),
                                                                                                        self.DOB.get(),
                                                                                                        self.Email.get(),
                                                                                                        self.Phone.get(),
                                                                                                        self.Address.get(),
                                                                                                        self.PhotoSample.get(),
                                                                                                        self.id.get()==id+1
                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #  =================== load predifined data set ====================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_croped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x,y,w,h) in faces:
                        face_croped = img[y:y+h,x:x+w]
                        return face_croped
                # ==================== load predefined data set ====================
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_croped(my_frame),(450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face, str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Croped Face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                
if __name__ == "__main__":
    root=Tk()
    obj=Student_Management_System(root)
    root.mainloop()