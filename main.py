import os

PAO_SAL = 0.15
PAO_LEITE = 0.10
PAO_MILHO = 0.20

quantidade_vendas = 0

sal_qtd = 0
leite_qtd = 0
milho_qtd = 0

def Venda():
      os.system('clear')
      print(" *** Vendas *** ""\n")
      print("Vendas do Dia""\n")
      meta_diaria = 150
      sal_qt = int(input ("Digite a quantidade de saída pães de Sal: "))
      leite_qt = int(input ("Digite a quantidade de saída pães de Leite: "))
      milho_qt = int(input ("Digite a quantidade de saída pães de Milho: " ))
      total_vendas = sal_qt*PAO_SAL + leite_qt*PAO_LEITE + milho_qt*PAO_MILHO
      total = sal_qt  + leite_qt + milho_qt
      print ("\n" "Foram vendidos " + str(sal_qt) + " pães de sal, " + str(leite_qt) + " pães de leite e " + str(sal_qt) + " pães de milho, totalizando %.0f de pães vendidos e R$ %.2f de caixa" "\n" % (total, total_vendas)) 
      if ((sal_qt > leite_qt) and (sal_qt > milho_qt)):
        print ("O pão mais vendido hoje foi o de Sal " "\n")
      elif ((leite_qt > sal_qt) and (leite_qt > milho_qt)):
        print ("O pão mais vendido hoje foi o de Leite " "\n")
      elif ((milho_qt > sal_qt) and (milho_qt > leite_qt)):
        print ("O pão mais vendido hoje foi o de Milho " "\n")
      if (int(total_vendas == meta_diaria)):
        print ("Parabéns, vocês bateram a meta do dia!" "\n")
      elif (int(total_vendas < meta_diaria)):
        print ("Infelizmente não batemos a meta, vamos nos esforçar mais" "\n")
      elif (int(total_vendas > meta_diaria)):
        print ("Parabéns, vocês superaram a meta do dia! Ótimo trabalho!" "\n")
        print ("Quantidade de Vendas:" "\n")

      global quantidade_vendas, sal_qtd, milho_qtd, leite_qtd
      quantidade_vendas = quantidade_vendas + 1
      sal_qtd = sal_qtd + sal_qt
      milho_qtd = milho_qtd + milho_qt
      leite_qtd = leite_qtd + leite_qt
      print(quantidade_vendas)

      input("\n\nPressione ENTER para continuar: ")
      os.system('clear')

def Mercadorias():
    os.system('clear')
    print(" *** Mercadorias *** ""\n")
    print("Estoque de Ingredientes""\n")
    massa = 110
    farinha = 90
    leite = 100
    milho = 40
    fermento = 50
    ovos = 50
    massa_usada = input ("Quantos kilos de massa foram usado hoje? " "\n")
    farinha_usada = input ("Quantos kilos de farinha foram usado hoje? " "\n")
    leite_usado = input ("Quantos litros de leite foram usado hoje? " "\n")
    milho_usado = input ("Quantos kilos de milho foram usado hoje? " "\n")
    fermento_usado = input ("Quantos kilos de fermento foram usado hoje? " "\n")
    ovos_usados = input ("Quantos ovos foram usado hoje? " "\n")
    massa_restante = float (massa) - float (massa_usada)
    farinha_restante = float (farinha) - float (farinha_usada)
    leite_restante = float (leite) - float (leite_usado)
    milho_restante = float (milho) - float (milho_usado)
    fermento_restante = float (fermento) - float (fermento_usado)
    ovos_restante = int (ovos) - int (ovos_usados)
    print ("Ainda sobraram " + str (massa_restante) + " kilos de massa, " + str (farinha_restante) + " kilos de farinha, " + str (leite_restante) + " litros de leite, " + str (milho_restante) + " kilos de milho, " + str (fermento_restante) + " kilos de de fermento, e " + str (ovos_restante) + " ovos restantes" "\n")
    if (massa_restante < 55):
      print ("É recomendável comprar mais sacas de massa" "\n")
    if (farinha_restante < 45):
      print ("É recomendável comprar mais sacas de farinha" "\n")
    if (leite_restante < 50):
      print ("É recomendável comprar mais sacas de leite" "\n")
    if (milho_restante < 25):
      print ("É recomendável comprar mais sacas de milho" "\n")
    if (fermento_restante < 25):
      print ("É recomendável comprar mais sacas de fermento" "\n")
    if (ovos_restante < 25):
      print ("É recomendável comprar mais sacas de ovos" "\n") 


def relatorio():
  os.system('clear') 
  print(" *** Relatório do Dia *** ""\n")
  print("\n")
  print("Quantidade de vendas do dia: ", quantidade_vendas)
  print("\nQuantidade por tipo de pão:")
  print("\t+ Sal: %.0f unidades = R$ %0.2f reais" %(sal_qtd, sal_qtd*PAO_SAL))
  print("\t+ Milho: %.0f unidades = R$ %0.2f reais" %(milho_qtd, milho_qtd*PAO_MILHO))
  print("\t+ Leite: %.0f unidades = R$ %0.2f reais" %(sal_qtd, leite_qtd*PAO_LEITE))

  print("\nMais vendidos: ")


  print("\nValor total do dia: R$ reais")

  input("\n\nPressione ENTER para continuar: ")
  os.system('clear')


def Sobre():
  print ("Sobre""\n")
  print ("Feito por Ian Rodrigo, em Python usando a plataforma Replit, Ago/2021, entre em contato comigo pelo email ianrodrigo25@gmail.com e no meu gitHub KaliRodri" "\n")


while (True):
  print ("Quantidade de Vendas:" + str(quantidade_vendas) + "\n")
  print ("1 - Vendas do Dia e Relatório")
  print ("2 - Estoque de ingredientes")
  print ("3 - Relatório")
  print ("4 - Sobre")
  print ("5 - Sair")
  opcao = input ("Digite a Opção Desejada: ")
  print(opcao)

  if (opcao == "1"):
    Venda()
       
  elif (opcao == "2"):
    Mercadorias() 
  
  elif (opcao == "3"):
    relatorio() 
   
  elif (opcao == "4"):
    Sobre()
    
  elif (opcao == "5"):
    print ("Sair")
    break
  else:
    print("Opção não válida, tente novamente ")
print ("Programa Finalizado")




 
