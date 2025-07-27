import tkinter as tk
from tkinter import ttk, scrolledtext, PhotoImage
from PIL import Image, ImageTk
import random

class HelpDeskChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Help Desk AI Chatbot")
        self.root.geometry("1200x600+0+0")
        self.root.resizable(False, False)
        
        # Theme (Dark/Light)
        self.theme_mode = "light"
        self.bg_color = "#f5f5f5"
        self.card_color = "#ffffff"
        self.text_color = "#333333"
        self.accent_color = "#4e73df"
        
        # Load icons (replace with your own paths)
        try:
            self.logo_img = ImageTk.PhotoImage(Image.open("logo.png").resize((40, 40)))
        except:
            self.logo_img = None
        
        # Main container
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.header_frame = tk.Frame(self.main_frame, bg=self.accent_color, height=60)
        self.header_frame.pack(fill=tk.X)
        
        # Logo & Title
        if self.logo_img:
            logo_label = tk.Label(self.header_frame, image=self.logo_img, bg=self.accent_color)
            logo_label.pack(side=tk.LEFT, padx=10)
        
        title_label = tk.Label(
            self.header_frame, 
            text="Help Desk AI Assistant", 
            font=("Helvetica", 16, "bold"), 
            fg="white", 
            bg=self.accent_color
        )
        title_label.pack(side=tk.LEFT, padx=10)
        
        # Theme Toggle
        self.theme_btn = tk.Button(
            self.header_frame, 
            text="🌙 Dark Mode", 
            font=("Helvetica", 10), 
            bg=self.accent_color, 
            fg="white", 
            bd=0,
            command=self.toggle_theme
        )
        self.theme_btn.pack(side=tk.RIGHT, padx=20)
        
        # Main Content (Split into Chat & Sidebar)
        self.content_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Chat Area (Left)
        self.chat_frame = tk.Frame(self.content_frame, bg=self.card_color, bd=2, relief=tk.RAISED)
        self.chat_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Chat Display (ScrolledText)
        self.chat_display = scrolledtext.ScrolledText(
            self.chat_frame, 
            wrap=tk.WORD, 
            width=60, 
            height=20, 
            font=("Helvetica", 11), 
            bg=self.card_color, 
            fg=self.text_color,
            padx=10,
            pady=10,
            bd=0
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        self.chat_display.insert(tk.END, "🤖 AI: Hello! How can I assist you today?\n")
        self.chat_display.config(state=tk.DISABLED)
        
        # User Input
        self.input_frame = tk.Frame(self.chat_frame, bg=self.card_color)
        self.input_frame.pack(fill=tk.X, pady=(0, 10), padx=10)
        
        self.user_input = tk.Entry(
            self.input_frame, 
            font=("Helvetica", 12), 
            bg="#f9f9f9", 
            fg=self.text_color, 
            bd=1, 
            relief=tk.SOLID
        )
        self.user_input.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=(0, 5))
        self.user_input.bind("<Return>", self.send_message)
        
        self.send_btn = tk.Button(
            self.input_frame, 
            text="Send", 
            font=("Helvetica", 10, "bold"), 
            bg=self.accent_color, 
            fg="white", 
            command=self.send_message
        )
        self.send_btn.pack(side=tk.RIGHT)
        
        # Sidebar (Right)
        self.sidebar_frame = tk.Frame(self.content_frame, bg=self.card_color, width=250, bd=2, relief=tk.RAISED)
        self.sidebar_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Sidebar Tabs
        self.sidebar_tabs = ttk.Notebook(self.sidebar_frame)
        self.sidebar_tabs.pack(fill=tk.BOTH, expand=True)
        
        # FAQ Tab
        self.faq_tab = tk.Frame(self.sidebar_tabs, bg=self.card_color)
        self.sidebar_tabs.add(self.faq_tab, text="📚 FAQ")
        
        faq_questions = [
            "How do I reset my password?",
            "Where can I download software?",
            "How to submit a support ticket?",
            "What are your business hours?",
            "How to contact IT support?"
        ]
        
        for q in faq_questions:
            faq_btn = tk.Button(
                self.faq_tab, 
                text=q, 
                font=("Helvetica", 10), 
                bg="#f0f0f0", 
                fg=self.text_color, 
                bd=1, 
                relief=tk.RAISED,
                command=lambda q=q: self.insert_faq_response(q)
            )
            faq_btn.pack(fill=tk.X, pady=2, padx=5)
        
        # Tickets Tab
        self.tickets_tab = tk.Frame(self.sidebar_tabs, bg=self.card_color)
        self.sidebar_tabs.add(self.tickets_tab, text="🎫 Tickets")
        
        ticket_list = tk.Listbox(
            self.tickets_tab, 
            bg="#f9f9f9", 
            fg=self.text_color, 
            font=("Helvetica", 10), 
            bd=0
        )
        ticket_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        sample_tickets = [
            "Ticket #001 - Login Issues (Open)",
            "Ticket #002 - Software Error (In Progress)",
            "Ticket #003 - Hardware Request (Closed)"
        ]
        
        for ticket in sample_tickets:
            ticket_list.insert(tk.END, ticket)
        
        # Footer
        self.footer_frame = tk.Frame(self.main_frame, bg=self.accent_color, height=30)
        self.footer_frame.pack(fill=tk.X)
        
        footer_label = tk.Label(
            self.footer_frame, 
            text="© 2024 Help Desk AI Assistant | Powered by Python & Tkinter", 
            font=("Helvetica", 9), 
            fg="white", 
            bg=self.accent_color
        )
        footer_label.pack(pady=5)
    
    def toggle_theme(self):
        if self.theme_mode == "light":
            self.theme_mode = "dark"
            self.bg_color = "#2d2d2d"
            self.card_color = "#3d3d3d"
            self.text_color = "#ffffff"
            self.theme_btn.config(text="☀️ Light Mode")
        else:
            self.theme_mode = "light"
            self.bg_color = "#f5f5f5"
            self.card_color = "#ffffff"
            self.text_color = "#333333"
            self.theme_btn.config(text="🌙 Dark Mode")
        
        self.update_theme()
    
    def update_theme(self):
        self.main_frame.config(bg=self.bg_color)
        self.header_frame.config(bg=self.accent_color)
        self.content_frame.config(bg=self.bg_color)
        self.chat_frame.config(bg=self.card_color)
        self.chat_display.config(bg=self.card_color, fg=self.text_color)
        self.input_frame.config(bg=self.card_color)
        self.user_input.config(bg="#f9f9f9" if self.theme_mode == "light" else "#444444", fg=self.text_color)
        self.sidebar_frame.config(bg=self.card_color)
        self.faq_tab.config(bg=self.card_color)
        self.tickets_tab.config(bg=self.card_color)
        self.footer_frame.config(bg=self.accent_color)
    
    def send_message(self, event=None):
        user_msg = self.user_input.get()
        if not user_msg.strip():
            return
        
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"👤 You: {user_msg}\n")
        
        # Simulate AI response
        ai_responses = [
            "I can help with that. Please check the FAQ section for quick answers.",
            "Let me look that up for you. One moment...",
            "For this issue, you might want to submit a support ticket.",
            "I recommend contacting IT support for further assistance.",
            "Here’s a solution I found..."
        ]
        ai_response = random.choice(ai_responses)
        self.chat_display.insert(tk.END, f"🤖 AI: {ai_response}\n")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
        self.user_input.delete(0, tk.END)
    
    def insert_faq_response(self, question):
        faq_answers = {
            "How do I reset my password?": "Go to Settings > Security > Reset Password.",
            "Where can I download software?": "Visit our Downloads portal at support.example.com/downloads.",
            "How to submit a support ticket?": "Click 'Tickets' in the sidebar and fill out the form.",
            "What are your business hours?": "Our support team is available Mon-Fri, 9 AM - 5 PM.",
            "How to contact IT support?": "Call +91 9759029731 or email ravindra975902@gmail.com."
        }
        
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"📚 FAQ: {question}\n🤖 AI: {faq_answers[question]}\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = HelpDeskChatbot(root)
    root.mainloop()