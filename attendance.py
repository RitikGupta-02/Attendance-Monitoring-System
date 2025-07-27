from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from mysql.connector import (connection)
from time import strftime
from datetime import datetime
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x800+0+0")
        self.root.title(" Attendance System") 
        
        # Variables
        self.attendance_id = StringVar()
        self.student_name = StringVar()
        self.roll_no = StringVar()
        self.department = StringVar()
        self.time = StringVar()
        self.date = StringVar()
        self.attendance_status = StringVar()

        img = Image.open(r"Images\background.jpeg")
        img = img.resize((750,140))
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=-80,y=0,width=800,height=100)
        # Second Image
        
        
        img1 = Image.open(r"Images\attendance1.jpg")
        img1 = img1.resize((750,140))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=650,y=0,width=750,height=100)

        
        
        

        #============================ bg image ==================================
        img3 = Image.open(r"Images\background.jpeg")
        img3 = img3.resize((1400,810))
        self.photoimg3 = ImageTk.PhotoImage(img3)
                
        bg_image = Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=103,width=1400,height=800)

        # title
        title_lbl = Label(bg_image,text="Attendance Management System",font=(" times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0, width=1400,height=45)

        # main frame
        main_frame = Frame(bg_image,bd=2,bg="light blue")
        main_frame.place(x=5,y=50,width=1340,height=520)

        # ================================================ Left  Frame ================================================
        left_frame = LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,
        "bold"))
        left_frame.place(x=10,y=1,width=650,height=495)
                
        img_left = Image.open(r"Images\attendance.jpg")
        img_left = img_left.resize((680,110))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
                
        f_lbl = Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=680,height=100)
        # inside left frame
        left_inside_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="light blue")
        left_inside_frame.place(x=3,y=105,width=638,height=360)

        # ================================== Label and Entry ==================================================
        # Attendance ID
        attendance_id_label = Label(left_inside_frame,text="Attendance ID :",font=("times new roman",12,"bold"),bg="light blue")
        attendance_id_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        attendance_id_entry = ttk.Entry(left_inside_frame, textvariable=self.attendance_id, width=20, font=("times new roman", 12, "bold"))
        attendance_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Student Name
        student_name_label = Label(left_inside_frame,text="Student Name",font=("times new roman",12,"bold"),bg="light blue")
        student_name_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        student_name_entry = ttk.Entry(left_inside_frame, textvariable=self.student_name, width=20, font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Roll No
        roll_no_label = Label(left_inside_frame,text="Roll No",font=("times new roman",12,"bold"),bg="light blue")
        roll_no_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        roll_no_entry = ttk.Entry(left_inside_frame, textvariable=self.roll_no, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Department
        department_label = Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg="light blue")
        department_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        department_entry = ttk.Entry(left_inside_frame, textvariable=self.department, width=20, font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        # Time
        time_label = Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"),bg="light blue")
        time_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        time_entry = ttk.Entry(left_inside_frame, textvariable=self.time, width=20, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        # Date
        date_label = Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"),bg="light blue")
        date_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        date_entry = ttk.Entry(left_inside_frame, textvariable=self.date, width=20, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        # Attendance Status
        attendance_status_label = Label(left_inside_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="light blue")
        attendance_status_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)    
        self.attendance_status_combo = ttk.Combobox(left_inside_frame, textvariable=self.attendance_status, font=("times new roman", 12, "bold"), width=18, state="readonly")
        self.attendance_status_combo["values"] = ("Status", "Present", "Absent")
        self.attendance_status_combo.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        self.attendance_status_combo.current(0)

        # ============================= Button Frame ==========================================
        button_frame = Frame(left_inside_frame,relief=RIDGE,bg="light blue")
        button_frame.place(x=0,y=200,width=635,height=120)
        # Save Button
        save_button = Button(button_frame,text="Import csv",command=self.importCSV,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0,padx=2,pady=20)
        # Update Button
        update_button = Button(button_frame,text="Export csv",command=self.exportCSV,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1,padx=2,pady=20)
        # Delete Button
        delete_button = Button(button_frame,text="Update",command=self.update,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2,padx=2,pady=20)
        # Reset Button
        reset_button = Button(button_frame,text="Reset",command=self.reset,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3,padx=2,pady=20)
        # Exit Button
        exit_button = Button(button_frame,text="Exit",command=self.exit,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        exit_button.grid(row=1,column=0,padx=2,pady=2)
        # ============================= Table Frame ==========================================
        
    
        
        
        
        
        


         # ================================================ right  Frame ================================================
        right_frame = LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,
        "bold"))
        right_frame.place(x=675,y=1,width=650,height=490)

        button_frame = Frame(right_frame,relief=RIDGE,bd=2,bg="white")
        button_frame.place(x=5,y=5,width=635,height=458)

        # ===================================== Scroolbar table =============================================
        scoll_x = ttk.Scrollbar(button_frame,orient=HORIZONTAL)
        scoll_y = ttk.Scrollbar(button_frame,orient=VERTICAL)

        self.AttendanceReport_table = ttk.Treeview(button_frame,columns=("ID","Name","ROLL","Department","Time","Date","Attendance"),xscrollcommand=scoll_x.set,yscrollcommand=scoll_y.set)
        scoll_x.pack(side=BOTTOM,fill=X)
        scoll_y.pack(side=RIGHT,fill=Y)

        scoll_x.config(command=self.AttendanceReport_table.xview)
        scoll_y.config(command=self.AttendanceReport_table.yview)

        self.AttendanceReport_table.heading("ID",text="Attendance ID")
        self.AttendanceReport_table.heading("Name",text="Name")
        self.AttendanceReport_table.heading("ROLL",text="ROLL")
        self.AttendanceReport_table.heading("Department",text="Department")
        self.AttendanceReport_table.heading("Time",text="Time")
        self.AttendanceReport_table.heading("Date",text="Date")
        self.AttendanceReport_table.heading("Attendance",text="Attendance")

        self.AttendanceReport_table["show"]="headings"
        self.AttendanceReport_table.column("ID",width=100)
        self.AttendanceReport_table.column("Name",width=100)
        self.AttendanceReport_table.column("ROLL",width=100)
        self.AttendanceReport_table.column("Department",width=100)
        self.AttendanceReport_table.column("Time",width=100)
        self.AttendanceReport_table.column("Date",width=100)
        self.AttendanceReport_table.column("Attendance",width=100)



        self.AttendanceReport_table.pack(fill=BOTH,expand=1)

        self.AttendanceReport_table.bind("<ButtonRelease-1>",self.get_cursor)
        

        # ================================== Fetch Data ===================================
    def fatchData(self,rows):
        self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
        for i in rows:
            self.AttendanceReport_table.insert("",END,values=i)
    # import CSV
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fatchData(mydata)

    # export CSV
    def exportCSV(self):
        global mydata
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                csvwrite = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    csvwrite.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported  To "+os.path.basename(fln)+" Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To : {str(es)}")
        # update function
    # get cursor
    

    def update(self):
        selected_item = self.AttendanceReport_table.focus()
        if not selected_item:
            messagebox.showerror("Error", "No item selected to update",parent=self.root)
            return

        values = self.AttendanceReport_table.item(selected_item, "values")
        if not values:
            messagebox.showerror("Error", "Selected item has no values",parent=self.root)
            return

        # Get updated values from the entry fields
        updated_values = (
            values[0],  # Attendance ID (unchanged)
            values[1],  # Name (unchanged)
            values[2],  # Roll No (unchanged)
            values[3],  # Department (unchanged)
            values[4],  # Time (unchanged)
            values[5],  # Date (unchanged)
            self.attendance_status_combo.get()  # Updated Attendance Status
        )

        # Update the selected item in the Treeview
        self.AttendanceReport_table.item(selected_item, values=updated_values)
        messagebox.showinfo("Success", "Attendance record updated successfully",parent=self.root)
        
            
    # reset function
    def reset(self):        
        self.attendance_id.set("")
        self.student_name.set("")
        self.roll_no.set("")
        self.department.set("")
        self.time.set("")
        self.date.set("")
        self.attendance_status.set("Status")

        messagebox.showinfo("Reset", "All fields and data have been reset successfully",parent=self.root)

    # exit function
    def exit(self):
        confirm_exit = messagebox.askyesno("Exit", "Are you sure you want to exit?",parent=self.root)
        if confirm_exit:
            self.root.destroy()
        exit()

    def get_cursor(self, event=""):
        # Get the selected row in the Treeview
        cursor_row = self.AttendanceReport_table.focus()
        contents = self.AttendanceReport_table.item(cursor_row)
        row = contents['values']

        # Populate the entry fields with the selected row's data
        self.attendance_id.set(row[0])
        self.student_name.set(row[1])
        self.roll_no.set(row[2])
        self.department.set(row[3])
        self.time.set(row[4])
        self.date.set(row[5])
        self.attendance_status.set(row[6])

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()