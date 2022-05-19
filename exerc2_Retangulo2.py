largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
cont = 1
altura_aux = altura

while altura_aux > 0:   
    i=largura
    while i>0:
        if cont==1 or cont ==altura:
            print("#", end="")
        elif i==1 or i==largura:
            print("#", end="")
        else:
            print(" ",end="")
        i=i-1
    altura_aux = altura_aux - 1
    cont= cont + 1
    print("")
