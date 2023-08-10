import random

menu = """
***************MENU***************
[c] Criar nova conta corrente
[u] Criar novo usuário
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
**********************************
=> """

saldo = 0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuario = {1: {}}
conta_corrente = []

def realizarDeposito(valor, saldo, extrato):
    print('imprimindo')
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    print(saldo)
    return saldo, extrato
            
def realizarSaque(valor, saldo, numero_saques, extrato, limite, LIMITE_SAQUES, /):
    if valor > saldo:
           print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
           print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
           print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}\n"
           numero_saques += 1
    else:
         print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def retornarExtrato(extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def inserirUsuario(nome, dataNascimento, cpf, endereco, bairro, estado):
    endereco = " - ".join([endereco, bairro, estado])
    cpfLimpo = cpf.replace(".", "").replace("-", "")
    for chave in usuario:
        if cpfLimpo == "cpf" in usuario[1]:
            print("O CPF informado já está cadastrado.")
    else: 
        usuario[1].update({"nome": nome, "dataNascimento": dataNascimento, "cpf": cpfLimpo, "endereco": endereco})
        print(usuario[1])

def criarContaCorrente(agencia, numero, usuario):
    conta_corrente.append({"agencia": agencia, "numero": numero, "usuario": usuario})
    print(conta_corrente)

while True:

    opcao = input(menu)
    
    if opcao == "c":
        agencia = "0001"
        numero = random.randint(1000, 9999)
        criarContaCorrente(agencia, numero, usuario)
        print("Conta criada com sucesso!")
        
    elif opcao == "u":
        nome = input("Digite o seu nome: ")
        dataNascimento = input("Digite a sua data de nascimento: ")
        cpf = input("Digite o seu CPF: ")
        endereco = input("Digite o seu endereço de moradia: ")
        bairro = input("Digite o bairro em que mora: ")
        estado = input("Digite a sigla do estado em que mora: ")
        inserirUsuario(nome, dataNascimento, cpf, endereco, bairro, estado)
        print("Usuário criado com sucesso!")

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = realizarDeposito(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        realizarSaque(valor, saldo, numero_saques, extrato, limite, LIMITE_SAQUES)

    elif opcao == "e":
        extrato = retornarExtrato(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")