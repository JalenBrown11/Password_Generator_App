import Password_Gui

""" Password Generator App

    Handles generating password of varies user-defined lengths and 
    allows users to copy each password for individual purposes.  
"""

def runApp():
    """
    Runs Password_Gui App
    """
    if __name__ == '__main__':
        app = Password_Gui.App()
        app.mainloop()

runApp()