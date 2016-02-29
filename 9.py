#-*- coding:utf-8 -*-
'''
描述：

仍然利用NSFG数据（url为http://112.124.1.3:8050/getData/101），
但这次我们想验证第一胎婴儿是否更倾向于更早或更晚出生而较少准时出生的假设，
因此需要利用卡方检验计算出其卡方值chisq及推翻假设的p值。
试写函数solve计算卡方值chisq及p值
输入：调查样本数据，格式为
{“status”:"ok","data":[[1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751], [1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751], ...]}
输出：[chisq,p]
注意：
（1）婴儿第几周出生数据由于被调查人选填错误等原因出现了一些不合理数据，
比如错填了月份（5<prglength<=10），其他错填（prglength<=5, 10<prglength<=25, prglength>=49），
对于错填月份的情况，将月份*4.33作为其周数，对于其他错填情况则舍弃此条数据
（2）一般认为，如果婴儿在第37周或更早出生，那就是提前出生；准时出生则是在第38周到第40周；而延后出生则是在41周或更晚
'''
import urllib2 as url
import scipy.stats as sci
import json
class Solution:
	def solve(self):
		webpage=url.urlopen("http://112.124.1.3:8050/getData/101")
		oriData=json.load(webpage)["data"]
		data=[]
		for row in oriData:
			if row[2]<=5 or (row[2]>10 and row[2]<=25) or row[2]>=49:
				continue
			elif row[2]>5 and row[2]<=10:
				row[2]=row[2]*4.33
				data.append(row)
			else:
				data.append(row)
		#------------------------------------------------------------------
		n=len(data)
		earlyNum=puncNum=lateNum=0.0
		earlyFirst=puncFirst=lateFirst=0.0
		firstNum=0.0
		for row in data:
			prgNo=row[5]
			prglen=row[2]
			if prgNo==1:
				firstNum+=1
				if prglen<=37:
					earlyNum+=1
					earlyFirst+=1
				elif prglen>=41:
					lateNum+=1
					lateFirst+=1
				else:
					puncNum+=1
					puncFirst+=1
			else:
				if prglen<=37:
					earlyNum+=1
				elif prglen>=41:
					lateNum+=1
				else:
					puncNum+=1
		Pearly=earlyNum/n
		Ppunc=puncNum/n
		Plate=lateNum/n
		result=((earlyFirst-firstNum*Pearly)**2)/(firstNum*Pearly)+((puncFirst-firstNum*Ppunc)**2)/(firstNum*Ppunc)+((lateFirst-firstNum*Plate)**2)/(firstNum*Plate)
		p=sci.chi2.sf(result,2)
		return [result,p]
sdf=Solution()
print sdf.solve()