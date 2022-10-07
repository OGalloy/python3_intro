import re
import csv

def write_wins_count(username:str, number:int):
	all_lines = []
	flag = False
	with open("database.csv", "r") as csv_file:
		reader = csv.DictReader(csv_file, fieldnames = ["user", "user_wins", "bot_wins"], delimiter = ";")
		for row in reader:
			if row["user"] == username and number == 1:
				flag = True
				row["user_wins"] = (int(row["user_wins"]) + 1)
				all_lines.append(row)
				continue
			if row["user"] == username and number == -1:
				flag = True
				row["bot_wins"] = (int(row["bot_wins"]) + 1)
				all_lines.append(row)
				continue
			all_lines.append(row)
	if flag == False:
		with open("database.csv", "a", newline='\n') as csv_file:
			writer = csv.DictWriter(csv_file, fieldnames = ["user", "user_wins", "bot_wins"], delimiter = ";")
			if number == 1:
				writer.writerow({"user": username, "user_wins": "1", "bot_wins": "0"})
			if number == -1:
				writer.writerow({"user": username, "user_wins": "0", "bot_wins": "1"})
		return print('New user was created!!!')
	if flag == True:
		with open("database.csv", "w", newline='\n') as csv_file:
			writer = csv.DictWriter(csv_file, fieldnames = ["user", "user_wins", "bot_wins"], delimiter = ";")
			for dic in all_lines:
				writer.writerow(dic)

def read_wins_count(username: str):
	with open("database.csv", "r") as csv_file:
		reader = csv.DictReader(csv_file, fieldnames = ["user", "user_wins", "bot_wins"], delimiter = ";")
		for row in reader:
			if row["user"] == username:
				return row

write_wins_count("sdsd", -1) 
	