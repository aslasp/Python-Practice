#-*- coding:utf-8 -*-
'''
要点：
1.数组size为0时返回4个None
2.var的值为b2/(n-1)
3.数组size为1时var=None,skew=0.0,kurt=-3
4.不要忘了round
'''
class Solution():
    def describe(self, a):
        sum=0.0
        n=len(a)
        if n==0:
            return [None,None,None,None]
        else:
            for t1 in a:
                sum=sum+float(t1)
            mean=sum/n
            mean=round(mean,6)
            b2=b3=b4=0.0
            for t2 in a:
                b2=b2+(float(t2)-mean)**2
                b3=b3+(float(t2)-mean)**3
                b4=b4+(float(t2)-mean)**4
            if n==1:
                var=None
                skew=0.0
                kurt=-3
            else:
                var=b2/(n-1)
                var=round(var,6)
                b2=b2/n
                b3=b3/n
                b4=b4/n
                skew=b3/((b2)**1.5)
                kurt=b4/((b2)**2)
                skew=round(skew,6)
                kurt=round(kurt,6)-3.0
            return [mean,var,skew,kurt]