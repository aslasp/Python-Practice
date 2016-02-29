#-*- coding:utf-8 -*-
'''
描述：利用python实现简化版皮尔森相关系数计算函数
输入：x : 一维数组；y : 一维数组，且x、y长度相同；
示例输入 : [1.0,2.0,3.0],[2.0,2.0,3.0]
输出：[r-val,p-value]分别代表皮尔森相关系数、检验结果P值；
示例输出 : [0.866025,0.333333]
注意：
（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
（2）x,y为空时，返回值为[None,None]
（3）结果保留6位小数点
'''
'''
要点：
1.p-value的求法
	当abs(r)==1的时候，p-value应当为0
	else:
		t=r*(((n-2)/(1-r**2))**0.5)
		p=scipy.stats.t.sf(abs(t),n-2)*2.0
'''
import scipy.stats as sci
class Solution():
	def pearsonr(self, x, y):
		if len(x)==0 or len(y)==0 :
			return [None,None]
		else:
			n=len(x)
			sumXY=sumX=sumY=sumX2=sumY2=0.0
			for t in x:
				sumX=sumX+float(t)
				sumX2=sumX2+float(t)**2
			for t in y:
				sumY=sumY+float(t)
				sumY2=sumY2+float(t)**2
			for i in range(n):
				sumXY=sumXY+float(x[i])*float(y[i])
			#------------------------------------
			r=(n*sumXY-sumX*sumY)/(((n*sumX2-sumX**2)**0.5)*((n*sumY2-sumY**2)**0.5))
			#------------------------------------
			if abs(r)==1.0:
				t=99999999
			else:
				t=(r*((n-2)**0.5))/((1-r**2)**0.5)
			p=sci.t.sf(abs(t),n-2)*2.0
			r=round(r,6)
			p=round(p,6)
			return [r,p]
a=Solution()
print a.pearsonr([1.0,2.0,3.0],[2.0,2.0,3.0])