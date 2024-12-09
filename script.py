import random  # Biblioteca para gerar números aleatórios
import string  # Biblioteca com caracteres e letras

def gerar_senha(tamanho):
    # Caracteres que podem ser usados na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gera uma senha aleatória com o tamanho especificado
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Pergunta ao usuário o tamanho da senha
try:
    tamanho = int(input("Digite uma senha: "))
    if tamanho > 8:
        senha = gerar_senha(tamanho)
        print(f"Sua senha gerada é: {senha}")
    else:
        print("8 tamanho deve ser maior que oito caracteres.")
except ValueError:
    print("Por favor, insira um número válido.")