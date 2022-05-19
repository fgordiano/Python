linha=1
coluna=1

while linha <=10:
    while coluna <=10:
        print(linha," x ", coluna,"=", linha * coluna, end="\t")
        coluna = coluna + 1 
    
    coluna=1
    linha=linha + 1

x = 1
cont = 0
i=0
while x < 3:
    y = 0
    while y <= 4:
        i=i+1
        # Iteração
        print("cont = ", y)
        y = y + 1
    x = x + 1

fora = 5
while fora > 0:
  dentro = 0
  while dentro < fora:
    print("oi")
    dentro = dentro + 1
  fora = fora - 1

  tab = 1
    while tab <= 10:
        print("Tabuada do", tab, ":", end="\t")
        i = 1
        while i <= 10:
            print(tab*i, end = "\t")
            i = i + 1
        print()
        tab = tab + 1