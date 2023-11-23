import random
pontos_eu = 0
pontos_pc = 0

while(True):
  cor_secreta = random.choice(['R','G','B'])
  palpite = input("adivinhe a cor (R, G, B): ").upper()
  if palpite not in ['R','G','B']:
    print("Entrada inválida. Escolha R, G ou B.")
  elif palpite == cor_secreta:
     print("Parabéns você acertou!")
     pontos_eu = pontos_eu + 1
  if palpite != cor_secreta:
     print(f"Você errou! a cor era {cor_secreta}")
     pontos_pc = pontos_pc + 1
     print(f'VOCE {pontos_eu} x PC {pontos_pc}')