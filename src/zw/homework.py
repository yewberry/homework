import random

'''
r: 计算题范围， 10以内，20以内 ...
t: 0:加减法，1:加减乘除
v: 题目数量
'''
def gen_math_calc(rg, t, v, avoid_plain_sub, avoid_plain_mul, avoid_plain_div):
	ops = ['+', '-'] if t==0 else ['+', '-', '*', '/']
	rtn = []
	r = rg + 1
	nums = list(range(1, r))
	str_temp = '{0} {1} {2} ='
	for i in range(v):
		op = random.choice(ops)
		if op == '+':
			while True:
				a = random.choice(nums)
				arr = [x for x in nums if a+x<r]
				if not arr:
					continue
				b = random.choice(arr)
				s = str_temp.format(a, op, b)
				if s not in rtn:
					rtn.append(s)
					break
		elif op == '-':
			while True:
				a = random.choice(nums)
				arr = [x for x in nums if a-x>=0]
				if not arr:
					continue
				b = random.choice(arr)
				s = str_temp.format(a, op, b)
				plain_sub = (a!=b) if avoid_plain_sub else True
				if (s not in rtn) and plain_sub:
					rtn.append(s)
					break
		elif op == '*':
			while True:
				a = random.choice(nums)
				arr = [x for x in nums if a*x<r]
				if not arr:
					continue
				b = random.choice(arr)
				s = str_temp.format(a, '\u00D7', b)
				plain_mul = (a!=1 and b!=1) if avoid_plain_mul else True
				if (s not in rtn) and plain_mul:
					rtn.append(s)
					break
		elif op == '/':
			while True:
				a = random.choice(nums)
				arr = [x for x in nums if a%x==0]
				if not arr:
					continue
				b = random.choice(arr)
				s = str_temp.format(a, '\u00F7', b)
				plain_div = (a!=b) if avoid_plain_div else True
				if (s not in rtn) and plain_div:
					rtn.append(s)
					break
	return rtn

def gen_math_blank(rg, t, v):
	ops = ['+', '-'] if t==0 else ['+', '-', '*', '/']
	rtn = []
	r = rg + 1
	nums = list(range(1, r))
	str_temp = '{0} {1} (  ) = {2}'
	for i in range(v):
		op = random.choice(ops)
		if op == '+':
			while True:
				a = random.choice(nums)
				arr = [x for x in nums if x>a and x!=a]
				if not arr:
					continue
				b = random.choice(arr)
				s = str_temp.format(a, op, b)
				if s not in rtn:
					rtn.append(s)
					break
		elif op == '-':
			while True:
				a = random.choice(nums)
				arr = [x for x in nums if x<a and x!=a]
				if not arr:
					continue
				b = random.choice(arr)
				s = str_temp.format(a, op, b)
				if (s not in rtn):
					rtn.append(s)
					break
		elif op == '*':
			while True:
				a = random.choice(nums)
				arr = [x for x in nums if x%a==0]
				if not arr:
					continue
				b = random.choice(arr)
				s = str_temp.format(a, '\u00D7', b)
				if (s not in rtn):
					rtn.append(s)
					break
		elif op == '/':
			while True:
				a = random.choice(nums)
				arr = [x for x in nums if a%x==0]
				if not arr:
					continue
				b = random.choice(arr)
				s = str_temp.format(a, '\u00F7', b)
				if (s not in rtn):
					rtn.append(s)
					break
	return rtn