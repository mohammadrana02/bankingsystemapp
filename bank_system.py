from tkinter import messagebox

from customer_account import CustomerAccount
from admin import Admin
import pandas as pd
from tkinter import *
pd.set_option('display.max_columns', None) # so the user's data won't be truncated when it is printed to the console


class BankSystem(object):
	def __init__(self, root):
		self.admins_list = [] # stores the admin objects
		self.load_bank_data()
		self.root = root
		self.root.title('Bank System')
		self.root.geometry('500x500')

		try: # attempts to load the customer data (stores in a csv) into a dataframe while checking for exceptions
			self.df = pd.read_csv('customers.csv', sep=';')
		except FileNotFoundError:
			print("Error: 'customers.csv' not found. Please check the file path.")
			self.df = pd.DataFrame()  # empty dataframe to avoid another crash
		except pd.errors.ParserError:
			print("Error: 'customers.csv' is corrupted or improperly formatted.")

		self.main_menu()

	def clear_window(self):
		for widget in self.root.winfo_children():
			widget.destroy()

	def load_bank_data(self):
		"""loads the admin information into self.admins_list"""

		admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"],
						"id1188", "1441", True)
		self.admins_list.append(admin_1)

		admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"],
						"id3313", "2442", False)
		self.admins_list.append(admin_2)

	def search_admins_by_name(self, admin_username):
		"""searches for admin based on a given username"""
		found_admin = None
		for a in self.admins_list: # looks through the admin usernames in the admin list
			username = a.get_username()
			if username == admin_username:
				found_admin = a
				break
		if found_admin == None:
			print("\n The Admin %s does not exist! Try again...\n" % admin_username)
		return found_admin

	def search_customers_by_name(self, lname):
		"""searches for customers by their last name and returns a customer object if found"""

		# checks the last names in the customers dataframe
		user_exists = self.df[(self.df['lname'] == lname)]

		if not user_exists.empty:
			# if the account number is a match. get the first matching row (if any)
			user_data = user_exists.iloc[0]

			# creating the customer object using the matching fields in the dataframe
			cust_obj = CustomerAccount(
				fname=user_data['fname'],
				lname=user_data['lname'],
				address=user_data['address'],
				account_no=user_data['account_no'],
				balance=user_data['balance'],
				account_type=user_data['account_type'],
				interest_rate=user_data['interest_rate'],
				overdraft_limit=user_data['overdraft_limit'])

			# a success message along with a customer object is returned otherwise an error message with no object
			return 'Success. User found.', cust_obj
		else:
			return 'User does not exist.', None

	def main_menu(self):
		self.header_label = Label(self.root, text='Welcome to the Python Bank System')
		self.header_label.pack()

		self.admin_login_button = Button(self.root, text='Admin Login', command=self.run_main_options)
		self.admin_login_button.pack()

		self.quit = Button(self.root, text='Quit', command=self.root.destroy)
		self.quit.pack()

	def run_main_options(self):
		"""Controls how logic for the main_menu options"""
		self.clear_window()

		self.login_label = Label(self.root, text='Login')
		self.login_label.grid(row=0, column=0, padx=5, pady=5)

		self.login_entry = Entry(self.root)
		self.login_entry.grid(row=0, column=1, padx=5, pady=5)

		self.pass_label = Label(self.root, text='Password')
		self.pass_label.grid(row=1, column=0, padx=5, pady=5)

		self.pass_entry = Entry(self.root)
		self.pass_entry.grid(row=1, column=1, padx=5, pady=5)

		self.login_button = Button(self.root, text='Login', command=self.admin_login)
		self.login_button.grid(row=1, column=2, padx=5, pady=5)

		# loop = 1
		# while loop == 1:
		# 	choice = self.main_menu()
		# 	if choice == 1:
		# 		# the user is prompted to input their username and password
		# 		username = input("\n Please input admin username: ")
		# 		password = input("\n Please input admin password: ")
		# 		msg, admin_obj = self.admin_login(username, password)
		# 		print(msg)
		# 		if admin_obj != None:
		# 			# if the login was successful then it displays the admin options
		# 			self.run_admin_options(admin_obj)
		# 	elif choice == 2:
		# 		# closes the app by ending the loop
		# 		loop = 0
		# 		print ("\n Thank you for stopping by the bank!")
		# 	else: # if the input was invalid the loop will repeat
		# 		print('Invalid input. Try again.')



	def admin_login(self):
		username = self.login_entry.get()
		password = self.pass_entry.get()

		"""Checks if the username and password are correct for the admin"""
		admin_obj = self.search_admins_by_name(username) # first searches for the admin based on username

		if admin_obj != None: # if the admin is found, it checks if the password is correct
			if admin_obj.get_password() == password: # if the details match
				messagebox.showinfo('Success', 'Login successful!')
				self.run_admin_options(admin_obj)
			else:
				messagebox.showerror('Error', 'User not found.')

	def admin_menu(self, admin_obj):

		# """Displays the admin menu and prompts the user to make a choice"""
		# #print the options you have
		# print (" ")
		# print ("Welcome Admin %s %s : Available options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
		# print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		# print ("1) Transfer money") # transfer from one account to another
		# # deposit, withdraw, view details, check balance, update details, print details
		# print ("2) Customer account operations & profile settings")
		# print ("3) Delete customer") # delete customer if admin has full right
		# print ("4) Print all customers details") # output all customer details
		# print("5) Admin settings") # admin can change account details
		# print("6) Print management report")
		# print ("7) Sign out")
		# print (" ")
		# try: # catches any input that isn't an integer
		# 	option = int(input ("Choose your option: "))
		# except ValueError:
		# 	print('Error. Please enter a number.')
		# else:
		# 	return option

	def run_admin_options(self, admin_obj):
		"""Controls the admin options"""
		loop = 1
		while loop == 1:
			choice = self.admin_menu(admin_obj)
			if choice == 1:  # allows the admin to transfer from account to another
				try: # prompts the admin to enter the amount to transfer while checking if the input is a float
					amount = float(input("\n Please input the amount to be transferred: "))
				except ValueError:
					print('Error. Please enter a number.')
				else:
					# prompts user to input sender surname, receive surname and their account number
					sender_lname = input("\n Please input sender surname: ")
					receiver_lname = input("\n Please input receiver surname: ")
					receiver_account_no = input("\n Please input receiver account number: ")
					self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)
			elif choice == 2: # customer account operations and profile settings
				while True: # loop doesn't end until the customer profile is found
					# searches for customer based on last name
					lname = input("\n Please input the customer's last name: ")
					msg, cust_obj = self.search_customers_by_name(lname=lname)
					print(msg)
					if cust_obj is not None:
						cust_obj.run_account_options(self.df)

			elif choice == 3: # closing a user account
				if admin_obj.has_full_admin_right() is False:
					print('You do not have permissions to perform this action.')
				else:
					while True:
						lname = input("\n Please input the customer's last name: ")
						msg, cust_obj = self.search_customers_by_name(lname=lname)
						print(msg)
						try:
							self.df.drop(self.df[self.df['lname'] == cust_obj.get_last_name()].index, inplace=True)
							self.df.to_csv('customers.csv', index=False, sep=';')
						except KeyError as ke: # incorrect dataframe structure
							print(f"Error updating customer data: {ke}")

			elif choice == 4: # displays all customer details
				self.print_all_accounts_details()

			elif choice == 5:  # controls the admin settings
				option = admin_obj.admin_settings()
				if option == 1:
					print(f'Current Name: {admin_obj.get_first_name()}')
					new_lname = input("\n Please input new Last Name: ")
					new_fname = input("\n Please input new First Name: ")

					admin_obj.update_first_name(new_fname)
					admin_obj.update_last_name(new_lname)

					print(f'New Name: {admin_obj.get_first_name(), admin_obj.get_last_name()}')

				elif option == 2:
					print(f'Current Address: {admin_obj.get_address()}')

					try:
						hnumber = int(input("\nPlease enter the new address number: "))
					except ValueError:
						print('Error. Please enter a number.')
					else:
						str_name = input("Please enter the new street name: ")
						city = input("Please enter the new city: ")
						post_code = input("Please enter the new postcode: ")

						address = f'{hnumber}, {str_name}, {city}, {post_code}'
						admin_obj.update_address(address)

						print(f'New Address: {admin_obj.get_address()}')

				elif option == 3:
					print(f'Current Username: {admin_obj.get_username()}')

					new_uname = input("\nPlease enter the new username: ")
					admin_obj.set_username(new_uname)

					print(f'New Username: {admin_obj.get_username()}')

				elif option == 4:
					print(f'Current Password: {admin_obj.get_password()}')
					new_password = input("\nPlease enter the new password: ")
					admin_obj.update_password(new_password)

					print(f'New Password: {admin_obj.get_password()}')
				else:
					print('Invalid option.')

			elif choice == 6: #managment report
				total_money = self.df['balance'].sum()  # The sum of all money the customers currently have in their accounts.
				total_overdrafts = self.df['overdraft_limit'].sum()
				total_customers = self.df.shape[0]

				# temporary column to hold the interest for each customer
				self.df['interest'] = self.df['balance'] * self.df['interest_rate']
				# Calculate the total interest payable
				total_interest_payable = self.df['interest'].sum()

				# Display the dataframe and total interest
				print("\n")
				print('Management Report')

				print(f'Total customers: {total_customers}')
				print(f'Total money: {total_money}')  # calculates total money in the dataframe
				print(f'Overdrafts: {total_overdrafts}')
				print(f"Total Interest Payable: {total_interest_payable}")
				print("\n")

			elif choice == 7:
				loop = 0
				print("\n Exit account operations")
				self.run_main_options()

	def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
		"""Transfers money between two customers"""
		# creates a sender and receiver object
		msg, sender = self.search_customers_by_name(sender_lname)
		msg, receiver = self.search_customers_by_name(receiver_lname)

		# withdraws from sender and deposits into receiver account
		sender.withdraw(amount, self.df)
		receiver.deposit(amount, self.df)

		# displays the updated balances
		print(f'Sender Balance: {sender.get_balance()}')
		print(f'Receiver Balance: {receiver.get_balance()}')

	def print_all_accounts_details(self):
		for index, row in self.df.iterrows():  # outputs all the customer details in an ordered format
			for col in self.df.columns:
				print(f"{col}: {row[col]}")
			print()

r = Tk()
app = BankSystem(r)
r.mainloop()

