
class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance, account_type, interest_rate, overdraft_limit):
        self.fname = fname
        self.lname = lname
        self.address = address.split()
        self.account_no = account_no
        self.balance = float(balance)
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.overdraft_limit = overdraft_limit
    
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
        
    def get_address(self):
        return self.address
    
    def deposit(self, amount, df):
        if amount < 0:
            print('Error. Deposit amount less than 0.')
        else:
            df.loc[df['lname'] == self.get_last_name(), 'balance'] += amount
            df.to_csv('customers.csv', index=False, sep=';')
            self.balance+=amount
        
    def withdraw(self, amount, df):
        if amount > self.get_balance():
            print('Error. withdraw amount greater than balance.')
        elif amount < 0:
            print('Error. withdraw amount less than 0.')
        else:
            self.balance-=amount
            df.loc[df['lname'] == self.get_last_name(), 'balance'] -= amount
            df.to_csv('customers.csv', index=False, sep=';')

        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        try:
            option = int(input("Choose your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            return option
    
    def print_details(self):
        print("First name: %s" % self.fname)
        print("Last name: %s" % self.lname)
        print("Account No: %s" % self.account_no)
        print("Address: %s" % self.address[0])
        print('Account Type: %s' % self.account_type)
        print("Interest Rate: %s" % self.interest_rate)
        print("Overdraft Limit: %s" % self.overdraft_limit)
        print(" %s" % self.address[1])
        print(" %s" % self.address[2])
        print(" %s" % self.address[3])
        print(" ")
   
    def run_account_options(self, df):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                try:
                    amount = float(input("\n Please enter amount to be deposited: "))
                except ValueError as e:
                    print("Error. Please enter a number.")
                else:
                    self.deposit(amount, df)
                    self.print_balance()

            elif choice == 2:
                try:
                    withdraw = float(input("\n Please input the amount to withdraw: "))
                except ValueError as e:
                    print("Error. Please enter a number.")
                else:
                    old_balance = self.get_balance()
                    self.withdraw(withdraw, df)

                    print(f'Old Balance: £{old_balance}')
                    print(f'New Balance: £{self.get_balance()}')

            elif choice == 3:
                self.print_balance()
            elif choice == 4:
                fname = input("\n Enter new customer first name: ")
                self.update_first_name(fname)
                sname = input("\nEnter new customer last name: ")
                self.update_last_name(sname)
            elif choice == 5:
                try:
                    hnumber = int(input("\nPlease enter the new address number: "))
                except ValueError as e:
                    print("Error. Please enter a number.")
                else:
                    str_name = input("Please enter the new street name: ")
                    city = input("Please enter the new city: ")
                    post_code = input("Please enter the new postcode: ")

                    address = f'{hnumber}, {str_name}, {city}, {post_code}'

                    df.loc[df['lname'] == self.get_last_name(), 'address'] = address
                    df.to_csv('customers.csv', index=False, sep=';')

                    self.update_address(address)
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
                print ("\n Exit account operations")