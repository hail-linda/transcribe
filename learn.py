#coding=utf-8

import Image,ImageFont,ImageDraw
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time
from pylab import mpl
from matplotlib.font_manager import FontProperties
import json , os
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
	
'''
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
use-date='2018-12-26'
plt.plot([5,95],[185,185],color='black')
plt.plot([5,95],[15,15],color='black')
plt.text(70,187,u'打印时间:'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),fontsize=10,fontproperties=font)
plt.text(6,187,u'使用日期:'+use-date,fontsize=10,fontproperties=font)

plt.tight_layout()
fig = matplotlib.pyplot.gcf()
fig.subplots_adjust(bottom=0,left=0,right=1,top=1)
fig.set_size_inches(8.27,11.69)
fig.savefig(use-date+'.png', dpi=150)

#plt.plot([0,1],[0,2])
plt.show()
'''

