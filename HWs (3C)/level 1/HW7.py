YorN = 'none'

while YorN :
    order = input ('Enter Your order : ')
    YorN = input ('add another order ? [Y/N] : ')
    if YorN == 'Y' :
        YorN = True
    elif YorN == 'y' :
        YorN = True
    elif YorN == 'N' :
        YorN = False
    elif YorN == 'n' :
        YorN = False
    else :
        print (' Error 404 ')
        YorN = False
