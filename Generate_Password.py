import string as s
import random

class Password:
    # Class Variables
    passwordCnt = 0 # Number of Passwords generated
    passwords = [] # List of passwords
    
    def __init__(self, length) -> None:
        """
        Create Password Class

        Args:
            length (integer): Get Password length
        """
        # Store password variables
        passwordChar = list(s.ascii_letters + s.digits + s.punctuation) # Store characters
        self.passLength = length # Store password length
        self.newPassword = ''.join(random.sample(passwordChar, length)) # Join characters for new password
        
        # While loop checks all password characters to match for upper, lower, digit, 
        # and punctuation characters
        while(True): 
            if (any(char.isupper() for char in self.newPassword) and
                any(char.islower() for char in self.newPassword) and
                sum(char.isdigit() for char in self.newPassword) >= 3 and
                sum(char in list(s.punctuation) for char in self.newPassword) >= 2):
                break # Break loop when True
            # Else generate new password and check if matches
            else: 
                self.newPassword = ''.join(random.sample(passwordChar, length))
        
        Password.passwords.append(self.newPassword) # Append to password list
        Password.passwordCnt += 1 # Add to class variable


    def displayNewPassword(self):
        """
        Print new password to user
        """
        print(self.newPassword)

    def getNewPassword(self):
        """
        Return New password

        Returns:
            String: New password string
        """
        return self.newPassword

    @classmethod
    def passwordNames(cls):
        """
        Prints list of passwords
        """
        print("List of passwords:")
        for x in cls.passwords: # Loop through list of password 
            print(f"\t{cls.passwords.index(x)+1}| " + x) # Print number and password

    @classmethod
    def numOfPassword(cls):
        """
        Print number of passwords created
        """
        print("Number of Passwords generated:", cls.passwordCnt)