#This file should be in a particular directory for it to run over all files in the folder
#It takes an xml file, uses BeautifulSoup to extract the text from the xml tags and write the text to a new .txt file in the 
#same dir. 

from bs4 import BeautifulSoup
import glob
import os

for file in glob.glob('*.xml'):
	print(file)
	soup = BeautifulSoup (open(file))
	text = soup.get_text()
	with open(file + '.txt', 'w') as newfile:
		newfile.write(text.encode('utf-8'))
