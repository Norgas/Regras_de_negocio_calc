def fatorial(x):
    fatlist = []
    while x > 1:
        fatlist.append(x)
        x -= 1
    resul = 1
    for x in fatlist:
        resul = resul * x
    return(resul)
