# coding=utf-8
from dic.stardict import DictCsv
import Image,ImageFont,ImageDraw
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
from matplotlib.font_manager import FontProperties
import json , os , time , random
from reportlab.lib.pagesizes import A4, portrait, landscape
from reportlab.pdfgen import canvas

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

def test(review_pencent):
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
			else:
				z=random.randint(0,len(newword)-1)
				i=newword[z]
				
def status():
	data=ReadDatas()
	newword = 0 
	priority_1 = 0
	priority_5 = 0
	learning = 0
	for i in range(len(data)):
		if data[i]['start_time'] == "0" :
			newword += 1
		elif data[i]['priority'] == 1:
			priority_1 += 1
		elif data[i]['priority'] == 5:
			priority_5 += 1
		else :
			learning += 1
	print(	"\n\n统计结果:\n"
			+str(len(data))+"  \t总词数\n\n"
			+str(newword)+"  \t新词数\n"
			+str(1.0*newword/len(data)*100.0)[:5]+"%\t比例\n"
			+str(priority_1)+"  \t不会单词数\n"
			+str(1.0*priority_1/len(data)*100.0)[:4]+"%  \t比例\n"
			+str(priority_5)+"  \t已会单词数\n"
			+str(1.0*priority_5/len(data)*100.0)[:4]+"%  \t比例\n"
			+str(learning)+"  \t学习中单词数\n"
			+str(1.0*learning/len(data)*100.0)[:4]+"%  \t比例\n")

def pre_draw(nPages):
	NumberOfWordPerPage = 9
	CopyRow = 2
	CopyCol = 5
	LineSpace = 6
	ColumnSpace = 5
	LineLength = 12
	data=ReadDatas()
	word_number=[]
	character_list=[]	
	for i in range(len(data)):
		if data[i]['priority'] > 0 and data[i]['priority'] < 5 :
			word_number.append(i)
	for i in range(nPages) :
		Graffiti_list=[]
		for j in range(NumberOfWordPerPage):
			z=random.randint(0,len(word_number)-1)

			word = data[word_number[z]]['word']
			translation = data[word_number[z]]['translation'].replace("\n","  ")[:60]

			W=Graffiti()
			W.set_name(word)
			W.set_xy(8,200-20-(CopyRow+1)*LineSpace*j)
			Graffiti_list.append(W)
			
			T=Graffiti()
			T.set_name(translation)
			T.set_xy(8+len(word),200-20-(CopyRow+1)*LineSpace*j)
			Graffiti_list.append(T)

			for m in range(CopyRow):
				for n in range(CopyCol):
					L=Graffiti()
					L.set_name("line")
					L.set_xy(8+(LineLength+ColumnSpace)*n,200-20-(CopyRow+1)*LineSpace*j-(m+1)*LineSpace)
					L.set_length(LineLength)
					Graffiti_list.append(L)
		draw(Graffiti_list,i+1,nPages)
	convert_images_to_pdf("imgs/", "papers/"+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+".pdf")

def convert_images_to_pdf(img_path, pdf_path):
	pages = 0
	(w, h) = portrait(A4)
	c = canvas.Canvas(pdf_path, pagesize = portrait(A4))
	l = os.listdir(img_path)
	l.sort(key= lambda x:int(x[-6:-4]))
	for i in l:
		f = img_path + os.sep + str(i)
		c.drawImage(f, 0, 0, w, h)
		c.showPage()
		pages = pages + 1
	c.save()
	for i in l:
		os.remove(img_path + os.sep + str(i))
	print("finish")

class Graffiti(object):
	def __init__(self):
		self.name = None
		self.x = None
		self.y = None
		self.length = None
	
	def set_name(self,string):
		self.name = string
	
	def set_xy(self,x,y):
		self.x = x
		self.y = y
	
	def set_length(self,integer):
		self.length = integer

def draw(Graffiti_list,whichPage,totalPage):
	#坐标轴配置
	plt.xticks([])
	plt.yticks([])
	plt.axis('off')
	plt.axis([0, 100, 0, 200]) 
	#汉字字体设置
	mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
	mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
	font=FontProperties(fname=r"SIMHEI.TTF") 
	#主图模板
	use_date = "2019-01-17"

	plt.plot([5,95],[185,185],color='black')
	plt.plot([5,95],[10,10],color='black')
	plt.text(70,187,u'打印时间:'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),fontsize=10,fontproperties=font)
	plt.text(6,187,u'页数:'+str(whichPage)+"/"+str(totalPage),fontsize=10,fontproperties=font)

	for G in Graffiti_list :
		if G.name == "line" :
			plt.plot([G.x,G.x+G.length],[G.y,G.y],color='black')
		else :
			plt.text(G.x,G.y,G.name,fontsize=10,fontproperties=font)
	
	plt.tight_layout()
	fig = matplotlib.pyplot.gcf()
	fig.subplots_adjust(bottom=0,left=0,right=1,top=1)
	fig.set_size_inches(8.27,11.69)
	fig.savefig("imgs/"+str(time.strftime("%Y-%m-%d-%H-00", time.localtime()))+str(whichPage)+'.png', dpi=150)
	plt.close('all')
	print(str(whichPage)+"/"+str(totalPage))

def funcChoose():
	print("1:init\n2:test\n3:status\n4:draw\n")
	flag = raw_input()
	if flag == "1":
		init()
	elif flag =="2":
		print("rate of review (0~1)")
		test(float(raw_input()))
	elif flag == "3":
		status()
	elif flag == "4":
		print("number of page")
		pre_draw(int(raw_input()))

if __name__ == "__main__":
    funcChoose()

