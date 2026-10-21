name  = 'none'
birth = '0000'

def HW11():
    print ('\n\n-----------------------------------------\n\n')
    def username(name,birth):
        x = name + birth
        return x
    name  = input ('    your name ? ')
    birth = input ('    year of birth ? ')
    print (f'\n\nYour username will be : {username(name,birth)}')
    print ('\n\n-----------------------------------------\n\n')

HW11()
