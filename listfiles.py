#Lists all files in a directory

import os, sys

path = "/Users/default/Desktop/oireachas_answers_txt"
textfiles = os.listdir(path)

for file in textfiles:
	print(file)