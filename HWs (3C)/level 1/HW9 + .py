allowed_users = ["ali","sara","noura","ahmed"]

name = input (' Enter your username : ')

if name.lower() in allowed_users :
    print (f'welcome , {name} !')

else :
    print ('Access denied...')

