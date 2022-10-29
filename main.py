from funcoes import limparTela, lerPalavra

competidor=input("Insira o nome do competidor:")
desafiante=input("insira o nome do desafiante:")
limparTela()

palavra=input("Desafiante insira a palavra chave: ")

tamanhoPalavra=lerPalavra(palavra)

todasAsDicas = []

dica1 = input("Desafiante insira a primeira dica: ")
todasAsDicas.append(dica1)
dica2 = input("Desafiante insira a segunda dica: ")
todasAsDicas.append(dica2)
dica3 = input("Desafiante insira a terceira dica: ")
todasAsDicas.append(dica3)

print(todasAsDicas)
input()
limparTela()

converteAsterisco = tamanhoPalavra * "*"
print(converteAsterisco)

letrasUsadas=[]
jogar=True
erros=0
numletras = []




while jogar:
    errosContador=erros+1
    print("{}, qual opção deseja realizar?" .format(competidor))
    print("> Digite 1 para solicitar uma dica!")
    print("> Digite 2 para chutar uma letra!")
    escolha = int(input("Informe sua escolha: "))
 

    if escolha==2:
      
      
       letra = str(input("informe uma letra: "))
       if letra in palavra:
                    for i in range(len(palavra)):
                        if palavra[i] == letra:
                           print("VOCE ACERTOU A LETRA")
                           numletras.append(letra)
                    if numletras==palavra:
                        print("VITORIA DO JOGADOR!!!")
                           
       else:
        errosContador
        print ("VOCE TEM:",errosContador,"erros")
        erros=errosContador
        if errosContador==5:
            print("O COMPETIDOR NAO TEM MAIS TENTATIVAS! \n",  "VITORIA DO DESAFIANTE, MEUS PARABENS!!!!")
            print( "FIM DE JOGO, OBRIGADO POR JOGAR!!!")
            break
    else:
        print(dica1)
   
   
        
   
   
        