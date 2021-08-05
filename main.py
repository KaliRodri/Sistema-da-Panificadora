import os

while (True):
  print ("1 - Vendas do Dia e Relatório")
  print ("2 - Estoque de ingredientes")
  print ("3 - Sobre")
  print ("4 - Sair")
  opcao = input ("Digite a Opção Desejada: ")
  print(opcao)

  if (opcao == "1"):
     os.system('clear')
     print("Nova venda")
     sal_qt = int(input ("Digite a quantidade de pães de Sal: "))
     leite_qt = int(input ("Digite a quantidade de pães de Leite: "))
     milho_qt = int(input ("Digite a quantidade de pães de Milho: "))
     total_vendas = sal_qt*0.15 + leite_qt*0.10 + milho_qt*20
     total = sal_qt  + leite_qt + milho_qt
     print ("Total de pães: %.0f deu R$ %.2f" "\n" % (total, total_vendas)) 
     if ((sal_qt > leite_qt) and (sal_qt > milho_qt)):
       print ("O pão mais vendido hoje foi o de Sal " "\n")
     elif ((leite_qt > sal_qt) and (leite_qt > milho_qt)):
       print ("O pão mais vendido hoje foi o de Leite " "\n")
     elif ((milho_qt > sal_qt) and (milho_qt > leite_qt)):
       print ("O pão mais vendido hoje foi o de Milho " "\n")
  elif (opcao == "2"):
    os.system('clear')
    massa = 150
    farinha = 120
    leite = 170
    milho = 90
    fermento = 80
    ovos = 90
    massa_usada = input ("Quantos kilos de massa foram usado hoje? " "\n")
    farinha_usada = input ("Quantos kilos de farinha foram usado hoje? " "\n")
    leite_usado = input ("Quantos litros de leite foram usado hoje? " "\n")
    milho_usado = input ("Quantos kilos de milho foram usado hoje? " "\n")
    fermento_usado = input ("Quantos kilos de fermento foram usado hoje? " "\n")
    ovos_usados = input ("Quantos ovos foram usado hoje? " "\n")
    massa_restante = int (massa) - int (massa_usada)
    farinha_restante = int (farinha) - int (farinha_usada)
    leite_restante = int (leite) - int (leite_usado)
    milho_restante = int (milho) - int (milho_usado)
    fermento_restante = int (fermento) - int (fermento_usado)
    ovos_restante = int (ovos) - int (ovos_usados)
    print ("Ainda sobraram " + str (massa_restante) + " kilos de massa, " + str (farinha_restante) + " kilos de farinha, " + str (leite_restante) + " litros de leite, " + str (milho_restante) + " kilos de milho, " + str (fermento_restante) + " kilos de de fermento, e " + str (ovos_restante) + " ovos restantes" "\n")
    if (massa_restante < 30):
      print ("É recomendável comprar mais sacas de massa" "\n")
    if (farinha_restante < 50):
      print ("É recomendável comprar mais sacas de farinha" "\n")
    if (leite_restante < 60):
      print ("É recomendável comprar mais sacas de leite" "\n")
    if (milho_restante < 15):
      print ("É recomendável comprar mais sacas de milho" "\n")
    if (fermento_restante < 10):
      print ("É recomendável comprar mais sacas de fermento" "\n")
    if (ovos_restante < 20):
      print ("É recomendável comprar mais sacas de ovos" "\n") 

     
    
   
  elif (opcao == "3"):
    print ("Sobre")
    print ("Feito por Ian Rodrigo, em Python usando a plataforma Replit, Ago/2021" "\n")
    
  elif (opcao == "4"):
    print ("Sair")
    break
  else:
    print("Opção não válida, tente novamente ")
print ("Programa Finalizado")


 
