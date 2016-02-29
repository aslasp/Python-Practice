#-*- coding:utf-8 -*-
'''
描述：
蒙特卡罗方法，或称计算机随机模拟方法，是一种基于随机数的计算方法，在金融工程学，宏观经济学，计算物理学等领域应用广泛。
试编写函数solve(a,b)，利用蒙特卡罗方法计算函数f(x)=(e^(-x²/2))/√2√π在区间[a,b]上的定积分并返回，其中b>a>0。
输入：a,b分别为正浮点数
输出：m: 定积分值
注意：
（1）为保证精确性，蒙特卡罗模拟次数至少为100000
（2）不能使用scipy.integrate库
'''
'''
要点：
'''
import random
import math
class Solution:
	def solve(self,a,b):
		n=100000
		k=0
		for i in range(n):
			x=random.uniform(a,b)
			up=((math.e**((-1*(a**2))/2))/((2*math.pi)**0.5))
			y=random.uniform(0.0,up)
			if y<=((math.e**((-1*(x**2))/2))/((2*math.pi)**0.5)):
				k=k+1.0
		return (k/n)*(b-a)*up
t=Solution()
print t.solve(1.0,2.0)

