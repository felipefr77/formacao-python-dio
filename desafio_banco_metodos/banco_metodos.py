import textwrap

def menu():  
  menu = """
  Informe a opção desejada:
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nc]\tNova Conta
  [lc]\tListar Contas
  [nu]\tNovo Usuário
  [q]\tSair
  """
  return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print("Depósito realizado com sucesso!")
  else:
    print("Valor inválido, deve ser maior que zero")
  return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  if numero_saques >= limite_saques:
    print(f"Você excedeu o limite de {limite_saques} saques diários")
  
  elif valor > limite:
    print (f"Você excedeu o limite de R$ {limite} por saque")
  
  elif valor <= 0.0:
    print("Valor inválido, deve ser maior que zero")
  
  elif valor > saldo:
    print("Valor de saldo insufience para o saque desejado")
  
  else:
    saldo -= valor
    numero_saques += 1
    extrato += f"Saque: R$ {valor:.2f}\n"
  return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
  print(" EXTRATO ".center(39,"=") + "\n")
  print("Não foram realizadas movimentações" if not extrato else extrato )
  print(f"\nSaldo atual R$ {saldo:.2f}\n")
  print(" FIM ".center(39,"="))


def criar_usuario(usuarios):
  cpf = input("Informe o CPF(somente números) ->")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Já existe um usuário com esse CPF!")
    return

  nome = input("Informe o nome completo ->")
  data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa) ->")
  endereco = input("Informe o endereço completo( logradouro, nro, bairro, cidade/UF) ->")
  usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco": endereco})
  print("Usuário cadastrado com sucesso!")


def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF(somente números) ->")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Conta criada com sucesso!")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}

  print("Usuário não encontrado para o CPF informado, operação cancelada!")


def listar_contas(contas):
  if len(contas) == 0:
    print("Nenhuma conta cadastrada!")
  else:
    for conta in contas:
      print( f"Agência {conta['agencia']}, Conta {conta['numero_conta']}, Usuário {conta['usuario']['nome']}")


def main():

  LIMITE_SAQUES = 3
  AGENCIA = "0001"
  limite = 500
  saldo = 0
  numero_saques = 0
  extrato = ""
  usuarios = []
  contas = []
  numero_conta = 1

  while True:
    opcao = menu()
    
    if opcao == "d":
      valor = float(input("Informe o valor do depósito -> "))
      saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == "s":
      valor = float(input("Informe o valor do saque -> "))
      saldo, extrato, numero_saques = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=LIMITE_SAQUES,
      )
  
    elif opcao == "e":
      exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
      criar_usuario(usuarios)

    elif opcao == "nc":
      conta = criar_conta(AGENCIA, numero_conta, usuarios)

      if conta:
        contas.append(conta)
        numero_conta += 1

    elif opcao == "lc":
      listar_contas(contas)

    elif opcao == "q":

      print("Obrigado por nos visitar!")
      break

    else:
      print("Opção inválida")

main()