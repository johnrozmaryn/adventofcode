def rule1(n):
# two digits are the same, but not part of a group of 3
	s = str(n)
	bReturn = False
	#first, see if there are any doubles. If there aren't, don't have to continue.
	if s[0]==s[1] or s[1]==s[2] or s[2]==s[3] or s[3]==s[4] or s[4]==s[5]:
		for i in range(0,5):
			if s.count(str(i)) == 2:
				bReturn = True
	return bReturn
		
	
def rule2(n):
# from left to right, digits never decrease
	s = str(n)
	return s[0]<=s[1] and s[1]<=s[2] and s[2]<=s[3] and s[3]<=s[4] and s[4]<=s[5]
	
def bothrules(n):
	return rule1(n) and rule2(n)
	
#test = (112233,123444,111122)

#for n in test:
#	print(bothrules(n))

tot = 0
for n in range(240920,789857):
	if bothrules(n):
		tot +=1

print(tot)

