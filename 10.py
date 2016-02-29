#-*- coding:utf-8 -*-
'''
描述：
仍然利用NSFG数据（url为http://112.124.1.3:8050/getData/101），验证母亲年龄Y对婴儿出生体重W是否有影响。
假设W=a+bY， 试写函数solve利用最小二乘法拟合a,b的值，并且计算其测定系数r2
输入：调查样本数据，格式为
{“status”:"ok","data":[[1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751], [1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751], ...]}
输出：[a,b,r2]
4,6
'''
import urllib2 as url
import json
class Solution:
	def solve(self):
		webpage=url.urlopen("http://112.124.1.3:8050/getData/101")
		data=json.load(webpage)["data"]
		'''data=[]
		for row in oriData:
			if row[2]<=5 or (row[2]>10 and row[2]<=25) or row[2]>=49:
				continue
			elif row[2]>5 and row[2]<=10:
				row[2]=row[2]*4.33
				data.append(row)
			else:
				data.append(row)'''
		#--------------------------------------
		sumW=sumY=0.0
		n=len(data)
		for row in data:
			sumW=sumW+row[4]
			sumY=sumY+row[6]
		meanW=sumW/n
		meanY=sumY/n
		lxx=lxy=0.0
		for row in data:
			lxy=lxy+(row[4]-meanW)*(row[6]-meanY)
			lxx=lxx+(row[6]-meanY)**2
		b=lxy/lxx
		a=meanW-b*meanY
		#--------------------------------------
		St=Sr=0.0
		for row in data:
			St=St+(row[4]-meanW)**2
			temp=a+b*row[6]
			Sr=Sr+(temp-meanW)**2
		r2=(Sr/St)
		return [a,b,r2]
fsf=Solution()
print fsf.solve()
