#This script is used to 

from bs4 import BeautifulSoup   #bs4 is the library ; BeautifulSoup is a Python package for parsing XML/HTML documents 
import glob      #glob is useful in any situation where your program needs to look for a list of files on the 
                #filesystem with names matching a pattern
import os

oldpath = '/Users/default/Dropbox/PhD/OIREACHTAS/oireachtas_ans_xml'  #assigning the variable 'path' to the directory
newpath = '/Users/default/Dropbox/PhD/OIREACHTAS/oireachtas_ans_xml_txt'
if not os.path.exists(newpath):                            #if the newpath doesn't exist   (it doesn't!)
	os.mkdir(newpath)										# create the newpath
for filename in glob.glob(oldpath + '/*.xml'):  # this glob.glob finds each xml file, and prints the filename 
    print(filename)
    soup = BeautifulSoup (open(filename, encoding='utf-8').read(), "xml")  #assigns the variable soup to the contents of each file printed 
    																		#above. "xml" here is very important to remove html encoding
    																		#BeautifulSoup default is html, so must use "xml"

    text = soup.get_text()   #assigns variable text to the text extracted from each file printed above 
    print(text)
    
    filename = filename.split('/')[-1]
    filename = newpath + '/' + filename
    with open(filename + '.txt', 'w', encoding='utf-8') as newfile: 
    	newfile.write(text)												#creates a new file with .txt extension encoded with utf-8

# NB - this must be run in py34

