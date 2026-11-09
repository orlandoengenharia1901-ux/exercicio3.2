#8. Cálculo de Pontuação: Escreva um código que peça duas pontuações (fase 1 e
#fase 2) e mostre a soma total usando o operador + .

fase1 = int (input("Digite um numero "))
fase2 = int (input("Digite um numero "))
Total = fase1 + fase2
print(f'Resultado {Total}')

#9. Dano de Combate: Crie um script onde o dano_arma = 25 e a
#armadura_inimigo = 10 . Calcule e mostre o dano real sofrido (dano menos
#armadura).

dano_arma = 25
armadura_inimigo = 10
combate = dano_arma - armadura_inimigo
print(f"Combate foi: {combate}")

#10. Divisão de Itens: Você tem 15 poções para dividir igualmente entre 3 jogadores.
#Use o operador / para mostrar quantas poções cada um recebe.

poções = 15
jogadores = 3
divisão = poções / jogadores
print(f"Cada jogador fica com {divisão}")

#11. Verificação de Vida: Escreva um código que peça a vida atual do herói e use o
#operador == para imprimir True se a vida for igual a 0.

vida = int(input("Digite a vida do heroi "))
if vida == 0:
    print(True)

#12. Ranking de Pontos: Crie uma variável pontos_jogador = 150 e verifique se
#ela é maior ou igual ( >= ) a 200 (que seria a pontuação para o próximo nível). Imprima
#o resultado booleano.

pontos_jogador = 150
print(pontos_jogador >= 200)

#13. Operador de Resto (%): O operador % (módulo) devolve o resto da divisão. Use-o
#para verificar se o número de moedas de um jogador é par . (Dica: moedas % 2 ==
#0 ).

moedas = int(input ("Digite o numero de moedas "))
print(moedas % 2 == 0)

#14. Multiplicador de Poder: Se um jogador pega um "Power-up" que triplica o seu
#ataque, qual operador você usaria para atualizar a variável ataque = 15 ? Escreva o
#código.

ataque = 15
multiplicação_de_poder = ataque * 3
print(f"Power-up {multiplicação_de_poder}")
