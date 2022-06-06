def buscarConsecutivo(*args):
    contador=0

    for i in args:
        if args[contador]== 0 and args[contador+1]== 0:
            return True
        else:
            contador+=1
    return False

r=buscarConsecutivo(1,2,1,0,5,0,0,8,9,10)
print (r)