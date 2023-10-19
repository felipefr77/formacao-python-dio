import os
  
LIMITE = 500
LIMITE_SAQUES = 3
saldo = 0
numero_saques = 0
extrato = ""

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

while True:
  
  print("\nInforme a opção desejada:")
  opcao = input(menu)
  os.system('clear')

  if opcao == "d":

    valor = float(input("Informe o valor do depósito -> "))
    
    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      os.system('clear')
    else:
      print("Valor inválido, deve ser maior que zero")    

  elif opcao == "s":

    valor = float(input("Informe o valor do saque -> "))

    if numero_saques >= LIMITE_SAQUES:
      print(f"Você excedeu o limite de {LIMITE_SAQUES} saques diários")
    
    elif valor > LIMITE:
      print (f"Você excedeu o limite de R$ {LIMITE} por saque")
    
    elif valor <= 0.0:
      print("Valor inválido, deve ser maior que zero")
    
    elif valor > saldo:
      print("Valor de saldo insufience para o saque desejado")
    
    else:
      saldo -= valor
      numero_saques += 1
      extrato += f"Saque: R$ {valor:.2f}\n"
      os.system('clear')
  
  elif opcao == "e":
    print(" EXTRATO ".center(39,"=") + "\n")
    print("Não foram realizadas movimentações" if not extrato else extrato )
    print(f"\nSaldo atual R$ {saldo:.2f}\n")
    print(" FIM ".center(39,"="))

  elif opcao == "q":

    print("Obrigado por nos visitar!")
    break

  else:
    print("Opção inválida")
