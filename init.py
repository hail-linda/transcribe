# coding=utf-8
from dic.stardict import DictCsv
import Image,ImageFont,ImageDraw
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
from matplotlib.font_manager import FontProperties
import json , os , time , random

def init():
	D=DictCsv("dic/ecdict.csv")

	words=open("words.txt")
	word_list = []
	word_info = {}
	for word in words:
		query_result = D.query(word.strip())
		if not query_result == None :
			if query_result.has_key('word') :
				word_info = {
					'word':query_result.get('word'),
					'definition':query_result.get('definition'),
					'translation':query_result.get('translation'),
					'collins':query_result.get('collins'),
					'bnc':query_result.get('bnc'),
					'frq':query_result.get('frq'),
					'start_time':'0',
					'n_yes':'0',
					'n_no':'0',
					't_yes':'0',
					't_no':'0',
					'priority':'0'
					}
				word_list.append(word_info)


	print(str(len(word_list))+" words")
	WriteDatas(word_list)

def ReadDatas():
	for i,j,k in os.walk("./datas"):
		pass

	FileList=[]
	for i in range(len(k)):
		FileList.append(float(k[i][:-5]))

	FileDir = max(FileList)

	with open("./datas/"+str(FileDir)+".json","r") as record:
		read_list = json.load(record)

	return read_list

def WriteDatas(write_list):
	with open("./datas/"+str(time.time())+".json","w") as f:
		json.dump(write_list,f)

def Test(review_pencent):
	print(u"Test Model")
	data=ReadDatas()
	t=time.time()
	endflag=0
	while(1):
		if endflag == 1:
			break
		review=[]
		newword=[]
		for i in range(len(data)):
			if data[i]['start_time'] == "0" :
				newword.append(i)
			else :
				review.append(i)
		print("(newword,review):",len(newword),len(review))

		for k in range(10):
			if random.random()>review_pencent:
				z=random.randint(0,len(newword)-1)
				i=newword[z]
				print(str(data[i]['word'])+"     ? 1:yes 0:no")
				ip1 = raw_input()
				if ip1=="1":
					print(data[i]['translation']+"    ? 1:yes 0:no")
					ip2 = raw_input()
					if ip2=="1":
						data[i]['start_time']=t
						data[i]['n_yes']=1
						data[i]['t_yes']=t
						data[i]['priority']=5
					elif ip2=="0":
						data[i]['start_time']=t
						data[i]['n_no']=1
						data[i]['t_no']=t
						data[i]['priority']=1
				elif ip1 == "0":
					print(data[i]['translation'])
					data[i]['start_time']=t
					data[i]['n_no']=1
					data[i]['t_no']=t
					data[i]['priority']=1
				else :
					endflag=1
					WriteDatas(data)
					print("saved")
					print("(newword,review):",len(newword),len(review),t)
					break

def funcChoose():
	print("1:init\n2:test")
	flag = raw_input()
	if flag == "1":
		init()
	elif flag =="2":
		print("rate of review (0~1)")
		Test(float(raw_input()))

if __name__ == "__main__":
    funcChoose()

