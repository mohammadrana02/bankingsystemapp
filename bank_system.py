from customer_account import CustomerAccount
from admin import Admin
import pandas as pd
pd.set_option('display.max_columns', None) # so the user's data won't be truncated when it is printed to the console

admins_list = []

class BankSystem(object):
	def __init__(self):
		self.admins_list = []
		self.load_bank_data()

		# loads the customer data into a dataframe
		self.df = pd.read_csv('customers.csv', sep=';')
		print(self.df)

	def load_bank_data(self):

		admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
		self.admins_list.append(admin_1)

		admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
		self.admins_list.append(admin_2)


	def search_admins_by_name(self, admin_username):
		found_admin = None
		for a in self.admins_list:
			username = a.get_username()
			if username == admin_username:
				found_admin = a
				break
		if found_admin == None:
			print("\n The Admin %s does not exist! Try again...\n" % admin_username)
		return found_admin

	def search_customers_by_name(self, lname):
		user_exists = self.df[(self.df['lname'] == lname)]  # checks if the last name exists

		if not user_exists.empty:  # if the account number is a match
			user_data = user_exists.iloc[0]  # Get the first matching row (if any)

			# creating the User object with the relevant fields
			cust_obj = CustomerAccount(
				fname=user_data['fname'],
				lname=user_data['lname'],
				address=user_data['address'],
				account_no=user_data['account_no'],
				balance=user_data['balance'],
				account_type=user_data['account_type'],
				interest_rate=user_data['interest_rate'],
				overdraft_limit=user_data['overdraft_limit'])

			return 'Success', cust_obj
		else:
			return 'User does not exist.', None

	def main_menu(self):
		#print the options you have
		print()
		print()
		print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print ("Welcome to the Python Bank System")
		print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print ("1) Admin login")
		print ("2) Quit Python Bank System")
		print (" ")
		option = int(input ("Choose your option: "))
		return option


	def run_main_options(self):
		loop = 1
		while loop == 1:
			choice = self.main_menu()
			if choice == 1:
				username = input ("\n Please input admin username: ")
				password = input ("\n Please input admin password: ")
				msg, admin_obj = self.admin_login(username, password)
				print(msg)
				if admin_obj != None:
					self.run_admin_options(admin_obj)
			elif choice == 2:
				loop = 0
		print ("\n Thank-You for stopping by the bank!")



	def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
		#ToDo
		pass


	def admin_login(self, username, password):
		found_admin = self.search_admins_by_name(username)
		msg = "\n Login failed"
		if found_admin != None:
			if found_admin.get_password() == password:
				msg = "\n Login successful"
		return msg, found_admin

	def admin_menu(self, admin_obj):
		#print the options you have
		print (" ")
		print ("Welcome Admin %s %s : Available options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
		print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print ("1) Transfer money") # transfer from one account to another
		print ("2) Customer account operations & profile settings") # deposit, withdraw, view details, check balance
		print ("3) Delete customer") # delete customer if admin has full rights
		print ("4) Print all customers details") # output all customer details
		print("5) Admin settings")
		print("6) Print management report")
		print ("7) Sign out") # sign out
		print (" ")
		option = int(input ("Choose your option: "))
		return option


	def run_admin_options(self, admin_obj):
		loop = 1
		while loop == 1:
			choice = self.admin_menu(admin_obj)
			if choice == 1:
				sender_lname = input("\n Please input sender surname: ")
				amount = float(input("\n Please input the amount to be transferred: "))
				receiver_lname = input("\n Please input receiver surname: ")
				receiver_account_no = input("\n Please input receiver account number: ")
				self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)
			elif choice == 2:
				while True:
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
						self.df.drop(self.df[self.df['lname'] == cust_obj.get_last_name()].index, inplace=True)
						self.df.to_csv('customers.csv', index=False, sep=';')


			elif choice == 4: # print all customer details
				self.print_all_accounts_details()

			elif choice == 5:  # admin settings
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

					hnumber = input("\nPlease enter the new address number: ")
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
					print('Invalid option. Please try again.')

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

	def print_all_accounts_details(self):
		for index, row in self.df.iterrows():  # outputs all the customer details in an ordered format
			for col in self.df.columns:
				print(f"{col}: {row[col]}")
			print()


app = BankSystem()
app.run_main_options()

