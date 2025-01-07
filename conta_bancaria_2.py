menu = """"

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido!")

    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        
        elif excedeu_limite:
            print("Erro. O valor de saque excede o limite!")    
        
        elif excedeu_saques: # numero limites de saques excedido
            print("Erro. Limite de saques excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: - R$ {valor:.2f}\n"
            numero_saque += 1 

        else:
            print("Valor inválido!")

    elif opcao == "e":
        print("\n================= EXTRATO =================")
        print("Não foram realizadas transações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Número de saques disponíveis: {LIMITE_SAQUES - numero_saque}")
        print("==========================================\n")
    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Opção inválida!")