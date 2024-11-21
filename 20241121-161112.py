``
# Jogo da Velha

# Tabuleiro
tabuleiro = [' ' for _ in range(9)]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro():
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")

# Função para verificar vitória
def verificar_vitoria(jogador):
    vitória = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontais
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticais
        (0, 4, 8), (2, 4, 6)  # Diagonais
    ]
    for combinacao in vitória:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

# Função para jogar
def jogar():
    jogador_atual = 'X'
    while True:
        imprimir_tabuleiro()
        print(f"Jogador {jogador_atual}, escolha uma posição (1-9):")
        posicao = int(input()) - 1
        if tabuleiro[posicao] != ' ':
            print("Posição ocupada! Escolha outra.")
            continue
        tabuleiro[posicao] = jogador_atual
        if verificar_vitoria(jogador_atual):
            imprimir_tabuleiro()
            print(f"Jogador {jogador_atual} venceu!")
            break
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Iniciar jogo
jogar()
```
