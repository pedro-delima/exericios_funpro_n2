def adicionar_funcionario(funcionarios):
    print("\n--- Adicionar Funcionário ---")
    
    nome = input("Nome completo: ").strip()
    if not nome:
        print("❌ Nome não pode ser vazio.")
        return
    
    try:
        idade = int(input("Idade: "))
        if idade <= 0:
            print("❌ Idade deve ser maior que zero.")
            return
    except ValueError:
        print("❌ Idade inválida. Deve ser um número inteiro.")
        return

    cargo = input("Cargo: ").strip()
    if not cargo:
        print("❌ Cargo não pode ser vazio.")
        return

    funcionario = {
        'nome': nome,
        'idade': idade,
        'cargo': cargo
    }

    funcionarios.append(funcionario)
    print("✅ Funcionário adicionado com sucesso!")


def listar_funcionarios(funcionarios):
    print("\n--- Lista de Funcionários ---")
    if not funcionarios:
        print("⚠️ Nenhum funcionário cadastrado.")
        return
    
    for i, f in enumerate(funcionarios, start=1):
        print(f"{i}. Nome: {f['nome']} | Idade: {f['idade']} | Cargo: {f['cargo']}")
    print()


def buscar_por_cargo(funcionarios, cargo_busca):
    print(f"\n--- Funcionários com cargo '{cargo_busca}' ---")
    encontrados = [f for f in funcionarios if f['cargo'].lower() == cargo_busca.lower()]
    
    if not encontrados:
        print("⚠️ Nenhum funcionário encontrado com esse cargo.")
    else:
        for f in encontrados:
            print(f"Nome: {f['nome']} | Idade: {f['idade']} | Cargo: {f['cargo']}")
    print()



def menu():
    funcionarios = []

    while True:
        print("\n===== Sistema de Cadastro de Funcionários =====")
        print("1 - Adicionar Funcionário")
        print("2 - Listar Funcionários")
        print("3 - Buscar por Cargo")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_funcionario(funcionarios)
        elif opcao == '2':
            listar_funcionarios(funcionarios)
        elif opcao == '3':
            cargo = input("Digite o cargo a ser buscado: ").strip()
            if cargo:
                buscar_por_cargo(funcionarios, cargo)
            else:
                print("❌ Cargo não pode ser vazio.")
        elif opcao == '4':
            print("👋 Encerrando o programa. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


menu()