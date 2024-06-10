'''name = str(input('enter your name:'))

print("You're welcome {:^20}!".format(name))'''


num1 = int(input('enter a value : '))

num2 = int(input(' enter another value : '))

s = num1 + num2
m = num1 * num2
d = num1 / num2
pot = num1 ** num2
di = num1 // num2


print(' the sum is {}, the multi is {}, the div is {:.3f}, the pot is {} , the div int is {}'.format(s,m,d,pot,di), end = '>>>')