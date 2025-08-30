import random
# comando print será usado para ser a mensagem
print("Olá sobrevivente! Bem vindo a minha selva!")
# comando input será usado para a ação do usuário (programador)
nome = input("Para começar os jogos, me informe teu nome")
idade = int(input("Me informe tua idade, Jogador"))
arte_marcial = input("Me informe tua arte marcial, Forest")
print(f"então {nome}, você tem {idade} e, prática {arte_marcial} correto? Você parece bem forte e me parece que vai sobreviver bem nesta selva perigosa!")

print("Agora vamos jogar um jogo... O jogo será de sorte, conhecido como dado... Prepare-se, será um desafio difícil!")
# código fácil que sera random-dado (um código Basico que me dará um resultado aleatório no caso um número aleatório)
print("Lembre-se, não será um dado qualquer, dependendo do número que cair, será um resultado frustante ou gratificante!")
print("O que cada número dá? 1 - Força sobrehumana 2 - imortalidade 3- Um corpo perfeito 4 - Super força 5 - invisibilidade 6 - Todos os poderes! Boa sorte!")
num_aleatory = random.randint(1, 6)
print(f"O resultado do jogo foi: {num_aleatory}!")
