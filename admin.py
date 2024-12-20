
class Admin:
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
    
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
    
    def set_username(self, uname):
        self.user_name = uname
        
    def get_username(self):
        return self.user_name
        
    def get_address(self):
        return self.address      
    
    def update_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right

    def has_full_admin_right(self):
        return self.full_admin_rights

    def admin_settings(self):
        print("1) Set Name")  # transfer from one account to another
        print("2) Set Address")  # deposit, withdraw, view details, check balance
        print("3) Set Username")  # delete customer if admin has full rights
        print("4) Set Password")  # output all customer details
        print("6) Go back")  # go back to the main menu
        try:
            option = int(input("Choose your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            return option

