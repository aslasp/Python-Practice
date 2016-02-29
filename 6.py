#-coding:utf-8-
'''
描述：利用python实现简化版独立检验函数
输入：A为二维数组，每行代表总体X的一个水平上的取值，每列代表总体Y的一个水平上的取值；
示例输入 : [[1.0,2.0,3.0],[2.0,2.0,3.0]]
输出：[c-val,p-value]分别代表检验结果C值与其对应的P值；
示例输出 : [0.257937,0.879002]
注意：
（1）A中只有一行时，返回结果为[0.0,None]
（2）结果保留6位小数点
'''
'''
要点：

'''
import scipy.stats as sci
class Solution():
	def getT(self,A,i,j,sum):
		ni=0.0
		nj=0.0
		for c in A[i]:
			ni=ni+c
		for index in range(len(A)):
			nj=nj+A[index][j]
		return (ni*nj/sum)

	def independence_test(self, A):
		rowNum=len(A)
		colNum=len(A[0])
		if rowNum==1:
			return [0.0,None]
		else:
			result=0.0
			sum=0.0
			for i in range(rowNum):
				for j in range(colNum):
					sum=sum+float(A[i][j])

			for i in range(rowNum):
				for j in range(colNum):
					t=self.getT(A,i,j,sum)
					result=result+((A[i][j]-t)**2)/t
			p=sci.chi2.sf(result,(rowNum-1)*(colNum-1))
			result=round(result,6)
			p=round(p,6)
			return [result,p]

a=Solution()
print a.independence_test([[1.0,2.0,3.0],[2.0,2.0,3.0]])