from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1400x650+0+0")

        # Background Image (resize to window size)
        bg_img = Image.open(r"Images\login.png")
        bg_img = bg_img.resize((1000, 600), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_img)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=-200, y=0, width=1300, height=700)

        # Login Frame
        frame = Frame(self.root, bg="white", highlightbackground="white", highlightthickness=1)
        frame.place(x=840, y=80, width=400, height=450)
        frame.tkraise()  # Ensure the frame is above the background

        

        # Title
        title = Label(frame, text="Login Here", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title.place(x=100, y=30)

        # Circular Image
        img = Image.open(r"Images\login_l.jpg")  # Replace with your image path
        img = img.resize((100, 100), Image.Resampling.LANCZOS)

        # Create a circular mask
        mask = Image.new("L", (100, 100), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 100, 100), fill=255)

        # Apply the mask to the image
        circular_img = Image.composite(img, Image.new("RGB", img.size, (255, 255, 255)), mask)
        self.photoimg = ImageTk.PhotoImage(circular_img)

        # Add the circular image to the frame
        img_label = Label(frame, image=self.photoimg, bg="white")
        img_label.place(x=150, y=80, width=100, height=100)

        # Username Label and Entry
        username_label = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="black")
        username_label.place(x=50, y=200)
        self.txt_user = Entry(frame, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=50, y=230, width=300)

        # Password Label and Entry
        password_label = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        password_label.place(x=50, y=270)
        self.txt_pass = Entry(frame, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass.place(x=50, y=300, width=300)

        # Login Button
        login_btn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bg="blue", fg="white", cursor="hand2")
        login_btn.place(x=50, y=375, width=100, height=40)

        # Register Button
        register_btn = Button(frame, text="Create Account", command=self.register_window, font=("times new roman", 15, "bold"), bg="green", fg="white", cursor="hand2")
        register_btn.place(x=230, y=375)

        # Forgot Password Button
        forgot_btn = Button(frame, text="Forgot Password?", command=self.forgot_password_window, font=("times new roman", 12, "bold"), bg="white", fg="red", bd=0, cursor="hand2")
        forgot_btn.place(x=230, y=330)
        

    def login(self):
        # Predefined username and password
        username = "admin"
        password = "Face@"

        # Get user input
        entered_username = self.txt_user.get()
        entered_password = self.txt_pass.get()

        # Authentication
        if entered_username == username and entered_password == password:
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def register_window(self):
        # Open a new window for registration
        register_win = Toplevel(self.root)
        register_win.title("Register")
        register_win.geometry("400x400+600+200")
        Label(register_win, text="Register Here", font=("times new roman", 20, "bold")).pack(pady=20)
        # Add registration fields here (e.g., username, password, email, etc.)
        Label(register_win, text="Registration functionality to be implemented").pack()

    def forgot_password_window(self):
        # Open a new window for password recovery
        forgot_win = Toplevel(self.root)
        forgot_win.title("Forgot Password")
        forgot_win.geometry("400x300+600+250")
        Label(forgot_win, text="Recover Password", font=("times new roman", 20, "bold")).pack(pady=20)
        # Add password recovery fields here (e.g., email, security question, etc.)
        Label(forgot_win, text="Password recovery functionality to be implemented").pack()
        

if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()