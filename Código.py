import random

# Este programa é um jogo de sorte onde um herói rola um dado
# para ganhar um poder, baseado em seus atributos.

# --- SEÇÃO DE APRESENTAÇÃO E INTRODUÇÃO ---
while True:
    print("Olá sobrevivente! Bem vindo a minha selva!")

    # --- SEÇÃO DE COLETA DE DADOS DO JOGADOR ---
    nome = input("Para começar os jogos, me informe teu nome: ")
    idade = int(input("Me informe tua idade, Jogador: "))
    
    # Lógica simples para a idade do herói
    if idade > 30:
        print("Você é um herói experiente!")
    else:
        print("Você é um herói jovem, cheio de potencial!")
    
    arte_marcial = input("Me informe tua arte marcial, Forest: ")

    print(f"\nEntão, {nome}, você tem {idade} e pratica {arte_marcial}, correto? Você parece bem forte e vai sobreviver bem nesta selva perigosa!")
    print("Agora vamos jogar um jogo... O jogo será de sorte, conhecido como dado... Prepare-se, será um desafio difícil!")

    # --- SEÇÃO DAS REGRAS DO JOGO ---
    print("\nLembre-se, não será um dado qualquer, dependendo do número que cair, será um resultado frustrante ou gratificante!")
    print("O que cada número dá? 1 - Força sobre-humana 2 - Imortalidade 3 - Um corpo perfeito 4 - Super força 5 - Invisibilidade 6 - Todos os poderes! Boa sorte!")

    # --- SEÇÃO DE ROLAGEM DO DADO E RESULTADO ---
    input("\nPressione Enter para rolar o dado...")
    num_aleatory = random.randint(1, 6)

    print(f"O resultado do jogo foi: {num_aleatory}!")

    # --- SEÇÃO DE LÓGICA DO JOGO (IF/ELIF) ---
    if num_aleatory == 1:
        print("Você ganhou a Força sobre-humana!")
    elif num_aleatory == 2:
        print("Você ganhou a Imortalidade!")
    elif num_aleatory == 3:
        print("Você ganhou um Corpo perfeito!")
    elif num_aleatory == 4:
        print("Você ganhou a Super-Força!")
    elif num_aleatory == 5:
        print("Você ganhou a Invisibilidade!")
    elif num_aleatory == 6:
        print("Você ganhou Todos os poderes! Que sorte, hein!")
