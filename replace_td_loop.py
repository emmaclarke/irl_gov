import os, sys

path = '/Users/default/Dropbox/PhD/OIREACHTAS/oireachtas_answers_xml'
dir = os.listdir (path)

suffix = 'a.xml'

def read_replace(filename): 
	global new_text
	source_file = open(path + '/' + filename, 'r')
	text = source_file.read()
	source_file.close()
	new_text = text.replace('<td>', '<td> ')
	return(new_text)

def new_file(filename):
	newfile = open(path + '/' + filename + '_td' + '.xml', 'w')
	newfile.write(new_text)
	newfile.close()

for filename in dir:
	if filename.endswith(suffix):
	 	read_replace(filename)
	 	new_file(filename)