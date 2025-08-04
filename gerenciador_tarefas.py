def adicionar_tarefa(lista_tarefas):
    print("\n--- Adicionar Tarefa ---")
    descricao = input("Descrição da tarefa: ").strip()
    if not descricao:
        print("❌ A descrição não pode ser vazia.")
        return

    prioridade = input("Prioridade (alta, média ou baixa): ").strip().lower()
    if prioridade not in ['alta', 'média', 'baixa']:
        print("❌ Prioridade inválida. Use: alta, média ou baixa.")
        return

    tarefa = {
        'descricao': descricao,
        'prioridade': prioridade
    }
    lista_tarefas.append(tarefa)
    print("✅ Tarefa adicionada com sucesso!")



def exibir_tarefas(lista_tarefas):
    print("\n--- Lista de Tarefas ---")
    if not lista_tarefas:
        print("⚠️ Nenhuma tarefa cadastrada.")
        return

    prioridades = ['alta', 'média', 'baixa']
    contador = 1

    for prioridade in prioridades:
        for tarefa in lista_tarefas:
            if tarefa['prioridade'] == prioridade:
                print(f"{contador}. {tarefa['descricao']} [Prioridade: {tarefa['prioridade']}]")
                contador += 1



def concluir_tarefa(lista_tarefas):
    print("\n--- Concluir Tarefa ---")
    if not lista_tarefas:
        print("⚠️ Nenhuma tarefa para concluir.")
        return

    exibir_tarefas(lista_tarefas)

    try:
        num = int(input("Digite o número da tarefa a ser concluída: "))
        if num < 1 or num > len(lista_tarefas):
            print("❌ Número inválido.")
            return

        
        prioridades = ['alta', 'média', 'baixa']
        tarefas_ordenadas = [t for p in prioridades for t in lista_tarefas if t['prioridade'] == p]

        tarefa_removida = tarefas_ordenadas[num - 1]
        lista_tarefas.remove(tarefa_removida)
        print(f"✅ Tarefa '{tarefa_removida['descricao']}' concluída e removida com sucesso!")
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")



def menu():
    lista_tarefas = []

    while True:
        print("\n===== Gerenciador de Tarefas =====")
        print("1 - Adicionar Tarefa")
        print("2 - Exibir Tarefas")
        print("3 - Concluir Tarefa")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa(lista_tarefas)
        elif opcao == '2':
            exibir_tarefas(lista_tarefas)
        elif opcao == '3':
            concluir_tarefa(lista_tarefas)
        elif opcao == '4':
            print("👋 Encerrando o programa. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


menu()