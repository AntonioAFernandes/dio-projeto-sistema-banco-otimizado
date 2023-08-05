from datetime import datetime, date, timedelta

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500.00
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
#dataAmanha = date.today() + timedelta(days=1)
#dataAtual = date.today()

#def resetarDia():
#    if (dataAtual == dataAmanha):
#        numero_saques = 0
#        extrato = []


while True:
    
    opcao = input(menu)
    #resetarDia()
    
    if opcao == "d":
        print("Deposito")
        valorDeposito = float(input("Digite o valor a ser depositado: "))
        if valorDeposito < 0:
            print("O valor a ser depositado é negativo! Por favor, insira um valor positivo.")
        else:
            saldo += valorDeposito
            print(f'Valor depositado com sucesso! Seu novo saldo é R$ {saldo:.2f}.')

    elif opcao == "s":
        print("Saque")
        valorSaque = float(input("Digite o valor a ser retirado da conta:"))
        if valorSaque > limite:
            print(f'O valor a ser sacado é maior que o limite de saque! Por favor, insira um valor menor que R$ {limite:.2f}.')
        
        elif valorSaque > saldo:
            print(f'Você não possui dinheiro suficiente na conta para sacar! O seu saldo atual é de R$ {saldo:.2f}, por favor insira um valor menor.')
        
        else:
            if (numero_saques < LIMITE_SAQUES):
                saldo -= valorSaque
                numero_saques += 1
                print(f'Valor sacado com sucesso! Você realizou {numero_saques} saques hoje.')             
                extrato.append(valorSaque)
            else:
                print("Limite de saques diários atingidos!")

    elif opcao == "e":
        print("Extrato")
        print(f'Você possui {saldo:.2f} em sua conta, tendo realizado {numero_saques} saques diários. Você realizou saques no valor de R$ {extrato}.')
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")