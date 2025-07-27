import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk
import webbrowser
import os

def open_email():
    webbrowser.open("mailto:raindra975902@gmail.com")

def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/ravindra97/")

def open_github():
    webbrowser.open("https://github.com/dashboard")

def create_developer_page(parent=None):
    if parent is None:
        root = tk.Tk()
    else:
        root = parent
    root.title("Face Recognition System - Developer Profile")
    root.geometry("1200x600+0+0")
    root.resizable(False, False)
    
    # Set a modern theme
    style = ttk.Style()
    style.theme_use('clam')
    
    # Configure colors
    bg_color = "#f0f2f5"
    card_color = "#ffffff"
    accent_color = "#4e73df"
    text_color = "#5a5c69"
    
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=text_color)
    style.configure('Card.TFrame', background=card_color, relief=tk.RAISED, borderwidth=1)
    style.configure('Title.TLabel', font=('Helvetica', 20, 'bold'), foreground=accent_color)
    style.configure('Section.TLabel', font=('Helvetica', 14, 'bold'), foreground=accent_color)
    style.configure('Link.TButton', foreground=accent_color, font=('Helvetica', 10, 'underline'), 
                   background=card_color, borderwidth=0)
    
    # Main container with background
    main_container = tk.Frame(root, bg=bg_color)
    main_container.pack(fill=tk.BOTH, expand=True)

    # Background image
    try:
        bg_image = Image.open("Images/developer_background.webp")  # Replace with your background image path
        bg_image = bg_image.resize((1200, 650), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(main_container, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, width=1200, height=650)
    except Exception as e:
        # Fallback if background image not found
        main_container.config(bg=bg_color)
    
    # Content card
    card = ttk.Frame(main_container, style='Card.TFrame', padding=(30, 20))
    card.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=800, height=500)
    
    # Header
    header_frame = ttk.Frame(card)
    header_frame.pack(fill=tk.X, pady=(0, 20))
    
    ttk.Label(header_frame, text="Face Recognition System Developer", style='Title.TLabel').pack()
    
    # Main content
    content_frame = ttk.Frame(card)
    content_frame.pack(fill=tk.BOTH, expand=True)
    
    # Left column - Developer photo and info
    left_frame = ttk.Frame(content_frame, width=250)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)
    
    # Developer photo
    try:
        dev_image = Image.open("Images/ravindra.jpg")  # Replace with developer photo path
        dev_image = dev_image.resize((200, 200), Image.LANCZOS)
        dev_photo = ImageTk.PhotoImage(dev_image)
        photo_label = ttk.Label(left_frame, image=dev_photo, background=card_color)
        photo_label.image = dev_photo
        photo_label.pack(pady=(0, 20))
    except:
        # Placeholder if photo not found
        photo_placeholder = ttk.Frame(left_frame, width=200, height=200, relief=tk.SOLID, 
                                    style='Card.TFrame')
        photo_placeholder.pack_propagate(False)
        photo_placeholder.pack(pady=(0, 20))
        ttk.Label(photo_placeholder, text="Developer Photo", foreground='gray', 
                 background=card_color).pack(expand=True)
    
    # Developer info
    info_frame = ttk.Frame(left_frame, style='Card.TFrame', padding=10)
    info_frame.pack(fill=tk.X)
    
    ttk.Label(info_frame, text="Ravindra Singh", font=('Helvetica', 14, 'bold'), 
             background=card_color).pack(anchor=tk.W)
    ttk.Label(info_frame, text="Python Developer", foreground='gray', 
             background=card_color).pack(anchor=tk.W)
    
    ttk.Label(info_frame, text="Contact:", font=('Helvetica', 10, 'bold'), 
             background=card_color).pack(anchor=tk.W, pady=(10, 0))
    
    # Email button
    email_frame = ttk.Frame(info_frame, style='Card.TFrame')
    email_frame.pack(fill=tk.X, pady=1)
    ttk.Button(email_frame, text="raindra975902@gmail.com", style='Link.TButton', 
              command=open_email).pack(side=tk.LEFT)
    
    # LinkedIn button
    linkedin_frame = ttk.Frame(info_frame, style='Card.TFrame')
    linkedin_frame.pack(fill=tk.X, pady=1)
    ttk.Button(linkedin_frame, text="LinkedIn", style='Link.TButton', 
              command=open_linkedin).pack(side=tk.LEFT)
    
    # GitHub button
    github_frame = ttk.Frame(info_frame, style='Card.TFrame')
    github_frame.pack(fill=tk.X, pady=1)
    ttk.Button(github_frame, text="GitHub", style='Link.TButton', 
              command=open_github).pack(side=tk.LEFT)
    
    # Right column - About sections
    right_frame = ttk.Frame(content_frame)
    right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0))
    
    # About the Developer
    about_dev_frame = ttk.Frame(right_frame, style='Card.TFrame', padding=15)
    about_dev_frame.pack(fill=tk.X, pady=(0, 20))
    
    ttk.Label(about_dev_frame, text="About the Developer", style='Section.TLabel', 
             background=card_color).pack(anchor=tk.W)
    
    about_text = ("Results-driven Python Developer with 1+ years of experience specializing in machine learning and artificial intelligence solutions. Proven track record of designing, developing, and deploying scalable ML systems across computer vision, natural language processing, and predictive analytics domains. Passionate about transforming complex business problems into AI-powered solutions with measurable impact")
    
    ttk.Label(about_dev_frame, text=about_text, wraplength=450, justify=tk.LEFT, 
             background=card_color).pack(anchor=tk.W)
    
    # About the Face Recognition System
    about_system_frame = ttk.Frame(right_frame, style='Card.TFrame', padding=15)
    about_system_frame.pack(fill=tk.X)
    
    ttk.Label(about_system_frame, text="About the Face Recognition System", 
             style='Section.TLabel', background=card_color).pack(anchor=tk.W)
    
    system_text = ("This advanced face recognition system utilizes state-of-the-art deep learning "
                  "algorithms to accurately detect and recognize faces in real-time. Key features include:\n\n"
                  "- Real-time face detection and recognition\n"
                  "- Support for multiple faces in a single frame\n"
                  "- High accuracy even with varying lighting conditions\n"
                  "- Database integration for user management\n"
                  "- Customizable confidence thresholds\n\n"
                  "Built with Python, OpenCV, and TensorFlow, the system can be deployed "
                  "for security, attendance tracking, or personalized user experiences.")
    
    ttk.Label(about_system_frame, text=system_text, wraplength=450, justify=tk.LEFT, 
             background=card_color).pack(anchor=tk.W)
    
    # Footer
    footer_frame = ttk.Frame(card)
    footer_frame.pack(fill=tk.X, pady=(20, 0))
    
    ttk.Label(footer_frame, text="© 2023 Ravindra Singh - Face Recognition System", 
             foreground='gray', background=card_color).pack(side=tk.RIGHT)
    
    root.mainloop() if parent is None else None

if __name__ == "__main__":
    create_developer_page()