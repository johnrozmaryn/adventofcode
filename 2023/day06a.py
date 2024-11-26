# f = open("day06.in")
# contents = (f.readlines())
# contents.append('')

# timespaced = contents[0].split(':')[1].strip().strip(' ')
# distspaced = contents[1].split(':')[1].strip().strip(' ')

# time = ''
# dist = ''
# for i in range(len(timespaced)):
#     if timespaced[i].isdigit():
#         time += timespaced[i]
#     if distspaced[i].isdigit():
#         dist += distspaced[i]
time = 51699878
dist = 377117112241505 


wins = 0
t = 1
while t < time:   
    travel = t*(time - t)
    if travel > dist:
        wins += 1
    t += 1
    
# print(time -2*t + 1)
# print(len(lst))
print(wins)

        



