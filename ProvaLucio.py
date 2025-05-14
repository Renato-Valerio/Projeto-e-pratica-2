from clientes import menu_clientes
from contas import menu_contas
from operacoes import menu_operacoes

def main():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Contas")
        print("3. Realizar Operações Bancárias")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_contas()
        elif opcao == "3":
            menu_operacoes()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

    clientes = []

def adicionar_cliente():
    cpf = input("Digite o CPF do cliente: ")
    nome = input("Digite o nome do cliente: ")
    cliente = {"cpf": cpf, "nome": nome}
    clientes.append(cliente)
    print(f"Cliente {nome} adicionado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente registrado.")
    else:
        print("\n=== Lista de Clientes ===")
        for cliente in clientes:
            print(f"CPF: {cliente['cpf']}, Nome: {cliente['nome']}")

def editar_cliente():
    cpf = input("Digite o CPF do cliente que deseja editar: ")
    cliente_encontrado = None
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado:
        nome_novo = input(f"Novo nome (atual: {cliente_encontrado['nome']}): ")
        cliente_encontrado['nome'] = nome_novo
        print(f"Cliente {cpf} atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")

def menu_clientes():
    while True:
        print("\n=== MENU DE CLIENTES ===")
        print("1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Editar Cliente")
        print("0. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            editar_cliente()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

            contas = []

def criar_conta():
    numero_conta = input("Digite o número da conta: ")
    agencia = input("Digite a agência: ")
    saldo = float(input("Digite o saldo inicial: "))
    conta = {"numero_conta": numero_conta, "agencia": agencia, "saldo": saldo}
    contas.append(conta)
    print(f"Conta {numero_conta} criada com sucesso!")

def listar_contas():
    if not contas:
        print("Nenhuma conta registrada.")
    else:
        print("\n=== Lista de Contas ===")
        for conta in contas:
            print(f"Conta: {conta['numero_conta']}, Agência: {conta['agencia']}, Saldo: R${conta['saldo']:.2f}")

def editar_conta():
    numero_conta = input("Digite o número da conta que deseja editar: ")
    conta_encontrada = None
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            conta_encontrada = conta
            break
    
    if conta_encontrada:
        novo_saldo = float(input(f"Novo saldo (atual: R${conta_encontrada['saldo']:.2f}): "))
        conta_encontrada['saldo'] = novo_saldo
        print(f"Conta {numero_conta} atualizada com sucesso!")
    else:
        print("Conta não encontrada.")

def menu_contas():
    while True:
        print("\n=== MENU DE CONTAS ===")
        print("1. Criar Conta")
        print("2. Listar Contas")
        print("3. Editar Conta")
        print("0. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            listar_contas()
        elif opcao == "3":
            editar_conta()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

            def deposito():
    numero_conta = input("Digite o número da conta para depósito: ")
    conta_encontrada = None
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            conta_encontrada = conta
            break
    
    if conta_encontrada:
        valor = float(input("Digite o valor para depósito: R$"))
        conta_encontrada['saldo'] += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def saque():
    numero_conta = input("Digite o número da conta para saque: ")
    conta_encontrada = None
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            conta_encontrada = conta
            break
    
    if conta_encontrada:
        valor = float(input("Digite o valor para saque: R$"))
        
        if valor > conta_encontrada['saldo']:
            print("Saldo insuficiente!")
        else:
            conta_encontrada['saldo'] -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def consultar_saldo():
    numero_conta = input("Digite o número da conta para consultar saldo: ")
    conta_encontrada = None
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            conta_encontrada = conta
            break
    
    if conta_encontrada:
        print(f"Saldo da Conta {numero_conta}: R${conta_encontrada['saldo']:.2f}")
    else:
        print("Conta não encontrada.")

def menu_operacoes():
    while True:
        print("\n=== MENU DE OPERAÇÕES BANCÁRIAS ===")
        print("1. Depósito")
        print("2. Saque")
        print("3. Consultar Saldo")
        print("0. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            deposito()
        elif opcao == "2":
            saque()
        elif opcao == "3":
            consultar_saldo()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")