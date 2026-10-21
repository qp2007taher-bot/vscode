N1 = 'Apple juice'
N2 = 'Orange juice'
N3 = 'Strawberry juice'
N4 = 'Mango juice'




P1 = '2.5'
P2 = '3'
P3 = '3.5'
P4 = '4'


name = input ('Enter your name :\n')
print ('\n Hello ' + name + f'\n\nHere is our juice menu:\n1.{N1} -- $2.5\n2.Orange juice -- $3\n3.Strawberry juice -- $3.5\n4.Mango juice -- $4\n\n')

print ('Enter the juice you want (apple [1], orange[2], strawberry[3], mango[4]):\n\n')
x = input ('{1 ,2 ,3 or 4} ? ')

if x =='1':
    print ('The price of ' + N1 + ' is ' + '$' + P1)
elif x =='2':
    print ('The price of ' + N2 + ' is ' + '$' + P2)
elif x =='3':
    print ('The price of ' + N3 + ' is ' + '$' + P3)
elif x =='4':
    print ('The price of ' + N4 + ' is ' + '$' + P4)
else :
    print ("Error404:\n" """sorre, we don't have the juice""")
