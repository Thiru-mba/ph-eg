#Else clause in while
#finding number is greater or smaller

num  = int(input('Enter number:'))
while (num > 0):
    print('value is greater than 0:', num)
    num  = num-1
else:
    print('value is less than or equal to 0:', num)
