def spam(divideBy):
    try:
        print('42/'+str(divideBy)+'='+str(42/divideBy))
    except ZeroDivisionError:
        print('YOU CANNOT DIVIDE BY ZERO, IDIOT!!!')

spam(10)
spam(42)
spam(0)
spam(401)
spam(-1)
