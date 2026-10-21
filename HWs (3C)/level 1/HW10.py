names = ['Ali','Adam','George','Nada','Dina','Fady']
print ('\n\n''''---------------------------------------------------------''''\n\n')
print (f' This is the students names of your class :\n\n {names}\n\n')
print ( '''

    1. Reverse the list
    2. Sort student names alphabetically
    3. Add a student to the list 

''')

x = input (' Choose 1, 2, or 3 : ')

if x == '1' :
    names.reverse()
    print (f'\n\n    Reversed list : {names} \n\n ')

elif x == '2' :
    names.sort()
    print (f'\n\n    Sorted list : {names} \n\n ')

elif x == '3' :
    y = input ('\n\n Enter the student name you want to add\n\n\n    Name : ')
    names.append(y)
    print (f'\n\n    List : {names} ')

else :
    print ('Error 404')

print ('''---------------------------------------------------------''''\n\n')
