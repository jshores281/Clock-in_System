
from datetime import date
import datetime, time
import os, sys



class time_log:
	def __init__(self):
		if sys.platform == 'linux' or sys.platform == 'linux2':
			#os.system('clear')
			print("OS = ",sys.platform)
		elif sys.platform == 'win32':
			#os.system("cls")
			print("OS = ",sys.platform)

		self.FILENAME = "time-log.txt"
		self.FILE = os.path.join(os.getcwd(), self.FILENAME)
		print("default folder path = ", self.FILE)

		ct = datetime.datetime.now()
		self.CUR_TIME = ct.strftime("%H:%M:%S")
		today = date.today()
		self.CUR_DATE = today.strftime("%m/%d/%Y")



	def capture_time(self):
		# captures current time
		print(f'\nDATE = {self.CUR_DATE}\nTIME = {self.CUR_TIME}\n')
		self.OPTION = input("CHOOSE TO CLOCK [IN/OUT]: ")
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
				time_calc = last_time.split(":")
		# 
				last_hour = int(time_calc[0])
				last_minute = int(time_calc[1])
				last_perc_time = last_minute*(1/60)+last_hour
				#second = time_calc[2]
				cur_time_calc = self.CUR_TIME.split(":")
				cur_hour = int(cur_time_calc[0])
				cur_minute = int(cur_time_calc[1])


				cur_perc_time = cur_minute*(1/60)+cur_hour
				print(f"-LAST CLOCKED ({last_clocked}) AT:\n{last_date}\n{last_time}\n")
				#print("last clock IN time",last_hour, last_minute)
				#print("current clock OUT time", cur_hour, cur_minute)
				if last_perc_time > cur_perc_time:
					night_hour = 24 - last_perc_time
					tot_hourmin = night_hour + cur_perc_time
					print(tot_hourmin)

				elif last_perc_time < cur_perc_time:
					tot_hourmin = cur_perc_time - last_perc_time
					print(tot_hourmin)
					
				elif last_perc_time == cur_perc_time:
					tot_hourmin = cur_perc_time - last_perc_time
					print(tot_hourmin)

				with open(self.FILE, "a") as file:
					file.write(f'{self.OPTION}@-:-{self.CUR_DATE}-:-{self.CUR_TIME}-:-{tot_hourmin}\n')
				print(f"YOU HAVE BEEN CLOCKED **{self.OPTION}**")
				sys.exit()
		except IndexError:
			print("you have no clockins or the log file has been incorrectly altered")
			sys.exit()


	#check if last line is "IN" 
		if self.OPTION == 'IN':
			#print(self.OPTION)
			last_clocked = self.lastline.split("@")[0]
			last_date = self.lastline.split("-:-")[1]
			last_time = self.lastline.split("-:-")[2]
			print(f"-LAST CLOCKED ({last_clocked}) AT:\n{last_date}\n{last_time}\n")

		with open(self.FILE, "a") as file:
			file.write(f'{self.OPTION}@-:-{self.CUR_DATE}-:-{self.CUR_TIME}\n')
		print(f"YOU HAVE BEEN CLOCKED **{self.OPTION}**")
		sys.exit()






	def redun_chk(self):
	# redundancy checks for no file, input is correct, if already clocked in
		if self.FILENAME not in os.listdir():
			fopen = open(self.FILE, 'w')
			fopen.write(f'')
			fopen.close()	
	# check log file if clocked in/out
		with open(self.FILE) as file:
			self.lastline = file.readlines()[-1]
			if self.OPTION == "EXIT":
				print("EXITING PROGRAM")
				time.sleep(3)
				sys.exit()
			elif "IN" != self.OPTION and "OUT" != self.OPTION:
				print("invalid choice")
				input("PRESS [ENTER]")
				time_log()
	# if try to clock in again, give error message: ALREADY CLOCKED IN		
			elif self.OPTION in self.lastline:
				print(f"ALREADY CLOCKED {self.OPTION}")
				input("PRESS [ENTER]")
				time_log()
	# if clock request mismatched with log then do successfully clock requested action
			elif self.OPTION not in self.lastline:
				print(f"\nCLOCKING ({self.OPTION}) AT: \nDATE = {self.CUR_DATE}\nTIME = {self.CUR_TIME}\n")
				tl.clockr()
	# if no clock in send meessage: FIRST CLOCK IN MESSAGE RECORDED
			else:
				print("UNKNOW ERROR")
				input("PRESS [ENTER]")
				time_log()


if __name__ == "__main__":
	while True:
		tl = time_log()
		tl.capture_time()
		try:
			tl.redun_chk()
		except IndexError:
			# check if empty log file control flow ends here
			tl.clockr()
	




















		"""
		DIR_CHG = input("CHANGE TIME-LOG DIRECTORY [Y/N]: ")
		DIR_CHG = DIR_CHG.upper()
		if DIR_CHG == "Y":
			self.FILE = input("ADD FOLDER DIRECTORY: ")
		elif DIR_CHG == "N":
			pass
		else:
			print("WRONG INPUT: ")
		"""
