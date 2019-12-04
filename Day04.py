def rule1(n):
# two digits are the same
	s = str(n)
	return s[0]==s[1] or s[1]==s[2] or s[2]==s[3] or s[3]==s[4] or s[4]==s[5]
	
def rule2(n):
# from left to right, digits never decrease
	s = str(n)
	return s[0]<=s[1] and s[1]<=s[2] and s[2]<=s[3] and s[3]<=s[4] and s[4]<=s[5]
	
def bothrules(n):
	return rule1(n) and rule2(n)
	
count = 0
for n in range(240920,789857):
	if bothrules(n):
		count +=1

print(count)
	