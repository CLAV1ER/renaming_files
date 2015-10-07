# Renaming File Names by removing numbers
# Revealing secret message after file renaming

import os
	def remain_files():
	# 1 get file names from folder
	file_list = os.listdir(r"C:\OOP\prank")
	print(file_list)
	saved_path = os.getcwd()
	os.chdir(r"c:\OOP\prank") # changes directory
	# 2 rename each file names
	for file_name in file_list:
		print("Old name - " + file_name)
		print("New Name - " + file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_list ()
