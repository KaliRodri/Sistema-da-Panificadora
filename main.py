import os

while (True):
  print ("1 - Nova Venda")
  print ("2 - Gerar relatório")
  print ("3 - Sobre")
  print ("4 - Sair")
  opcao = input ("Digite a Opção Desejada: ")
  print(opcao)

  if (opcao == "1"):
     os.system('clear')
     print("Nova venda")
     sal_qt = int(input ("Digite a quantidade de pães de Sal"))
     leite_qt = int(input ("Digite a quantidade de pães de Leite"))
     milho_qt = int(input ("Digite a quantidade de pães de Milho"))
     total = sal_qt + leite_qt + milho_qt
     print ("Total de pães: %.0f deu R$ %.2f" % (total, total*0.25)) 
  elif (opcao == "2"):
    print ("Relatório")
   
  elif (opcao == "3"):
    print ("Sobre")
    
  elif (opcao == "4"):
    print ("Sair")
    break
  else:
    print("Opção não válida, tente novamente ")
print ("Programa Finalizado")


 
