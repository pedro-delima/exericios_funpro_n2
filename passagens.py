assentos = {i: 'Disponível' for i in range(1, 21)}

def mostrar_assentos():
    print("\nStatus dos Assentos:")
    for numero, status in assentos.items():
        print(f"Assento {numero}: {status}")
    print()

def reservar_assento():
    try:
        num = int(input("Digite o número do assento que deseja reservar (1 a 20): "))
        if num not in assentos:
            print("❌ Assento inválido.")
        elif assentos[num] == 'Reservado':
            print("⚠️ Esse assento já está reservado.")
        else:
            assentos[num] = 'Reservado'
            print(f"✅ Assento {num} reservado com sucesso!")
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")

# Menu principal
while True:
    print("\n===== Sistema de Reserva de Ônibus =====")
    print("1 - Ver assentos disponíveis")
    print("2 - Reservar um assento")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        mostrar_assentos()
    elif opcao == '2':
        reservar_assento()
    elif opcao == '3':
        print("Encerrando o sistema. Obrigado!")
        break
    else:
        print("❌ Opção inválida. Tente novamente.")