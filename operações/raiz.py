def raiz_oper(x):
    global resul
    resul = x ** (1/y)
    oper = input("oper: ")
    if oper == "raiz" :
        raiz_oper(resul)
   

