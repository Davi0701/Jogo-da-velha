```
print("A Ilha Misteriosa")

while True:
 escolha = input("Você está na praia. O que fazer? (A) Floresta / (B) Trilha Costeira: ")

 if escolha.upper() == "A":
 mapa = input("Encontrou um mapa. Seguir? (A) Sim / (B) Não: ")
 if mapa.upper() == "A":
 print("Encontrou o tesouro! Escape da ilha.")
 break
 else:
 print("Voltou à praia. Game Over.")
 elif escolha.upper() == "B":
 barco = input("Encontrou um barco. Entrar? (A) Sim / (B) Não: ")
 if barco.upper() == "A":
 print("Afundou! Game Over.")
 else:
 print("Voltou à praia. Game Over.")
 else:
 print("Opção inválida. Tente novamente.")
``