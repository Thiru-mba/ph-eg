#List
#listing top 4 students marks and making corrections

s1 = [90,90,91,92,95]
s2 = [85,86,82,83]
s3 = [75,78,76,70,79]
s4 = [69,69,68,64,65]
'''finding total subjects for student1 '''
print('Total subjects:', len(s1))

'''there are 5 subjects for student2 only 4 marks only enter, adding a mark'''
s2.append(84)
print('Added mark:', s2)

'''list first two students mark'''
s2.extend(s1)
print(s2)

'''arranging the value larger to smaller'''
s2.sort(reverse=True)
print('Larger to smaller:', s2)

'''find how many times s1 gets 90 mark'''
print('count:',s1.count(90))

'''finding index of given mark '''
print('Index', s4.index(69))

'''find min and max mark s1 & s4'''
print('Minimum mark:', min(s4))
print('Maximum mark', max(s1))

'''changing the mistaken value'''
s3[-2] = 71
print('Change of mark:', s3)

'''Removing the s1 values from s2 '''
s2.pop(0)
s2.pop(1)
s2.pop(2)
s2.pop(3)
s2.pop(4)
print('s2 values:', s2)

'''Calculating total marks'''
print('s1:',sum(s1),'s2:',sum(s2),'s3:',sum(s3),'s4:',sum(s4))

