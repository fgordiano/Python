def computador_escolhe_jogada(n,m):
 
    for i in range(1,m+1):
        jogada = i

        if (n - jogada) % (m + 1)==0:
            return jogada

    return jogada
    
        
def usuario_escolhe_jogada(n,m):
    continua = True
    
    while continua:
        print("Quantas peças você vai tirar? ")
        jogada = int(input(""))

        if jogada < 1 or jogada > m or jogada > n:
            print("Oops! Jogada inválida! Tente de novo.")
            continua = True
        else:
            continua = False
            return jogada
 

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    primeira_vez = True

    while n > 0:
            if primeira_vez:
                if n%(m+1) == 0:
                    print("")
                    print("")
                    print("Você começa")
                    jogador = "usuario"
                    proximo_jogador = "usuario"
                else:
                    print("")
                    print("")
                    print("Computador começa")
                    jogador = "computador"
                    proximo_jogador = "computador"

                primeira_vez = False

            else:
                if proximo_jogador=="usuario":
                    jogada = usuario_escolhe_jogada(n,m)
                    print("Você tirou ", jogada, " peças.")
                    proximo_jogador = "computador"
                    jogador = "usuario"
                else:
                    jogada = computador_escolhe_jogada(n,m)
                    print("O computador tirou ", jogada, " peça.")
                    proximo_jogador = "usuario"
                    jogador = "computador"
            
                n = n - jogada

                if n==0:
                    if jogador == "computador":
                        print("Fim do jogo! O computador ganhou!!")
                    else:
                        print("Fim do jogo! Você ganhou!!")

                else:
                    print("Agora restam ",n," peça(s) no tabuleiro.")
    return jogador



def campeonato():
    placar_computador=0
    placar_usuario=0
    
    for i in range(1,4):
        print("")
        print("")
        print("**** Rodada ",i, "****")
        print("")
        print("")
        ganhador = partida()
        if ganhador == "computador":
            placar_computador = placar_computador+1
        else:
            placar_usuario = placar_usuario + 1
    print("**** Final do campeonato! ****")
    print("")
    print("")
    print("Placar: Você ", placar_usuario, " X ",  placar_computador , " Computador")
    print("")
    print("")

 
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha = int(input(""))
    print("")
    print("")

    if escolha > 1:
        print("Voce escolheu um campeonato!")
        campeonato()
    else:
        print("Voce escolheu um partida isolada!")
        partida()

main()


        

 
