from customer_account import CustomerAccount
from admin import Admin
import pandas as pd
pd.set_option('display.max_columns', None) # so the user's data won't be truncated when it is printed to the console

# df.loc[df['account_number'] == account_number, 'balance'] -= withdraw # withdraws money from the balance column

accounts_list = []
admins_list = []

class BankSystem(object):
	def __init__(self):
		# self.accounts_list = []
		self.admins_list = []
		self.load_bank_data()

		# loads the customer data into a dataframe
		self.cu = pd.read_csv('customers.csv', sep=';')
		print(self.cu)

		# loads the admin data into a dataframe
		self.ad = pd.read_csv('admins.csv', sep=';')
		print(self.ad)

	def load_bank_data(self):
		# create customers
		# account_no = 1234
		# customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00)
		# self.accounts_list.append(customer_1)
		#
		# account_no+=1
		# customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00)
		# self.accounts_list.append(customer_2)
		#
		# account_no+=1
		# customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00)
		# self.accounts_list.append(customer_3)
		#
		# account_no+=1
		# customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00)
		# self.accounts_list.append(customer_4)
		# create admins

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

	def search_customers_by_name(self, customer_lname):
		#STEP A.3
		pass

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

		# user_exists = self.ad[(self.ad['user_name'] == username) & (
		# 		self.ad['password'] == int(password))]  # checks if the username and password match
		#
		# if not user_exists.empty:  # if the username and the password are a match
		# 	admin_data = user_exists.iloc[0]  # Get the first matching row (if any)
		#
		# 	# creating the Admin object with the relevant fields
		# 	admin_obj = Admin(
		# 		fname=admin_data['fname'],
		# 		lname=admin_data['lname'],
		# 		address=admin_data['address'],
		# 		user_name=admin_data['user_name'],
		# 		password=admin_data['password'],
		# 		full_rights=admin_data['full_rights'])
		#
		# 	return 'Successfully logged in!', admin_obj
		# else:
		# 	return 'Username or password incorrect.', None  # if they don't match

	def admin_menu(self, admin_obj):
		#print the options you have
		print (" ")
		print ("Welcome Admin %s %s : Available options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
		print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print ("1) Transfer money")
		print ("2) Customer account operations & profile settings")
		print ("3) Delete customer")
		print ("4) Print all customers detail")
		print ("5) Sign out")
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
				lname = input("\n Please input the customer's last name: ")

				cust_obj = self.search_customers_by_name(customer_lname=lname)
				while True:
					# account number is used as a unique identfier
					acc_number = int(input("\nPlease input the customer's account number: "))
					user_exists = self.cu[(self.cu['account_no'] == acc_number)] # checks if the account number exists

					if not user_exists.empty:  # if the account number is a match
						user_data = user_exists.iloc[0]  # Get the first matching row (if any)

						# creating the User object with the relevant fields
						cust_obj = CustomerAccount(
							fname=user_data['fname'],
							lname=user_data['lname'],
							address=user_data['address'],
							account_no=user_data['account_no'],
							balance=user_data['balance'])
					else:
						print('User does not exist.')


			elif choice == 3:
				#Todo
				pass

			elif choice == 4:
				#Todo
				pass

			elif choice == 5:
				loop = 0
		print ("\n Exit account operations")


	def print_all_accounts_details(self):
		# list related operation - move to main.py
		i = 0
		for c in self.accounts_list:
			i+=1
			print('\n %d. ' %i, end = ' ')
			c.print_details()
			print("------------------------")


app = BankSystem()
app.run_main_options()
