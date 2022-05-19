def imprime(valor):
        print("Valor de c:", valor)
        
def maior_primo(n):

    primos = []
    for i in range(n+1):
        c = 0
        for j in range(n+1):
            if i%(j+1) == 0: 
                c += 1
        if c == 2:
            primos.append(i)
            imprime(c)

    return(max(primos))

def main():
    n1 = input("Digite um número = ")
    maior_primo(n1)

main()


        

 
