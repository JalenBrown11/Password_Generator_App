import tkinter as tk
import clipboard
from tkinter import ttk
from tkinter import *
from Generate_Password import Password

class App(tk.Tk):
    # Class Variable
    passwordLength = int # Store password length
    def __init__(self):
        """
        Create Password_Gui class
        """
        super().__init__(className=" Password Generator") # Initialize Window

        # Constant Variables
        WIDTH = self.winfo_screenwidth() // 2 # Window width
        HEIGHT = self.winfo_screenheight() // 3 # Window height
        COLUMNS, ROWS = 3, 2 # Num of Column and Rows in Window

        # Text variables
        self.setPassword = tk.StringVar() # New Password text
        self.setMessage = tk.StringVar() # Output Message text
        self.setMessage.set('[Enter Input Here]') # Set Default Message (In case no input)
        
        # Configure App Window
        self.geometry(f'{WIDTH}x{HEIGHT}') # Default Window size 
        self.configure(padx=10, pady=10, background='#232429') # Window border and background color
        self.resizable(False, False) # Disable Window resize
        
        # Window Placement Grid
        for cols in range(COLUMNS):
            self.columnconfigure(cols, weight=1, minsize=50)
        for rows in range(ROWS):
            self.rowconfigure(rows,weight=1, minsize=50)

        # Creates and stores window components and handles events
        self.create_frames(COLUMNS,ROWS)
        self.create_widgets()
        self.configure_widgets()
        self.event_handler()

    """ Handle keyboard/widgets events """
    def event_handler(self):
        """
        Event Handler for both keyboard & widget events
        """
        self.bind('<Escape>', lambda Destroy: self.quit()) # Close App (Escape key)

        self.bind('<Return>', lambda FocusIn: self.generateButton.focus()) # Focus on generate button (Enter key)
        self.generateButton.bind('<Return>', self.generate_password) # Create new password (Enter key x2)

        self.bind('<Control-KeyPress-c>', lambda event: self.copyButton.focus()) # Focus on copy button (Control-C key)
        self.copyButton.bind('<Control-KeyPress-c>', self.copy_password) # Copy password (Control-C key x2)
    
    def update_length(self, event):
        """
        Update Password Length

        Args:
            event (Event): Receives Slider input
        """
        self.passwordLength = self.lengthSlider.get() # Store Slider Value in password length
        self.setMessage.set(f"Password Length is {self.passwordLength}") # Set label text to output message

    """ Generate New Password"""
    def generate_password(self, event):
        """
        Generate New Password and Outputs Event Message

        Args:
            event (Event): Receives KeyPress input
        """
        generate = Password(self.passwordLength) # Generate password from length
        self.setPassword.set(generate.getNewPassword()) # Set label text to password
        self.setMessage.set('New Password Generated!') # Set label text to output message

    def copy_password(self, event):
        """
        Copies Password and Outputs Event Message 

        Args:
            event (Event): Receives KeyPress input
        """
        clipboard.copy(self.setPassword.get()) # Copies password
        self.setMessage.set('Copied Password!') # Set label text to output message
    
    def create_frames(self, cols, rows):
        """
        Create Frames in App

        Args:
            cols (integer): Number of columns
            rows (integer): Number of rows
        """
        # Title Frame
        self.titleFrame = tk.Frame(self, background='#38373D')
        self.titleFrame.grid(column=0,row=0, pady=5, columnspan=cols, sticky='nesw')

        # Left Frame
        self.LFrame = tk.Frame(self, background='#38373D')
        for irows in range(rows):
            self.LFrame.rowconfigure(irows, weight=1, minsize=30)
        self.LFrame.grid(column=0,row=1, sticky='nesw')

        # Middle Frame
        self.MFrame = tk.Frame(self, background='#38373D')
        for irows in range(rows):
            self.MFrame.rowconfigure(irows,weight=1, minsize=30)
        self.MFrame.grid(column=1, row=1, sticky='nesw')

        # Right Frame
        self.RFrame = tk.Frame(self, background='#38373D')
        for irows in range(rows):
            self.RFrame.rowconfigure(irows, weight=1, minsize=30)
        self.RFrame.grid(column=2,row=1, sticky='nesw')

        # Bottom Frame
        self.BFrame = tk.Frame(self, background='#38373D')
        self.BFrame.rowconfigure(0, weight=1, minsize=50)
        self.BFrame.grid(column=0, row=2, pady=5, columnspan=cols, sticky='nesw')
        
    def create_widgets(self):
        """
        Create and Sort Widgets in App
        """
        # Title Frame Label
        titleLabel = ttk.Label(self.titleFrame, style='Top.TLabel', 
            text="Password Generator (esc to exit)").pack()

        # Left Frame Labels
        passwordLengthPrompt = ttk.Label(self.LFrame, style='Left.TLabel',
            text='Choose Length of Password:').grid(row=0, sticky='nesw')

        newPasswordPrompt = ttk.Label(self.LFrame, style='Left.TLabel',
            text='New Password:').grid(row=1, sticky='nesw')

        # Middle Frame Label
        self.outputPassword = ttk.Label(self.MFrame, style='Middle.TLabel',
            textvariable=self.setPassword).grid(row=1, sticky='ew')

        # Bottom Frame Label
        self.userMessage = ttk.Label(self.BFrame, style='Bottom.TLabel',
            textvariable=self.setMessage).grid(row=0, sticky='ew')

        # Middle Frame Slider
        self.lengthSlider = Scale(self.MFrame, command=self.update_length)
        self.lengthSlider.set(20)
        self.lengthSlider.grid(row=0, padx=5, pady=5, sticky='nesw')

        # Right Frame Buttons
        self.generateButton = ttk.Button(self.RFrame, text='Generate',
            command= lambda: self.generate_password('<Button>'))
        self.generateButton.grid(row=0, sticky='ew') # Generate password

        self.copyButton = ttk.Button(self.RFrame, text='Copy',
            command= lambda: self.copy_password('<Button>'))
        self.copyButton.grid(row=1, sticky='ew') # Copy password
    
    def configure_widgets(self):
        """
        Configure the Style of Widgets
        """
        # Create Style class
        style = ttk.Style()

        # Top Label Configuration
        style.configure('Top.TLabel', font=("Montserrat",12),
            foreground='#B2AFC2', background='#38373D',
            padding='10 10 10 10')

        # Left Label Configuration
        style.configure('Left.TLabel', font=("Montserrat",10),
            foreground='#B2AFC2', background='#38373D')
        
        # Middle Label Configuration
        style.configure('Middle.TLabel', font=("Montserrat",10),
            foreground='#504E57', anchor=tk.CENTER)
        
        # Middle Slider Configuration
        self.lengthSlider.configure(orient=HORIZONTAL,
            from_=12, to=26, tickinterval=4, resolution=4,
            showvalue=0, length=200, fg='#918F9E', bg='#38373D',
            activebackground='#504E57', highlightthickness=0, 
            troughcolor='white', sliderrelief='flat', bd=2)
        
        # Bottom Label Configuration
        style.configure('Bottom.TLabel', font=("Montserrat",10),
            foreground='#B2AFC2', background='#38373D', padding='10 0 0 0',
            anchor=tk.CENTER)

        # Bottom Label Configuration
        style.configure('TButton', font=("Montserrat",10))
