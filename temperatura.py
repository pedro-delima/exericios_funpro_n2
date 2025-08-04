temperaturas = []

print("Digite as temperaturas dos 10 primeiros dias de agosto (entre 15 e 40 graus):")
for i in range(1, 11):
    while True:
        try:
            temp = float(input(f"Dia {i}: "))
            if 15 <= temp <= 40:
                temperaturas.append(temp)
                break
            else:
                print("Erro: Temperatura deve estar entre 15°C e 40°C.")
        except ValueError:
            print("Erro: Digite um número válido.")


menor = min(temperaturas)
maior = max(temperaturas)
media = sum(temperaturas) / len(temperaturas)
dias_abaixo_da_media = sum(1 for t in temperaturas if t < media)


print("\nResultados:")
print(f"Menor temperatura: {menor:.1f}°C")
print(f"Maior temperatura: {maior:.1f}°C")
print(f"Temperatura média: {media:.1f}°C")
print(f"Número de dias com temperatura inferior à média: {dias_abaixo_da_media}")