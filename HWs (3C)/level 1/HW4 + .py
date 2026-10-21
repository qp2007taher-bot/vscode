num1 = float ( input ('''Num1:
''')) 
op   = input ( '''OP ( + , * , - , / ):
''' )
num2 = float ( input ('''Num2:
'''))

if op == '+':
    num3 = num1 + num2 
elif op == '-':
    num3 = num1 - num2
elif op == '*':
    num3 = num1 * num2
elif op == '/':
    if num2 != 0:            
        num3 = num1 / num2
    else :
        num3 = "Error 1"
else :
    num3 = 'Error 2'


print ('Answer: ' , num3)
