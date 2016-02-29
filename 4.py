#-*- coding:utf-8 -*-
'''
描述：利用python实现简化版单总体T检验函数
输入：a : 非空一维数组；popmean：假设总体期望值；
示例输入 : [1.0,2.0,3.0],2.0
输出：[t-val,p-value]分别代表检验结果T值与其对应的P值；
示例输出 : [0.000000,1.000000]
注意：
（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
（2）结果保留6位小数点
'''
'''
要点：
1.注意：S是方差开根号！
2.scipy.stats.t.sf(abs(t),n-1)*2
'''
import scipy.stats as sci
class Solution():
	def ttest_1samp(self, a, popmean):
		sum=0.0
		n=len(a)
		for t in a:
			sum=sum+float(t)
		mean=sum/n
		if n==1:
			return [0.0,0.0]
		else:
			S=0.0
			for te in a:
				S=S+((float(te)-mean)**2)
			S=(S/(n-1))**0.5
			tr=(mean-popmean)/(S/(n**0.5))
			p=sci.t.sf(abs(tr),n-1)*2
			tr=round(tr,6)
			p=round(p,6)
			return [tr,p]