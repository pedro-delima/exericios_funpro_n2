import random

categorias = {
    "Mamíferos": ["cachorro", "gato", "elefante", "baleia", "urso"],
    "Aves": ["papagaio", "águia", "coruja", "pombo", "falcão"],
    "Répteis": ["jacaré", "crocodilo", "cobra", "lagarto", "tartaruga"]
}

def exibir_categorias():
    print("Categorias disponíveis:")
    for i, categoria in enumerate(categorias.keys(), start=1):
        print(f"{i}. {categoria}")

def escolher_categoria():
    while True:
        exibir_categorias()
        escolha = input("Escolha uma categoria pelo nome: ").strip()
        if escolha in categorias:
            return escolha
        else:
            print("❌ Categoria inválida. Tente novamente.\n")

def jogo_adivinhacao():
    print("🎮 Bem-vindo ao Jogo de Adivinhação de Animais!\n")
    
    categoria_escolhida = escolher_categoria()
    palavra_secreta = random.choice(categorias[categoria_escolhida])
    tentativas = []

    print(f"\n🔍 Dica: A palavra tem {len(palavra_secreta)} letras.")

    while True:
        palpite = input("Digite seu palpite: ").strip().lower()
        if not palpite:
            print("⚠️ O palpite não pode ser vazio.")
            continue

        tentativas.append(palpite)

        if palpite == palavra_secreta.lower():
            print(f"\n🎉 Parabéns! Você acertou a palavra '{palavra_secreta}'!")
            print(f"🔢 Total de tentativas: {len(tentativas)}")
            print(f"📋 Palpites: {', '.join(tentativas)}")
            break
        else:
            print("❌ Palpite incorreto. Tente novamente.\n")


jogo_adivinhacao()