import string
fin = open("article.txt") 
output = open("words.txt","w")
words = []
count = 0
for line in fin:
	line = line.replace('-',' ')
	for word in line.split():
		word = word.replace('\"','')
		word = word.replace('\t','')
		word = word.replace(' ','')
		word = word.replace('\'','')
		word = word.replace('!','')
		word = word.replace('?','')

		word = word.strip()
		for i in range(10):
  			word = word.replace(str(i),'')
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		if word not in words and len(word)>1:
			word = word.replace(' ','')
			words.append(word)
			count = count + 1
			print count , ' ' , word
			print >> output, word

fin.close()
output.close()
			
 
