import random

'''
r: 计算题范围， 10以内，20以内 ...
t: 0:加减法，1:加减乘除
v: 题目数量
'''
def gen_math_calc(r, t, v):
	ops = ['+', '-'] if t==0 else ['+', '-', '*', '/']
	rtn = []
	nums = list(range(1, r))
	for i in range(v):
		op = random.choice(ops)
		if op == '+':
			while True:
				a = random.choice(nums)
				b = random.choice([x for x in nums if a+x<=r])
				s = '{0} {1} {2} ='.format(a, op, b)
				if s not in rtn:
					rtn.append(s)
					print(s)
					break
		elif op == '-':
			while True:
				a = random.choice(nums)
				b = random.choice([x for x in nums if a-x>=0])
				s = '{0} {1} {2} ='.format(a, op, b)
				if (s not in rtn) and (a!=b):
					rtn.append(s)
					print(s)
					break
		elif op == '*':
			while True:
				a = random.choice(nums)
				b = random.choice([x for x in nums if a*x<=r])
				s = '{0} {1} {2} ='.format(a, '\u00D7', b)
				if (s not in rtn) and (a!=1 and b!=1):
					rtn.append(s)
					print(s)
					break
		elif op == '/':
			while True:
				a = random.choice(nums)
				b = random.choice([x for x in nums if a%x==0])
				s = '{0} {1} {2} ='.format(a, '\u00F7', b)
				if (s not in rtn) and (a!=b):
					rtn.append(s)
					print(s)
					break
	return rtn			
				




