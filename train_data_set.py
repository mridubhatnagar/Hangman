"""Instructions:
	1. Run train_data_set.py to create seperate files based on word length.
	2. after the data is trained. Run file play.py. 


Data-set.txt file consists of word-list of 800 words. 
Depending on the word length the files are created
eg file "3.txt" contains words with length 3"""



fp=open("data-set.txt","r")
for line in fp:
		a=line
		s=str(len(a)-1)+".txt"
		fp1=open(s,"a")
		fp1.write(a)

print("Trained")
fp.close()