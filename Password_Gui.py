import tkinter as tk
import sys
import clipboard
from tkinter import ttk
from tkinter import *
from Generate_Password import Password


class App(tk.Tk):
    # Class Variable
    passwordLength = int  # Store password length

    def __init__(self):
        """
        Create Password_Gui class
        """
        super().__init__(className=" Password Generator")  # Initialize Window

        # Text variables
        self.setPassword = tk.StringVar() # Password text
        self.sliderValue = tk.IntVar(value=20) # Slider value
        self.setMessage = tk.StringVar()  # Output Message text
        
        # Set Default Message (In case no input)
        self.setMessage.set('Generate Password Here')

        # Configure App Window
        self.configure(padx=10, pady=10, background='#232429')
        self.resizable(False, False) # Disable Window resize

        # Creates and stores window components and handles events
        self.create_frames()
        self.create_widgets()
        self.configure_widgets()
        self.event_handler()

    """ Handle keyboard/widgets events """

    def event_handler(self):
        """
        Event Handler for both keyboard & widget events
        """
        # Close app shortcut (Escape key)
        self.bind('<Escape>', sys.exit)

        # Generate password shortcut (Enter key)
        self.bind('<Return>', self.generate_password)

        # Copy shortcut (Control-C key)
        self.bind('<Control-KeyPress-c>', self.copy_password)
        
        # Increment slider shortcut (Right arrow)
        self.bind('<Right>', self.update_slider_value)
        # Decrement slider shortcut (Left arrow)
        self.bind('<Left>', self.update_slider_value)

        # self.bind('<Key>', self.key_pressed) Debug user input
    
    def key_pressed(self, event):
        """
        Prints User Input for Debugging

        Args:
            event (Event): Receives user input
        """
        print(event) 
        
    def update_slider_value(self, event):
        """
        Update Slider's Integer Variable

        Args:
            event (Event): Receive user input
        """
        # Handle KeyPress events
        if event.keysym == 'Right': # Right arrow key
            if self.sliderValue.get() != 28:
                self.sliderValue.set(self.sliderValue.get() + 4)# Increase slider
                
        if event.keysym == 'Left': # Left arrow key
            if self.sliderValue.get() != 12:
                self.sliderValue.set(self.sliderValue.get() - 4) # Decrease slider
        
        self.update_pass_length() # Update password length message
        
    
    def update_pass_length(self):
        """
        Update Password Length Message 

        Args:
            event (Event): Receives Slider input and User input
        """                  
        # Set label text to output message
        self.setMessage.set(f"Password Length is {self.sliderValue.get()}")

    """ Generate New Password"""

    def generate_password(self, event):
        """
        Generate New Password and Outputs Event Message

        Args:
            event (Event): Receives KeyPress input
        """
        self.generateButton.focus()
        generate = Password(self.sliderValue.get())  # Generate password from length
        # Set label text to password
        self.setPassword.set(generate.getNewPassword())
        # Set label text to output message
        self.setMessage.set('New Password Generated!')

    def copy_password(self, event):
        """
        Copies Password and Outputs Event Message 

        Args:
            event (Event): Receives KeyPress input
        """
        self.copyButton.focus()
        clipboard.copy(self.setPassword.get())  # Copies password
        # Set label text to output message
        self.setMessage.set('Copied Password!')

####################################################################################################
    def create_frames(self):
        """
        Create Frames
        """
        # Title Frame
        self.TFrame = tk.Frame(self, background='#232429')
        self.TFrame.grid(row=0, column=0)
        
        # Middle Frame
        self.MFrame = tk.Frame(self, background='#232429')
        self.MFrame.grid(row=1, column=0)
        
        # Bottom Frame
        self.BFrame = tk.Frame(self, background='#232429')
        self.BFrame.grid(row=2, column=0)
        
        # Right Frame
        self.RFrame = tk.Frame(self, background='#3d3e42')
        self.RFrame.grid(row=0, rowspan=3, column=1, sticky=NSEW, padx=8, pady=0)
#######################################################################################################

    def create_widgets(self):
        """
        Create and Sort Widgets
        """
        # Title Frame Label
        titleLabel = ttk.Label(
            self.TFrame,
            style='Top.TLabel',
            text="<< Password Generator >>")
        titleLabel.pack(pady=16)

        # Left Frame Labels
        passwordLengthPrompt = ttk.Label(
            self.MFrame,
            style='Left.TLabel',
            text='Choose Length of Password:')
        passwordLengthPrompt.grid(row=1, column=0, sticky=NSEW)

        newPasswordPrompt = ttk.Label(
            self.MFrame,
            style='Left.TLabel',
            text='New Password:')
        newPasswordPrompt.grid(row=2, column=0, sticky=NSEW)

        # Middle Frame Label
        self.outputPassword = ttk.Label(
            self.MFrame,
            style='Middle.TLabel',
            textvariable=self.setPassword)
        self.outputPassword.grid(row=2, column=1, sticky=NSEW, padx=16, pady=8)

        # Middle Frame Slider
        self.lengthSlider = Scale(
            self.MFrame, 
            variable=self.sliderValue,
            command=self.update_pass_length)
        self.lengthSlider.grid(row=1, column=1, sticky=NSEW, padx=16, pady=8)

        # Middle Frame Buttons
        self.generateButton = ttk.Button(
            self.MFrame,
            text='Generate',
            command=lambda: self.generate_password('<Button>'))
        self.generateButton.grid(row=1, column=2, sticky=EW, pady=8)  # Generate password

        self.copyButton = ttk.Button(
            self.MFrame,
            text='Copy',
            command=lambda: self.copy_password('<Button>'))
        self.copyButton.grid(row=2, column=2, sticky=EW, pady=8)  # Copy password

        # Right Frame Labels
        ttk.Label(self.RFrame, style='Right.TLabel', text='Close App [Escape]').pack()
        ttk.Label(self.RFrame, style='Right.TLabel', text='Generate password [Enter]').pack()
        ttk.Label(self.RFrame, style='Right.TLabel', text='Copy password [Control-C]').pack()
        ttk.Label(self.RFrame, style='Right.TLabel', text='Increment slider [Right arrow]').pack()
        ttk.Label(self.RFrame, style='Right.TLabel', text='Decrement slider [Left arrow]').pack()
        
        # Bottom Frame Label
        self.userMessage = ttk.Label(
            self.BFrame,
            style='Bottom.TLabel',
            textvariable=self.setMessage)
        self.userMessage.pack(pady=16)

    def configure_widgets(self):
        """
        Configure the Style of Widgets
        """
        # Create Style class
        style = ttk.Style()

        # Top Label Configuration
        style.configure('Top.TLabel', font=("Montserrat", 16),
                        foreground='white', background='#232429',
                        padding='10 10 10 10')

        # Left Label Configuration
        style.configure('Left.TLabel', font=("Montserrat", 10),
                        foreground='white', background='#232429')

        # Middle Label Configuration
        style.configure('Middle.TLabel', font=("Montserrat", 10),
                        foreground='white', background='#3d3e42',
                        padding=4, anchor=tk.CENTER)

        # Middle Slider Configuration
        self.lengthSlider.configure(orient=HORIZONTAL,
                                    from_=12, to=26, tickinterval=4, resolution=4,
                                    showvalue=0, length=200, fg='white', bg='#232429',
                                    activebackground='#3d3e42', highlightthickness=0,
                                    troughcolor='white', sliderrelief='flat', bd=2)

        # Bottom Label Configuration
        style.configure('Bottom.TLabel', font=("Montserrat", 12),
                        foreground='white', background='#232429', padding='10 0 0 0',
                        anchor=tk.CENTER)

        # Bottom Label Configuration
        style.configure('TButton', font=("Montserrat", 10))
        
        style.configure('Right.TLabel', font=("Montserrat", 10),
                        foreground='white', background='#3d3e42',
                        anchor=tk.LEFT, padding=12)
