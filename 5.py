#-*- coding:utf-8 -*-
'''
描述：利用python实现简化版双样本K-S检验函数
输入：a,b分别为非空一维数组；
示例输入 : [1.0,2.0,3.0],[1.0,2.0,3.0]
输出：ks-value为检验结果KS值；
示例输出 : 0.333333
注意：（1）不能调用math、scipy、numpy包
'''
'''
要点：
1.data1,data2传的是数据值
2.思路：用其中一组的每一个数据点做一组，另外一个数组以它作为分组依据
'''
class Solution():
	def ks_2samp(self, data1, data2):
		data1.sort()
		data2.sort()
		step1=1.0/len(data1)
		step2=1.0/len(data2)
		#------------------------------------
		star1=star2=0.0
		result=0.0
		for temp1 in data1:
			star1=star1+step1
			star2=0.0
			for temp2 in data2:
				if temp2<=temp1:
					star2=star2+step2
				else:
					break
			tempResult=abs(star1-star2)
			if tempResult>result:
				result=tempResult
		return result