import nltk
from nltk.corpus import PlaintextCorpusReader

corpus_root = '/Users/default/nltk_data/corpora/short_corp'
# short_corp is a sample corpus.

short_corp = PlaintextCorpusReader(corpus_root, '.*\.txt')    # regular expression for 'filename.txt' 
																# . means any character
																# * means 0 or more times
																# \. means the actual full stop character
																# txt is the sequence of characters txt

fileids = short_corp.fileids()
print 'fileids'
print fileids
for fileid in short_corp.fileids():
	fileid = fileid.decode('utf8')
	print (fileid.encode('utf8'))	 #here, need to give it a filename to get the words back
	
print(fileids)

#wordlist = short_corp.words()
#short_corp.words()[0:10]

#print(wordlist)