
#-*- coding:utf-8 -*-
'''
实现自己的单因素方差检验
描述：利用python实现简化版单因素方差检验函数
输入：sample1,sample2,... : 不定数量（至少一个）的一维数组；
示例输入 : [1.0,2.0,3.0],[2.0,2.0,3.0]
输出：[F-value, p-value]分别代表检验结果F值与其对应的P值；
示例输出：[0.250000，0.643330]
注意：
（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
（2）sample_i为空时，返回值为[None,None]
（3）结果保留6位小数点
'''
'''
要点：
1.注意判断传入参数行为0和列为0的情况
2.求解过程：
		1.求Sa,Se
			Sa=Qa-C
			Se=Qt-Qa
			Qa:每行数据和的平方之和除以列数
			C:所有数据的和的平方除以数据个数
			Qt:每个数据的平方之和
		2.求fa,fe
			fa:行数-1
			fe:数据个数-行数
		3.求Va,Ve
			Va=Sa/fa
			Ve=Se/fe
		4.求F,P
			F=Va/Ve
			P=scipy.stats.f.sf(F,fa,fe)
'''
import scipy.stats as sci
class Solution():
	def f_oneway(self, *args):
		rowNum=len(args)
		if rowNum==0:
			return [None,None]
		else:
			colNum=len(args[0])
			if colNum==0:
				return [None,None]
			else:
				Qt=0.0
				Qa=0.0
				C=0.0
				for tRow in args:
					rowSum=0.0
					for t in tRow:
						rowSum=rowSum+float(t)
						Qt=Qt+float(t)**2
						C=C+float(t)
					Qa=Qa+rowSum**2
				C=C**2/(rowNum*colNum)	#C is OK,Qt is OK
				Qa=Qa/colNum			#Qa is OK
				#step1-----------------------------------
				Se=Qt-Qa
				Sa=Qa-C
				#step2-----------------------------------
				fa=rowNum-1
				fe=rowNum*colNum-rowNum
				#step3-----------------------------------
				Va=Sa/fa
				Ve=Se/fe
				#step4-----------------------------------
				F=Va/Ve
				P=sci.f.sf(F,fa,fe)
				return [F,P]