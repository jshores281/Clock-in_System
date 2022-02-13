from datetime import date
import datetime, time
import os, sys

class time_log:
	def __init__(self):
		self.FILENAME = "time-log.txt"
		self.FILE = os.path.join(os.getcwd(), self.FILENAME)
		ct = datetime.datetime.now()
		self.CUR_TIME = ct.strftime("%H:%M:%S")
		today = date.today()
		self.CUR_DATE = today.strftime("%m/%d/%Y")

	def capture_time(self):
		print("""
___________.___   _____  ___________         _________ .____    ________  _________  ____  __. 
\__    ___/|   | /     \ \_   _____/         \_   ___ \|    |   \_____  \ \_   ___ \|    |/ _| 
  |    |   |   |/  \ /  \ |    __)_   ______ /    \  \/|    |    /   |   \/    \  \/|      <   
  |    |   |   /    Y    \|        \ /_____/ \     \___|    |___/    |    \     \___|    |  \  
  |____|   |___\____|__  /_______  /          \______  /_______ \_______  /\______  /____|__ \ 
                       \/        \/                  \/        \/       \/        \/        \/ 
  ______________.___. _______________________________   _____                                 
 /   _____/\__  |   |/   _____/\__    ___/\_   _____/  /     \                                 
 \_____  \  /   |   |\_____  \   |    |    |    __)_  /  \ /  \                                
 /        \ \____   |/        \  |    |    |        \/    Y    \                               
/_______  / / ______/_______  /  |____|   /_______  /\____|__  /                               
        \/  \/              \/                    \/         \/                                  
		""")
		if sys.platform == 'linux' or sys.platform == 'linux2':
			#os.system('clear')
			print("\n"*3,"-----------------------------------------------------",
				"\n[X] - OS ::",sys.platform)
		elif sys.platform == 'win32':
			#os.system("cls")
			print("\n"*3,"-----------------------------------------------------",
				"\n[X] - OS ::",sys.platform)
		print("\n[X] - default folder path ::", self.FILE)
		print("[X] - default text editor :: Sublime-Text3")
		try:
			with open(self.FILE) as file:
				self.lastline = file.readlines()[-1]
				print("\n[X] - LAST EVENT ::",self.lastline)
		except IndexError:
			print("\n[X] - NEW FILE NO ENTRIES")
		except FileNotFoundError:
			print("\n[X] - NO FILE FOUND")

	# captures current time and input action
		print(f"-----------------------------------------------------",
			f'\nDATE = {self.CUR_DATE}\nTIME = {self.CUR_TIME}\n',
			f"-----------------------------------------------------")
		self.OPTION = input("CHOOSE AN OPTION [IN/OUT/SHOW/OPEN/EXIT]: ")
		self.OPTION = self.OPTION.upper()


	def clockr(self):
	# clock in status: YOUR CLOCKED IN [OR] YOUR CLOCKED OUT
	# add comments option
		try:
			if self.OPTION == "OUT":
		# get clocked in data 
				last_clocked = self.lastline.split("@")[0]
				last_date = self.lastline.split("-:-")[1]
				last_time = self.lastline.split("-:-")[2]
				last_time_iso = last_time.split(":")
		# gets last time. hour and minute into individual variables
				last_hour = int(last_time_iso[0])
				last_minute = int(last_time_iso[1])
		# converts last time into decimal notation
				last_perc_time = last_minute*(1/60)+last_hour
				#second = time_calc[2]
		# gets clocked out current time. hour and minute into individual variables
				cur_time_iso = self.CUR_TIME.split(":")
				cur_hour = int(cur_time_iso[0])
				cur_minute = int(cur_time_iso[1])

		# converts current time into decimal notation
				cur_perc_time = cur_minute*(1/60)+cur_hour
				print(f"-LAST CLOCKED ({last_clocked}) AT:\n{last_date}\n{last_time}\n",
					f"-----------------------------------------------------")
	
				if last_perc_time > cur_perc_time:
					night_hour = 24 - last_perc_time
					tot_hourmin = night_hour + cur_perc_time

				elif last_perc_time < cur_perc_time:
					tot_hourmin = cur_perc_time - last_perc_time

				elif last_perc_time == cur_perc_time:
					tot_hourmin = cur_perc_time - last_perc_time


				with open(self.FILE, "a") as file:
					file.write(f'{self.OPTION}@-:-{self.CUR_DATE}-:-{self.CUR_TIME}-:-{tot_hourmin}\n')
				print(f"TOTAL HOURS = {tot_hourmin}\nYOU HAVE BEEN CLOCKED **{self.OPTION}**\n",
					f"-----------------------------------------------------")
				input("RETURN TO MENU - [ENTER]")
				time_log()

		except (IndexError, AttributeError):
			print("you have no clockins or the log file has been incorrectly altered")
			input("RETURN TO MENU - [ENTER]")
			time_log()

		try:
	# check if last line is "IN" 
			if self.OPTION == 'IN':
				#print(self.OPTION)
				last_clocked = self.lastline.split("@")[0]
				last_date = self.lastline.split("-:-")[1]
				last_time = self.lastline.split("-:-")[2]
				print(f"-LAST CLOCKED ({last_clocked}) AT:\n{last_date}\n{last_time}\n")

				with open(self.FILE, "a") as file:
					file.write(f'{self.OPTION}@-:-{self.CUR_DATE}-:-{self.CUR_TIME}\n')
				print(f"-----------------------------------------------------",
					f"\nYOU HAVE BEEN CLOCKED **{self.OPTION}**\n",
					f"-----------------------------------------------------")
				input("RETURN - [ENTER]")
				time_log()

		except (IndexError, AttributeError):
			print(f"-----------------------------------------------------",
			f"\n[X] - FIRST CLOCK IN EVENT")
			with open(self.FILE, "a") as file:
				file.write(f'{self.OPTION}@-:-{self.CUR_DATE}-:-{self.CUR_TIME}\n')
			print(f"YOU HAVE BEEN CLOCKED **{self.OPTION}**",
			f"\n-----------------------------------------------------")
			input("RETURN TO MENU - [ENTER]")
			time_log()

	def redun_chk(self):
	# redundancy checks for no file, input is correct, if already clocked in
		if self.OPTION == "EXIT":
			print("EXITING PROGRAM")
			sys.exit()
		try:
	# check log file if clocked in/out
			with open(self.FILE) as file:
				self.lastline = file.readlines()[-1]
				if self.OPTION == "SHOW":
					with open(self.FILE, 'r') as file:
						read_file = file.read(1)
						if not read_file: 
							print("NO RECORDS FOUND")
							pass
						print(file.read())
					input("RETURN TO MENU - [ENTER]")
					time_log()
			# NO EXCEPTION BUG creates clock in record with show
				elif self.OPTION == "OPEN":
					
					if sys.platform == 'linux' or sys.platform == 'linux2':
						os.system("subl time-log.txt")
					
					elif sys.platform == 'win32':
						os.system("sublime time-log.txt")


					input("RETURN TO MENU - [ENTER]")
					time_log()
				elif self.OPTION != "IN"  and self.OPTION != "OUT":
					print("invalid choice")
					input("RETURN TO MENU - [ENTER]")
					time_log()
		# if try to clock in again, give error message: ALREADY CLOCKED IN		
				elif self.OPTION in self.lastline:
					print(f"-----------------------------------------------------",
						f"\nALREADY CLOCKED {self.OPTION}")
					last_clocked = self.lastline.split("@")[0]
					last_date = self.lastline.split("-:-")[1]
					last_time = self.lastline.split("-:-")[2]
					print(f"-LAST CLOCKED ({last_clocked}) AT:\n{last_date}\n{last_time}\n",
					f"-----------------------------------------------------",)
					input("RETURN TO MENU - [ENTER]")
					time_log()
		# if clock request mismatched with log then do successfully clock requested action
				elif self.OPTION not in self.lastline:
					print(f"-----------------------------------------------------",
					f"\nCLOCKING ({self.OPTION}) AT: \nDATE = {self.CUR_DATE}\nTIME = {self.CUR_TIME}\n")
					tl.clockr()
		# if no clock in send meessage: FIRST CLOCK IN MESSAGE RECORDED
				else:
					print("UNKNOW ERROR")
					input("RETURN TO MENU - [ENTER]")
					time_log()
		except FileNotFoundError:
			if self.FILENAME not in os.listdir():
				print(f"-----------------------------------------------------",
				f"\n[X] - NO FILE FOUND [{self.FILENAME}]")
				fopen = open(self.FILE, 'w')
				fopen.write(f'')
				fopen.close()
				print(f"[X] - CREATING NEW FILE",
				f"\n-----------------------------------------------------\n")
				input("RETURN TO MENU - [ENTER]")
		except IndexError:
			tl.clockr()



if __name__ == "__main__":
	while True:
		tl = time_log()
		tl.capture_time()
		try:
			tl.redun_chk()
		except IndexError:
			# check if empty log file control flow ends here
			tl.clockr()
