import re
class Validator:


    def passwordValidator(self, password):
        """
        Declare Min & Max Length of Password 
        to be use to register on the system
        """
        minPassLength = 8
        maxPassLength = 15


        """Check the Strongness of the password"""
        
        regex = ("^(?=.*[a-z])(?=." + "*[A-Z])(?=.*\\d)" + "(?=.*[-+_!@#$%^&*., ?]).+$")
        p = re.compile(regex)
        """Check the length of the password coming"""
        if len(password) >= minPassLength or len(password) <= maxPassLength:

            """Test the password if it's align to regex structure of Variable Character"""

            if (password == None):
                return False

            elif(re.search(p, password)):
                return True
            
            else:
                return False
        else:
            return False